# Routing in Zenith

Routing is an essential part of web applications, and Zenith provides a powerful routing system to handle different URLs and route them to the appropriate components or handlers.

## Configuring Routes

To configure routes in Zenith, follow these steps:

1. Create a new instance of the Zenith `Builder` class:

   """
   builder = Zenith.Builder()
   """

2. Define your routes using the `add_route` method of the builder instance:

   """
   builder.add_route("/", homeComponent)
   builder.add_route("/about", aboutComponent)
   """

   In this example, the root URL ("/") is mapped to the `homeComponent`, and the "/about" URL is mapped to the `aboutComponent`.

3. Build the routes using the `Build` method:

   """
   builtRoutes = builder.Build()
   """

   The `Build` method returns a dictionary that maps route URLs to their corresponding components.

4. Register the built routes with your Zenith application:

   """
   app = Zenith.WApp()

   for route, component in builtRoutes.items():
       app.register_route(route, component)
   """

   This step ensures that the defined routes are registered with your Zenith application.


# COMING SOON

## Dynamic Routing


Zenith supports dynamic routing, allowing you to define routes with parameters that can be accessed within your components or handlers. To define a dynamic route, use curly braces `{}` to wrap the parameter name in the route URL.

For example:

```
builder.add_route("/user/{id}", userComponent)
```


In this example, the route "/user/{id}" defines a dynamic parameter named "id". This parameter can be accessed within the `userComponent` to retrieve the specific user ID.

## Route Parameters

To access route parameters within your component or handler, use the `get_param` method of the Zenith application instance:

```
@app.route("/user/{id}")
def user_handler(request):
userId = request.get_param("id")
# Use the userId to retrieve user information or perform other logic
...
```

