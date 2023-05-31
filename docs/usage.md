# Zenith Usage

To start building web applications with Zenith, follow these steps:

1. Create a new Python file for your application, e.g., `app.py`.

2. Import the necessary modules:

   ```
   import Zenith
   ```

3. Create a new Zenith application instance:

   ```
   app = Zenith.WApp()
   ```

4. Define your webpage content using Zenith's declarative syntax. For example:

   ```
   homePageContent = '''
       <Container>
           <Header idName="header">Hello world from Zenith</Header>
       </Container>
   '''
   ```

5. Use the Zenith `Builder` class to build the webpage:

   ```
   builder = Zenith.Builder({"home": homePageContent})
   built = builder.Build()
   ```

6. Register the webpage routes with your Zenith application:

   ```
   for route in builder.getRoutes():
       app.register_route(f'/{route}', built[route])
   ```

   You can customize the route URL as per your requirements.

7. Serve the Zenith application:

   ```
   app.serve()
   ```

8. Open your web browser and visit `http://localhost:8000` to see your Zenith application in action.

Congratulations! You have created and served your first Zenith web application.

Now you can explore further and leverage Zenith's features to build interactive and scalable web applications.

