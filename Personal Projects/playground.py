def retrieve_keys(
    path='/Users/colby/Documents/Lambda/03 Unit 3/twitterapi.keys'
):
    """Retrieves my twitter api keys because .env files won't work"""

    file = open(
        '/Users/colby/Documents/Lambda/03 Unit 3/twitterapi.keys',
        'r'
    )

    data = file.read().split('\n')

    keys = {}

    for x in data:
        y = x.split('=')

        keys[y[0]] = y[1]

    return keys

print(retrieve_keys())