import Zenith


app = Zenith.WApp()

homePageContent = """
    <Container>
        <Header idName="header">Welcome to Zenith</Header>
        
        <Image srcUrl="path/to/image.jpg" altText="Zenith Logo" className="logo-image" />
        
        <Paragraph className="intro-paragraph">
            Zenith is a powerful and flexible web framework that empowers developers to create modern and dynamic web applications with ease.
        </Paragraph>
        
        <Button className="primary-button">Get Started</Button>
        
        <Footer className="footer">
            <Paragraph className="footer-text">
               &#169; 2023 Zenith Framework. All rights reserved.
            </Paragraph>
        </Footer>
    </Container>
"""

    
builder = Zenith.Builder({"home": homePageContent})
built = builder.Build()

style = Zenith.Stylesheet.new({

    'id.header': {
        'color': '#333',
        'font-size': '28px',
        'text-align': 'center',
        'margin-top': '40px',
        'text-shadow': '2px 2px 4px rgba(0, 0, 0, 0.3)',
    },
    'class.logo-image': {
        'width': '200px',
        'height': 'auto',
        'margin-top': '40px',
        'box-shadow': '0px 2px 4px rgba(0, 0, 0, 0.2)',
        'transition': 'transform 0.3s ease-in-out',
    },
    'class.logo-image:hover': {
        'transform': 'rotate(5deg) scale(1.05)',
    },
    'class.intro-paragraph': {
        'font-size': '18px',
        'color': '#555',
        'margin-bottom': '30px',
        'text-align': 'center',
        'line-height': '1.5',
    },
    'class.primary-button': {
        'background-color': '#007BFF',
        'color': 'white',
        'padding': '12px 24px',
        'border-radius': '6px',
        'text-transform': 'uppercase',
        'font-weight': 'bold',
        'cursor': 'pointer',
        'box-shadow': '2px 2px 4px rgba(0, 0, 0, 0.2)',
        'transition': 'background-color 0.3s ease-in-out, transform 0.3s ease-in-out',
    },
    'class.primary-button:hover': {
        'background-color': '#0056b3',
        'transform': 'scale(1.05)',
    },
    'class.footer': {
        'background-color': '#f8f9fa',
        'padding': '20px',
        'text-align': 'center',
        'font-size': '14px',
    },
    'class.footer-text': {
        'color': '#888',
        'margin': '0',
    },
})


style.apply(built, "home")

for route in builder.getRoutes():
    app.register_route(f'{route}', built[route])

# print(style.STYLE_DICTIONARY)

app.serve()