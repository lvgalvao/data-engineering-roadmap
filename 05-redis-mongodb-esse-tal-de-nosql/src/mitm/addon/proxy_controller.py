import logging
import base64

from os import environ as env
from uuid import uuid4

from mitmproxy import ctx, http
from mitmproxy.connection import Server
from mitmproxy.http import HTTPFlow
from mitmproxy.utils import strutils
from mitmproxy.net.server_spec import ServerSpec
# from mitmproxy.proxy.layers.http import HTTPMode

LOGGING_LEVEL = env.get("LOGGING_LEVEL", "INFO").upper()
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)

class ProxyControllerAddon:
    def responseheaders(self, flow: HTTPFlow):
        """
        Enables streaming for all responses.
        This method sets `stream` attribute to True in the response, 
        allowing streaming large responses.

        Equivalent to passing `--set stream_large_bodies=1` to mitmproxy.
        """
        flow.response.stream = True

    def request(self, flow: HTTPFlow):
        self.set_proxy_configs(flow)
    
    
    def response(self, flow: HTTPFlow):
        pass

    def set_proxy_configs(self, flow: HTTPFlow):
        if self.has_new_proxy_auth(flow):
                flow.request.headers["Proxy-Authorization"] = self.has_new_proxy_auth(flow)
        if self.has_new_proxy_server(flow):
            address = self.has_new_proxy_server(flow)
            logger.info(f"UPSTREAM_PROXY_ENDPOINT: {address}")
            is_proxy_change = address != flow.server_conn.address
            if is_proxy_change:
                flow.server_conn = Server(address=address)
                if flow.request.headers["x-New-Proxy-Server"] != "No-Proxy":
                    flow.server_conn.via = ServerSpec(("http", address))            

    def has_new_proxy_auth(self, flow: HTTPFlow):
        """
        Checks if the request contains the x-New-Proxy-Auth header.
        If found, retrieves the parameter and encodes it in base64, 
        then concatenates the string "Basic" with the encoded value.
        The parameter should be in the format {username}:{password}.
        """
        if "x-New-Proxy-Auth" in flow.request.headers:
            user, password = flow.request.headers["x-New-Proxy-Auth"].split(":")
            session = 15054
            new_auth = f'{user}-session-{session}-c_tag-{session}:{password}'
            return "Basic " + base64.b64encode(strutils.always_bytes(new_auth)).decode("utf-8")
        return None

    def has_new_proxy_server(self, flow: HTTPFlow):
        """
        Checks if the request contains the x-New-Proxy-Server header.
        If found, retrieves the parameter in the format {host}:{port}.
        The parameter could be an IP address or hostname.
        Returns a tuple containing the host (string) and port (integer).
        """
        if "x-New-Proxy-Server" in flow.request.headers:
            if flow.request.headers["x-New-Proxy-Server"] == "No-Proxy":
                return {"localhost", 80}
            else:
                proxy_server = flow.request.headers["x-New-Proxy-Server"]
                host,port = proxy_server.split(":")
                return (host, int(port))
        return 
  
addons = [ProxyControllerAddon()]