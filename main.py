import os

def get_path(filename=None):
    if filename is None:
        return os.path.dirname(os.path.abspath(__file__))
    else:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

def read_file(filename):
    try:
        with open(get_path(filename), 'r', encoding="utf8") as f:
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

def count_lines(text):
    splitters = [
        ".",
        "!",
        "?",
        "...",
    ]
    splitters_count = 0
    for splitter in splitters:
        splitters_count += text.count(splitter)
    return splitters_count + 1

def calculate(text):
    words_count = count_words(text)
    lines_count = count_lines(text)
    return {
        "words": words_count,
        "lines": lines_count,
    }

def generate_results(results):
    words = results.get("words")
    lines = results.get("lines")
    return f"Words: {words}, Lines: {lines}"

if __name__ == "__main__":
    text = read_file('example_text.txt')
    calculated = calculate(text)
    results = generate_results(calculated)
    print(results)
    
    # Output: 
    # Words: 201, Lines: 10

