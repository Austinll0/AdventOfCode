# shell.nix
{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell
{
    nativeBuildInputs = [
        pkgs.python3
    ];
}
