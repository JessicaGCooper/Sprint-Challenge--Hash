import itertools

def finder(files, queries):

    paths = []
    for path in files:
        f = path.split('/')
        paths.append(f[-1])

    check = dict()
    for i in range(len(files)):
        if paths[i] not in check:
            check[paths[i]] = []
        check[paths[i]].append(files[i])

    results = []
    
    for q in queries:
        if q in check:
            results.append(check[q])
    
    result = list(itertools.chain.from_iterable(results))

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/usr/baz',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
