# vyos-module-tailscale

A module for adding tailscale functionality to Vyos. To be used with [vyos-modular](https://github.com/jack-broadway/vyos-modular)

# Usage

Add this to your vyos-modular config

```yml
modules:
  - type: git
    url: https://github.com/jack-broadway/vyos-module-tailscale.git
    version: main
```  

For ami, crux and equuleus builds, use `version: main`  

For current builds, use `version: current`
