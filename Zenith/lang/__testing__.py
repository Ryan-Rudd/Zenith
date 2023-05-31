import langAST
import langParser

tokens = langParser.parse_string("""
    <Container>
        <Header idName="header">Hello from Zenith</Header>
        <Block idName="block-title>
            <Button idName="button" onPress="doFunction()">Press me!</Button>
        </Block>
    </Container>
    """)

ast = langAST.build_ast(tokens)
langAST.print_ast(ast)
