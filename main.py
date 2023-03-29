import os

def get_path(filename=None):
    if filename is None:
        return os.path.dirname(os.path.abspath(__file__))
    else:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

def read_file(filename):
    try:
        with open(get_path(filename), 'r') as f:
            return f.read()
    except:
        return None

