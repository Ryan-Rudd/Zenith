# API Reference

This document provides a detailed reference for the Zenith API. 

## Zenith.WApp

The `Zenith.WApp` class is used to create a Zenith application.

Example:

```python
app = Zenith.WApp()
```

### Methods

- `serve()`: Starts the Zenith server.

Example:

```python
app.serve()
```

## Zenith.Builder

The `Zenith.Builder` class is used to create Zenith components.

Example:

```python
builder = Zenith.Builder({"home": homePageContent})
```

### Methods

- `Build()`: Builds the Zenith components.

Example:

```python
built = builder.Build()
```

- `getRoutes()`: Returns the routes from the built components.

Example:

```python
for route in builder.getRoutes():
    app.register_route(f'{route}', built[route])
```

## Stylesheet

The `Stylesheet` class is used to style Zenith components.

Example:

```python
stylesheet = Stylesheet(builder, "HomePage", {
    "id.header": 
    {
        "foreColor": "#000",
        "fontSize": 22
    }
})
```

## Conclusion

This is a brief overview of the Zenith API. For more detailed information, please refer to the [official Zenith documentation](LINK_TO_DOCUMENTATION).
