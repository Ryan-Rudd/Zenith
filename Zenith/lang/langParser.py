import re

def parse_string(input_string):
    # Tokenize open tags, close tags, and text content
    pattern = re.compile(r"(<[^>]*>)|([^<]+)")
    tokens = pattern.findall(input_string)
    # Flatten list of tuples and remove whitespace-only tokens
    tokens = [token for sub in tokens for token in sub if token.strip()]
    return tokens

