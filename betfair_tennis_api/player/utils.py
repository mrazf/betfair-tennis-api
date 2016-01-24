from flask import request
from urllib import quote
from urlparse import urlparse


def build_player_url(player_id):
    safe_player_id = quote(player_id.encode('utf8'))
    url = build_host_and_port() + "/api/player/" + safe_player_id

    return url


def build_host_and_port():
    parsed_url = urlparse(request.url_root)
    base_url = parsed_url.hostname

    if parsed_url.port is not None:
        port = ":" + str(parsed_url.port)
    else:
        port = ""

    return "http://" + base_url + port
