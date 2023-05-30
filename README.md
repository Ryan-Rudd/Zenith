<a href="https://www.buymeacoffee.com/rydev" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

# Zenith
 Zenith is a powerful Python framework that revolutionizes web development by enabling declarative and efficient UI components for building interactive and scalable websites.

# Usage 
## Installation 
```
pip install ZenithLib
```
## Start a server
```python
import Zenith

app = Zenith.WApp()

app.serve()
```

## Creating a basic webpage
```python

import Zenith

app = Zenith.WApp()

builder = Builder({"HomePage": """
    <Container>
        <Header idName="header">Hello from Zenith</Header>
    </Container>
"""})

stylesheet = Stylesheet(builder, "HomePage", {
    "id.header": 
    {
        "foreColor": "#000",
        "fontSize": 22
    }
})

app.render(Builder)
app.serve()
```
