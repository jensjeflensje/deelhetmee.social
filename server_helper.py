import config
from importlib import reload
import random
import requests

def get_server():
    reload(config)
    servers = config.SERVERS
    server = servers[random.randint(0, len(servers) - 1)]
    return server

def get_prefixes():
    server = get_server()
    prefixes = requests.get(f"{server['protocol']}://{server['address']}:{server['port']}/prefixes").json()
    return prefixes