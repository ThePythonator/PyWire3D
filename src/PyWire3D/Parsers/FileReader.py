import inspect, os

def stack_search_and_read(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            return f.readlines()

    for directory in [os.path.dirname(s[1]) for s in inspect.stack()]:
        path = os.path.join(directory, filename)

        if os.path.isfile(path):
            with open(path, 'r') as f:
                return f.readlines()

    return None