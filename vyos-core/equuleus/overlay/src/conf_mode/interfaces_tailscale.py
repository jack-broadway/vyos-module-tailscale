#!/usr/bin/env python3
from sys import exit

from vyos.config import Config
from vyos.configdict import get_interface_dict
from vyos.ifconfig import TailscaleIf
from vyos import ConfigError
from vyos import airbag
airbag.enable()

def get_config(config=None):
    """
    Retrive CLI config as dictionary. Dictionary can never be empty, as at least the
    interface name will be added or a deleted flag
    """
    if config:
        conf = config
    else:
        conf = Config()
    base = ['interfaces', 'tailscale']
    ifname, tailscale = get_interface_dict(conf, base)
    return tailscale

def verify(tailscale):
    return None

def generate(tailscale):
    return None

def apply(tailscale):
    l = TailscaleIf(**tailscale)
    l.update(tailscale)

    return None

if __name__ == '__main__':
    try:
        c = get_config()
        verify(c)
        generate(c)
        apply(c)
    except ConfigError as e:
        print(e)
        exit(1)