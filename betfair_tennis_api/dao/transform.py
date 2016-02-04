def take_root(tennis_node):
    return do_list(tennis_node['children'], [], [])


def do_list(elems, path, matches):
    print path
    for elem in elems:
        path.append(elem['name'])

        if is_match_odds(elem):
            print 'unpopped', path
            matches.append(build_match(elem, path))
            path = []
            break
        elif 'children' in elem:
            do_list(elem['children'], list(path), matches)

    return matches


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
