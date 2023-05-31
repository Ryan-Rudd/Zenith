from .lang import langParser
from .lang import langAST
from .lang import langTranspiler

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
            
            tokens = langParser.parse_string(BUILD_PRE_BUILD_CONTENT)
            ast = langAST.build_ast(tokens)
            transpiled = langTranspiler.transpile_to_html(ast)
            
            print(transpiled)
            NEW_BUILDER_BUILT[NAME] = f"""{transpiled}"""
            
            return NEW_BUILDER_BUILT
            
    def getRoutes(self):
        ROUTES = []
        for ROUTE in self.routes:
            ROUTES.append(f"{ROUTE}")
        return ROUTES
    
    
