import re

class ParserTokens:
    BRACKET_OPEN = "<"
    BRACKET_CLOSE = ">"
    BRACKET_END = "/"
    EQUALS = "="
    QUOTATION = "\""
    
    
def parse_string(input_string):
    pattern = re.compile(
        fr"\s*({re.escape(ParserTokens.BRACKET_OPEN)}"
        fr"|{re.escape(ParserTokens.BRACKET_CLOSE)}"
        fr"|{re.escape(ParserTokens.BRACKET_END)}"
        fr"|{re.escape(ParserTokens.EQUALS)}"
        fr"|{re.escape(ParserTokens.QUOTATION)})"
    )

    tokens = pattern.split(input_string)
    tokens = [token.strip() for token in tokens if token.strip()]  # Remove empty and whitespace-only tokens

    return tokens

print(parse_string("""
    <Container>
        <Header idName="header">Hello from Zenith</Header>
    </Container>
    """))