from mitmproxy.tools.main import mitmdump
import os

username = os.getenv("DEFAULT_PROXY_USERNAME")
password = os.getenv("DEFAULT_PROXY_PASSWORD")
server = os.getenv("DEFAULT_PROXY_SERVER", 'brd.superproxy.io')
port = os.getenv("DEFAULT_PROXY_PORT", 22225)


mitmdump(args=[
    "-s", "./mitm/addon/proxy_controller.py",
    "--mode", f"upstream:http://{server}:{port}",
    "--upstream-auth", f"{username}:{password}",
    "--set stream_large_bodies=5g",
    "--set connection_strategy=lazy"
    "--set upstream_cert=false",
    "--ssl-insecure"
])

"""
--set connection_strategy=lazy

Determine when server connections should be established. 
When set to lazy, mitmproxy tries to defer establishing an upstream connection as long as possible. 
This makes it possible to use server replay while being offline. 
When set to eager, mitmproxy can detect protocols with server-side greetings, as well as accurately mirror TLS ALPN negotiation.
Default: eager
Choices: eager, lazy
"""

"""
--set stream_large_bodies=5g

Stream data to the client if response body exceeds the given threshold. 
If streamed, the body will not be stored in any way, and such responses cannot be modified. 
Understands k/m/g suffixes, i.e. 3m for 3 megabytes.
Default: None
"""