def take_root(tennis_node):
    return do(tennis_node, tennis_node['children'], [], [])


def do(elem, children, path, matches):
    path.append(elem['name'])

    for child in children:
        if is_match_odds(child):
            matches.append(build_match(elem, path))
        elif 'children' in child:
            do(child, child['children'], list(path), matches)

    return matches


def build_match(raw_match, path):
    return dict([('id', raw_match['id']), ('path', path)])


def is_match_odds(elem):
    if 'marketType' in elem and elem['marketType'] == "MATCH_ODDS":
        return True

    return False
