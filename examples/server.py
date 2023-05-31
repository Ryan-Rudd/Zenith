import Zenith


app = Zenith.WApp()

homePageContent = """
    <Container idName="container" className="loading-container">
        <div className="loader"></div>
    </Container>
"""

    
builder = Zenith.Builder({"home": homePageContent})
built = builder.Build()

style = Zenith.Stylesheet.new({
    'id.container': {
        'display': 'flex',
        'justify-content': 'center',
        'align-items': 'center',
        'height': '100vh',
    },
    '.loading-container': {
        'background-color': '#f8f9fa',
    },
    '.loader': {
        'border': '16px solid #f3f3f3',
        'border-top': '16px solid #007BFF',
        'border-radius': '50%',
        'width': '120px',
        'height': '120px',
        'animation': 'spin 2s linear infinite',
    },
    '@keyframes spin': {
        '0%': {
            'transform': 'rotate(0deg)',
        },
        '100%': {
            'transform': 'rotate(360deg)',
        },
    },
})

style.apply(built, "home")

for route in builder.getRoutes():
    app.register_route(f'{route}', built[route])

app.serve()
