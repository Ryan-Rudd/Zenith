import Zenith

app = Zenith.WApp()

homePageContent = """
    <Container>
        <Header idName="header">Hello world from Zenith</Header>
    </Container>
    """
    
builder = Zenith.Builder({"home": homePageContent})
built = builder.Build()
print(built)
for route in builder.getRoutes():
    app.register_route(f'{route}', built[route])
    
app.serve()