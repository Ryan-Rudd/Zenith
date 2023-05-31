import langAST
import langParser
import langTranspiler

# input_string = """
# <Container>
#     <Header idName="header">Hello from Zenith</Header>
#     <Block idName="block-title">
#         <Button idName="button" onPress="doFunction()">Press me!</Button>
#     </Block>
# </Container>
# """
# 
# tokens = langParser.parse_string(input_string)
# ast = langAST.build_ast(tokens)
# # langAST.print_ast(ast)
# 
# html_code = langTranspiler.transpile_to_html(ast)
# print(html_code)
