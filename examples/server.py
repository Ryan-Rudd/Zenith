import Zenith

app = Zenith.WApp()

homePageContent = """
    <Container>
        <Header idName="header">Hello from Zenith</Header>
    </Container>
    """
builder = Zenith.Builder({"home": homePageContent})
built = builder.Build()
print(built )