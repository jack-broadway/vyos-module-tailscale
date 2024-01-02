from vyos.ifconfig.interface import Interface


@Interface.register
class TailscaleIf(Interface):
    iftype = "tailscale"
    definition = {
        **Interface.definition,
        **{
            "section": "tailscale",
            "prefixes": [
                "tailscale",
            ],
            "bridgeable": False,
        },
    }
