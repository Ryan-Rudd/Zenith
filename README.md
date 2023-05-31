# Zenith
![Python Version](https://img.shields.io/badge/Python-3.8-brightgreen.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Zenith is a powerful Python framework that revolutionizes web development. It provides a declarative approach to designing efficient UI components, making it easier than ever to build interactive and scalable websites.

![Zenith Usage](./docs/zenith_usage.png)

## Features

- **Efficient UI components**: Zenith makes it easy to build and manage reusable UI components.
- **Scalable**: Designed with large-scale applications in mind, Zenith helps you build websites that can grow with your needs.
- **Declarative**: Zenith's declarative style makes your code easier to understand and maintain.

## Getting Started

### Installation

To install Zenith, simply run:

```shell
pip install ZenithLib
```

# Basic Usage 

Here's a basic example of how to use Zenith to create a webpage:

```python
import Zenith

app = Zenith.WApp()

homePageContent = """
    <Container>
        <Header idName="header">Hello world from Zenith</Header>
    </Container>
"""

builder = Zenith.Builder({"home": homePageContent})
built = builder.Build()

for route in builder.getRoutes():
    app.register_route(f'{route}', built[route])

app.serve()
```

# Documentation

For more detailed information on using Zenith, please refer to our [documentation](/docs).

# Contributing 
We welcome contributions of all kinds. Check out our [contributing guide](./CONTRIBUTING.md) for more details on how you can help improve Zenith.

# License 

Zenith is released under the MIT License. See [LICENSE](./LICENSE) for details.

# Connect With Us
Have questions or suggestions? Please [open an issue on GitHub](https://github.com/Ryan-Rudd/Zenith/issues) or [send us a pull request](https://github.com/Ryan-Rudd/Zenith/pulls).