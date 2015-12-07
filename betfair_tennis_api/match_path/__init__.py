def is_match(elem):
    if 'marketType' in elem and elem['marketType'] == "MATCH_ODDS":
        return True

    return False


def pull_out_matches(elem, path, depth, paths):
    if 'children' in elem:
        for child in elem['children']:
            path.append(elem['name'])
            if is_match(child):
                match = {}
                match['id'] = elem['id']
                match['path'] = path

                paths.append(match)
                continue

            pull_out_matches(child, list(path), depth+1, paths)

            if path:
                path.pop()

    return paths


def get(tennis_matches):
    paths = pull_out_matches(tennis_matches, [], 0, [])

    return paths
