# vyos-module-tailscale

A module for adding tailscale functionality to Vyos. To be used with [vyos-modular](https://github.com/jack-broadway/vyos-modular).

This repo now implements version 2 of the vyos-modular spec. If you are using legacy vyos-modular please point to the sagitta or equuleus branches

# Usage

Add this to your vyos-modular config

```yml
modules:
  - type: git
    url: https://github.com/jack-broadway/vyos-module-tailscale.git
    version: main
```
# Developing

If there is common code between vyos versions, create a symlink to that folder/file to the oldest common version 
(i.e if your code works for current, saggita, and equuleus; current and saggita should symlink to the equuleus implementation)