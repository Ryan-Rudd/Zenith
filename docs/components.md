# Zenith Components ( COMING SOON )

Components are a fundamental building block in Zenith for creating UI elements. They allow you to encapsulate and reuse UI logic and markup across your web application.

## Creating a Component

To create a component in Zenith, follow these steps:

1. Define a Python class that inherits from the `Zenith.Component` class:

   ```
   class MyComponent(Zenith.Component):
       def render(self):
           return '''
               <div>
                   <h1>Welcome to MyComponent</h1>
                   <p>This is a custom Zenith component.</p>
               </div>
           '''
   ```

2. Implement the `render` method of the component. This method should return the HTML markup that represents the component.

3. Instantiate the component and use it in your application:

   ```
   myComponent = MyComponent()
   ```

4. Include the component in your webpage content or other components:

   ```
   homePageContent = '''
       <Container>
           <Header idName="header">Hello world from Zenith</Header>
           {myComponent.render()}
       </Container>
   '''
   ```

   In this example, the component is included by calling its `render` method within the webpage content.

## Component Lifecycle

Zenith components have a lifecycle that consists of several phases, including creation, rendering, and updating. By overriding specific methods in your component class, you can tap into these lifecycle phases and perform custom logic.

The following methods are available to override in a component:

- `__init__`: Called when the component is initialized.
- `on_mount`: Called when the component is first rendered.
- `on_update`: Called when the component is updated.
- `on_unmount`: Called when the component is removed from the DOM.

By implementing these methods, you can control the behavior of your component throughout its lifecycle.

## Component Composition

Zenith allows you to compose components together to build complex user interfaces. You can include one component within another by calling its `render` method within the parent component's render method or in the webpage content.

For example:

```
class ParentComponent(Zenith.Component):
def render(self):
childComponent = ChildComponent()
return f"""
    <div>
        <h1>Welcome to ParentComponent</h1>
        {childComponent.render()}
    </div>"""
```

In this example, the `ChildComponent` is included within the `ParentComponent` by calling its `render` method within the parent component's `render` method.

## Conclusion

Components are a powerful feature of Zenith that enable you to build reusable and scalable UI elements. By encapsulating UI logic and markup within components, you can create modular and maintainable web applications.

Explore further to learn about advanced component features such as state management, event handling, and data binding in the Zenith documentation.

