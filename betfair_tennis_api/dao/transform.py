def process_root(tennis_node):
    return process(tennis_node['children'], [], [])


def process(elems, path, matches):
    for elem in elems:
        path.append(elem['name'])

        if is_event(elem) and has_match_odds(elem['children']):
            matches.append(build_match(elem, list(path)))
            path.pop()
            continue
        elif 'children' in elem:
            process(elem['children'], list(path), matches)

        path.pop()

    return matches


def build_match(raw_match, path):
    return dict([('id', raw_match['id']), ('path', path)])


def has_match_odds(children):
    if children:
        for child in children:
            if 'marketType' in child and child['marketType'] == "MATCH_ODDS":
                return True

    return False


def is_event(elem):
    if 'type' in elem and elem['type'] == 'EVENT':
        return True

    return False
