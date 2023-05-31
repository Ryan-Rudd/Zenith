import lang.langAST
import lang.langParser
import lang.langTranspiler

class BuilderConstructedObject(object):
    def __init__(self) -> None:
        self.ROUTE_NAME = str
        self.CONTENT = str
    

class Builder():
    def __init__(self, routes) -> None:
        self.routes = routes
        
    def Build(self):
        NEW_BUILDER_BUILT = {}
        for BUILD_ROUTE in self.routes:
            NAME = BUILD_ROUTE
            BUILD_PRE_BUILD_CONTENT = self.routes[BUILD_ROUTE]
            
            tokens = lang.langParser.parse_string(BUILD_PRE_BUILD_CONTENT)
            ast = lang.langAST.build_ast(tokens)
            transpiled = lang.langTranspiler.transpile_to_html(ast)
            
            NEW_BUILDER_BUILT[NAME] = str(transpiled)
            
            return
            
    def getRoutes(self):
        ROUTES = []
        for ROUTE in self.routes:
            ROUTES.append(f"{ROUTE}")
        return ROUTES
    
    
    
homePageContent = """
    <Container>
        <Header idName="header">Hello from Zenith</Header>
    </Container>
    """
    
builder = Builder({"homePage": homePageContent})
builder.Build()

routes = builder.getRoutes()
