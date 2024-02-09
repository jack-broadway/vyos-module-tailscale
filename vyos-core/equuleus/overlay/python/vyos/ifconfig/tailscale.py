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

    def _create(self):
        # we can not create this interface as it is managed outside
        pass

    def _delete(self):
        # we can not create this interface as it is managed outside
        pass
