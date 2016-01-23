from flask import request
from urllib import quote
from urlparse import urlparse



def build_player_url(player_id):
    parsed_url = urlparse(request.url_root)

    base_url = parsed_url.hostname
    port = str(parsed_url.port)
    safe_player_id = quote(player_id.encode('utf8'))
    url = "http://" + base_url + ":" + port + "/api/player/" + safe_player_id

    return url
