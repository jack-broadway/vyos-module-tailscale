#!/usr/bin/env python3
from sys import exit

from subprocess import TimeoutExpired

from vyos.config import Config
from vyos.utils.process import call, run
from vyos import ConfigError
from vyos import airbag

airbag.enable()


def get_config(config=None):
    if config:
        conf = config
    else:
        conf = Config()
    base = ["service", "tailscale"]
    if not conf.exists(base):
        return None

    return conf.get_config_dict(base, key_mangling=("-", "_"), get_first_key=True)


def verify(tailscale):
    pass


def generate(tailscale):
    pass


def apply(tailscale):
    if tailscale is None or 'disable' in tailscale:
        call('tailscale down')
        return None

    arguments = ["tailscale", "up", "--reset", "--operator=vyos", "--json"]

    if "advertise_route" in tailscale:
        arguments += ["--advertise-routes", ",".join(tailscale["advertise_route"])]
    if "login_server" in tailscale:
        arguments += ["--login-server", tailscale["login_server"]]
    if "auth_key" in tailscale:
        arguments += ["--authkey", tailscale["auth_key"]]
    if "netfilter_mode" in tailscale:
        arguments += ["--netfilter-mode", tailscale["netfilter_mode"]]
    if "exit_node" in tailscale:
        arguments += ["--exit-node", tailscale["exit_node"]]
        if "exit_node_allow_lan_access" in tailscale:
            arguments += ["--exit-node-allow-lan-access=true"]
    if "advertise_exit_node" in tailscale:
        arguments += ["--advertise-exit-node"]
    if "advertise_connector" in tailscale:
        arguments += ["--advertise-connector"]
    if "shields_up" in tailscale:
        arguments += ["--shields-up"]
    if "accept_routes" in tailscale:
        arguments += ["--accept-routes"]
    if "ssh" in tailscale:
        arguments += ["--ssh"]
    if "hostname" in tailscale:
        arguments += ["--hostname", tailscale["hostname"]]

    # Default true handlers
    if "host_routes" not in tailscale:
        arguments += ["--host-routes=false"]
    if "accept_dns" not in tailscale:
        arguments += ["--accept-dns=false"]
    if "manage_netfilter" not in tailscale:
        arguments += ["--netfilter-mode", "off"]
    if "snat_subnet_routes" not in tailscale:
        arguments += ["--snat-subnet-routes=false"]

    # Because tailscale may ask us to login, which will hang forever, set the timeout value
    # this is pretty hacky...
    try:
        run(" ".join(arguments), timeout=6)
    except TimeoutExpired:
        print("Please check tailscale login status with 'tailscale status'")

if __name__ == "__main__":
    try:
        c = get_config()
        verify(c)
        generate(c)
        apply(c)
    except ConfigError as e:
        print(e)
        exit(1)
