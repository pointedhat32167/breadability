from os import path


TEST_DIR = path.dirname(__file__)


def load_snippet(filename):
    """Helper to fetch in the content of a test snippet"""
    return open(path.join(TEST_DIR, 'test_snippets', filename)).read()
