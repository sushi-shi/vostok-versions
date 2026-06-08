{
  description = "Survarium cross-version sources + toolchain: archive.org installers innoextracted to survarium.{exe,pdb}, plus the delink/diff tools on a devShell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    rust-overlay = {
      url = "github:oxalica/rust-overlay";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    # The delink/diff toolchain, fetched from its public source repos (non-flake
    # checkouts used directly as derivation sources).
    vostok-delinker-src = {
      url = "github:srp-survarium/vostok-delinker";
      flake = false;
    };
    vostok-pdb-parser-src = {
      url = "github:srp-survarium/vostok-pdb-parser";
      flake = false;
    };
  };

  outputs = { self, nixpkgs, rust-overlay, vostok-delinker-src, vostok-pdb-parser-src }:
    let
      systems = [ "x86_64-linux" ];
      forAll = nixpkgs.lib.genAttrs systems;

      # Single source of truth, shared with scripts/*.py (which read it as JSON).
      versions = builtins.fromJSON (builtins.readFile ./versions.json);

      pkgsFor = system: import nixpkgs {
        inherit system;
        overlays = [ rust-overlay.overlays.default ];
      };
    in
    {
      packages = forAll (system:
        let
          pkgs = pkgsFor system;

          # Nightly Rust, matching what the delinker/pdb-parser were developed
          # against (they use nightly-only features).
          rust = pkgs.rust-bin.nightly.latest.default.override {
            extensions = [ "rust-src" ];
          };
          nightly-rustPlatform = pkgs.makeRustPlatform { cargo = rust; rustc = rust; };

          # ---------------------------------------------------------------------
          # vostok-delinker - splits an EXE into per-unit COFF .obj files for
          # objdiff, using the PDB for symbol names + function boundaries.
          #
          # cargoHash: update by running `nix build .#vostok-delinker` after
          # `nix flake update vostok-delinker-src` - Nix reports the new hash.
          # ---------------------------------------------------------------------
          vostok-delinker = nightly-rustPlatform.buildRustPackage {
            pname = "vostok-delinker";
            version = "0.1.0";
            src = vostok-delinker-src;
            cargoHash = "sha256-ry3TH1fz7Aj/JdbmlgQFFn29m8E7EQHyGaVXnZTEcXo=";
          };

          # ---------------------------------------------------------------------
          # vostok-pdb-parser - PDB tooling; provides the `pdb_parser` binary that
          # emits readable C++ structure stubs from a build's survarium.pdb.
          #
          # cargoHash: update by running `nix build .#vostok-pdb-parser` after
          # `nix flake update vostok-pdb-parser-src` - Nix reports the new hash.
          # ---------------------------------------------------------------------
          vostok-pdb-parser = nightly-rustPlatform.buildRustPackage {
            pname = "vostok-pdb-parser";
            version = "0.1.0";
            src = vostok-pdb-parser-src;
            cargoHash = "sha256-XUF9ca0D1k5NhR6tZth2/yactZ1NyWc8W9voWNRXcDI=";
          };

          # ---------------------------------------------------------------------
          # objdiff-cli - upstream's prebuilt Linux binary (not in nixpkgs). It is
          # a foreign ELF for a normal FHS distro, so autoPatchelfHook rewrites its
          # interpreter + RPATH into the store. It dlopen's nothing, so the C++
          # runtime alone is enough (no LD_LIBRARY_PATH wrapper needed).
          # ---------------------------------------------------------------------
          objdiffVersion = "3.7.1";
          objdiff-cli = pkgs.stdenv.mkDerivation {
            pname = "objdiff-cli";
            version = objdiffVersion;
            src = pkgs.fetchurl {
              url = "https://github.com/encounter/objdiff/releases/download/v${objdiffVersion}/objdiff-cli-linux-x86_64";
              hash = "sha256-QNhW2gHgpnbA8zr1NOVi8JjNUORey2Tzs0ZBjHsmSuY=";
            };
            dontUnpack = true; # a bare binary; nothing to unpack
            nativeBuildInputs = [ pkgs.autoPatchelfHook ];
            buildInputs = [ pkgs.stdenv.cc.cc.lib ]; # libstdc++ / libgcc_s
            installPhase = "install -Dm755 $src $out/bin/objdiff-cli";
          };

          # ---------------------------------------------------------------------
          # One `version-<label>` package per registry entry: fetch the installer
          # from archive.org and innoextract it to a dir holding survarium.{exe,pdb}
          # (largest non-uninstaller survarium.exe, sibling files copied alongside).
          # ---------------------------------------------------------------------
          # Two packaging formats seen on archive.org: InnoSetup .exe installers
          # (2013 builds) and plain .7z trees (2014 builds, "survarium_full_*").
          extract = v:
            let
              installer = pkgs.fetchurl {
                name = builtins.baseNameOf v.url;
                url = v.url;
                sha256 = v.sha256;
              };
              is7z = pkgs.lib.hasSuffix ".7z" v.url;
              unpack =
                if is7z
                then ''7z x -y -oextract "${installer}" >/dev/null''
                else ''innoextract -d extract "${installer}"'';
              # A build flagged symbols=false (e.g. a stripped retail-style drop)
              # is allowed through without a PDB; the delink step just won't apply.
              requirePdb = (v.symbols or true);
            in
            pkgs.runCommand "survarium-${v.label}" {
              nativeBuildInputs = [ pkgs.innoextract pkgs.p7zip ];
            } ''
              mkdir extract
              ${unpack}
              surv_exe=$(find extract -iname survarium.exe ! -path "*uninstall*" \
                -printf "%s %p\n" | sort -rn | head -1 | awk '{print $2}')
              if [ -z "$surv_exe" ]; then
                echo "ERROR: survarium.exe not found in ${v.label}"; exit 1
              fi
              dir=$(dirname "$surv_exe")
              if [ ! -e "''${surv_exe%.exe}.pdb" ] && ! ls "$dir"/*.pdb >/dev/null 2>&1; then
                ${if requirePdb
                  then ''echo "ERROR: no .pdb beside survarium.exe in ${v.label} (symbol-less build)"; exit 1''
                  else ''echo "WARNING: ${v.label} has no .pdb (symbols=false); extracting exe only"''}
              fi
              mkdir -p "$out"
              cp -r "$dir"/. "$out"/
            '';

          # Dots in a label would split the `nix build .#attr` CLI path, so the
          # package attribute uses an underscore-sanitized label (scripts/common.py
          # applies the same transform). The human label keeps its dots.
          versionPkgs = builtins.listToAttrs (map (v: {
            name = "version-${builtins.replaceStrings [ "." ] [ "_" ] v.label}";
            value = extract v;
          }) versions);
        in
        versionPkgs // {
          inherit vostok-delinker vostok-pdb-parser objdiff-cli;
        }
      );

      # `nix develop` puts the whole delink/diff toolchain on PATH, so the scripts
      # run with no *_BIN env vars set. innoextract + p7zip cover both archive
      # formats; python3/ruff/ripgrep/jq are the script + inspection tooling.
      devShells = forAll (system:
        let
          pkgs = pkgsFor system;
          p = self.packages.${system};
        in
        {
          default = pkgs.mkShell {
            name = "vostok-versions";
            packages = [
              p.vostok-delinker
              p.vostok-pdb-parser
              p.objdiff-cli
              pkgs.innoextract
              pkgs.p7zip
              pkgs.python3
              pkgs.ruff
              pkgs.ripgrep
              pkgs.jq
            ];
          };
        }
      );
    };
}
