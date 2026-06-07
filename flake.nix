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
          extract = v:
            let
              installer = pkgs.fetchurl {
                name = "${v.label}-installer.exe";
                url = v.url;
                sha256 = v.sha256;
              };
            in
            pkgs.runCommand "survarium-${v.label}" {
              nativeBuildInputs = [ pkgs.innoextract ];
            } ''
              mkdir extract
              innoextract -d extract "${installer}"
              surv_exe=$(find extract -iname survarium.exe ! -path "*uninstall*" \
                -printf "%s %p\n" | sort -rn | head -1 | awk '{print $2}')
              if [ -z "$surv_exe" ]; then
                echo "ERROR: survarium.exe not found in ${v.label}"; exit 1
              fi
              if [ ! -e "''${surv_exe%.exe}.pdb" ] && ! ls "$(dirname "$surv_exe")"/*.pdb >/dev/null 2>&1; then
                echo "ERROR: no .pdb beside survarium.exe in ${v.label} (symbol-less build)"; exit 1
              fi
              mkdir -p "$out"
              cp -r "$(dirname "$surv_exe")"/. "$out"/
            '';
        in
        builtins.listToAttrs (map (v: {
          name = "version-${v.label}";
          value = extract v;
        }) versions)
      );
    };
}
