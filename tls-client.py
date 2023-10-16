import socket
import ssl
import pprint

HOSTNAME = "www.python.org"
context = ssl.create_default_context()

with socket.create_connection((HOSTNAME, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=HOSTNAME) as ssock:
        print(ssock.version())
        print(ssock.cipher())
        pprint.pprint(ssock.getpeercert())
