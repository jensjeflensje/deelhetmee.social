import config
from importlib import reload
import random
import requests

def get_server(servers):
    server = servers[random.randint(0, len(servers) - 1)]
    return server

def get_online_servers():
    working_servers = []
    reload(config)
    for server in config.SERVERS:
        try:
            r = requests.get(f"{server['protocol']}://{server['address']}:{server['port']}/prefixes")
            print(r)
            working_servers.append(server)
        except Exception as e:
            print(str(e))
    return working_servers

def get_prefixes(servers):
    server = get_server(servers)
    prefixes = requests.get(f"{server['protocol']}://{server['address']}:{server['port']}/prefixes").json()
    return prefixes