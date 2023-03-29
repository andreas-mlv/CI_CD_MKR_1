import pytest
import main

test_text = "Hello, World!"

# Fixtures
@pytest.fixture
def text():
    return test_text

# Parameterized tests
@pytest.mark.parametrize("test_input, expected", [(test_text, 2)])
def test_count_words(test_input, expected):
    assert main.count_words(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(test_text, 2)])
def test_count_lines(test_input, expected):
    assert main.count_lines(test_input) == expected
