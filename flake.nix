{
  description = "Survarium cross-version sources: archive.org installers, innoextracted to survarium.{exe,pdb}";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" ];
      forAll = nixpkgs.lib.genAttrs systems;

      # Single source of truth, shared with scripts/*.py (which read it as JSON).
      versions = builtins.fromJSON (builtins.readFile ./versions.json);
    in
    {
      # One `version-<label>` package per registry entry: fetch the installer
      # from archive.org and innoextract it to a dir holding survarium.{exe,pdb}
      # (mirrors vostok-review's extraction heuristic - largest non-uninstaller
      # survarium.exe, with its sibling files copied alongside).
      packages = forAll (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};

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
        in
        # Dots in a label would split the `nix build .#attr` CLI path, so the
        # package attribute uses an underscore-sanitized label (scripts/common.py
        # applies the same transform). The human label keeps its dots.
        builtins.listToAttrs (map (v: {
          name = "version-${builtins.replaceStrings [ "." ] [ "_" ] v.label}";
          value = extract v;
        }) versions)
      );
    };
}
