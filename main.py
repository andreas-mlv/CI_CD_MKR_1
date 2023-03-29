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

def count_words(text):
    splitters = [
        ",",
        " ",
        ":",
        ";",
    ]
    splitters_count = 0
    for splitter in splitters:
        splitters_count += text.count(splitter)
    # IF last character is not a splitter, minus 1
    if text[-1] not in splitters:
        splitters_count -= 1
    return splitters_count + 1

