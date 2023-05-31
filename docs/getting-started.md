# Getting Started with Zenith

Welcome to Zenith! This guide will help you get started with Zenith, a powerful Python framework for web development.

## Installation

To install Zenith, follow these steps:

1. Ensure you have Python 3.8 or higher installed on your system.
2. Open a terminal or command prompt.
3. Run the following command to install Zenith using pip:

   ```
   pip install ZenithLib
   ```

4. Wait for the installation to complete.

Congratulations! You have successfully installed Zenith on your system.

## Usage

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

## Next Steps

- Check out the [Zenith Documentation](/docs) for detailed information on Zenith's features, components, and API reference.
- Explore the example applications provided in the Zenith repository to learn more about building complex web applications.
- Join the Zenith community to ask questions, share your experiences, and get support.

Enjoy building powerful and scalable web applications with Zenith!

