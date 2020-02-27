import config
from importlib import reload
import random
import requests

def get_server(servers):
    reload(config)
    server = servers[random.randint(0, len(servers) - 1)]
    return server

def get_online_servers():
    working_servers = []
    for server in config.SERVERS:
        try:
            requests.get(f"{server['protocol']}://{server['address']}:{server['port']}/prefixes").json()
            working_servers.append(server)
        except Exception:
            pass
    return working_servers

def get_prefixes(servers):
    server = get_server(servers)
    prefixes = requests.get(f"{server['protocol']}://{server['address']}:{server['port']}/prefixes").json()
    return prefixes