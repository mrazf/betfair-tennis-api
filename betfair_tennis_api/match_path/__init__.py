# MESSY

def is_match(elem):
    if 'marketType' in elem and elem['marketType'] == "MATCH_ODDS":
        return True

    return False

def pull_out_matches(elem, path, depth, paths):
    print path
    if 'children' in elem:
        for child in elem['children']:
            if is_match(child):
                path['id'] = elem['id']
                path[depth] = elem['name']

                print 'dicting', dict(path)
                paths.append(dict(path))
                continue

            path[depth] = elem['name']
            pull_out_matches(child, dict(path), depth+1, paths)

    return paths


def get(tennis_matches):
    paths = pull_out_matches(tennis_matches, {}, 0, [])

    return paths
