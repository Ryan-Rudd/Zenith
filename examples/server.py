import Zenith


app = Zenith.WApp()

homePageContent = """
    <Title>Test Server</Title>
    <Container>
        <Header idName="header">Hello world from Zenith</Header>
        <Button className="test-button">Press Me!</Button>
        <Select>
            <Option>Hello</Option>
        </Select>
        <Input typeAttribute="number"/>
    </Container>
"""
    
builder = Zenith.Builder({"home": homePageContent})
built = builder.Build()

style = Zenith.Stylesheet.new({
    'id.header': {
        'color': 'red',
    },
    'class.test-button': {
        'width': 250,
        'height': 20,
    }
})

style.apply(built, "home")

for route in builder.getRoutes():
    app.register_route(f'{route}', built[route])

# print(style.STYLE_DICTIONARY)

app.serve()