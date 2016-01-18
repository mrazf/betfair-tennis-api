from urllib import quote


def build_player_url(player_id):
    safe_player_id = quote(player_id.encode('utf8'))
    url = "http://localhost:5000/api/player/" + safe_player_id

    return url
