import Zenith

app = Zenith.WApp()

homePageContent = """
    <Title>Test Server</Title>
    <Container>
        <Header idName="header">Hello world from Zenith</Header>
        <Button idName="test-button">Press Me!</Button>
        <Select>
            <Option>Hello</Option>
        </Select>
        <Input typeAttribute="number"/>
    </Container>
"""
    
builder = Zenith.Builder({"home": homePageContent})
built = builder.Build()

for route in builder.getRoutes():
    app.register_route(f'{route}', built[route])
    
app.serve()