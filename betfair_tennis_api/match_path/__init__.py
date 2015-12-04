def recursive(root):
    paths = []

    def inner(root, path, depth):
        if 'marketType' in root and root['marketType'] == "MATCH_ODDS":
            paths.append(dict(path))

        path[depth] = root['name']
        if 'children' in root:
            for child in root['children']:
                inner(child, path, depth+1)
                if path:
                    path.pop(depth+1)

    inner(root, {}, 0)
    return paths


def get(tennis_matches):
    paths = recursive(tennis_matches)

    return paths
