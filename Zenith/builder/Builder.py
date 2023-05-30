class BuilderConstructedObject(object):
    def __init__(self) -> None:
        self.ROUTE_NAME = str
        self.CONTENT = str
    

class Builder():
    def __init__(self, routes) -> None:
        self.routes = routes
    
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
    
builder = Builder({"homePage": homePageContent, "loginPage": homePageContent})
routes = builder.getRoutes()
print(routes)