/*
Components are the core of React. Everything in React is a component.

There are two ways to create a React component. The first way is to use a JavaScript function. 
Defining a component in this way creates a stateless functional component. 
For now, think of a stateless component as one that can receive data and render it, 
but does not manage or track changes to that data. 
*/


/* Stateless Functional Component

To create a component with a function, you simply write a JavaScript function that 
returns either JSX or null. One important thing to note is that React requires your 
function name to begin with a capital letter. Here's an example of a stateless functional 
component that assigns an HTML class in JSX:               */

const DemoComponent = function() {
    return (
      <div className='customClass' />
    );
  };

/*
After being transpiled, the <div> will have a CSS class of customClass.

Because a JSX component represents HTML, you could put several components together to create 
a more complex HTML page. This is one of the key advantages of the component architecture React provides. 
It allows you to compose your UI from many separate, isolated components. This makes it easier 
to build and maintain complex user interfaces.
*/




/* ES6 React Component

The other way to define a React component is with the ES6 class syntax. 
In the following example, Kitten extends React.Component:                       */

class Kitten extends React.Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (
        <h1>Hi</h1>
      );
    }
  }


/*
This creates an ES6 class Kitten which extends the React.Component class. 
So the Kitten class now has access to many useful React features, such as local state and lifecycle hooks. 
Don't worry if you aren't familiar with these terms yet, they will be covered in greater detail 
in later challenges. Also notice the Kitten class has a constructor defined within it that calls super(). 
It uses super() to call the constructor of the parent class, in this case React.Component. 
The constructor is a special method used during the initialization of objects that are created 
with the class keyword. It is best practice to call a component's constructor with super, and pass 
props to both. This makes sure the component is initialized properly. For now, know that it is 
standard for this code to be included. Soon you will see other uses for the constructor as well as props.
*/




/* Create a Component with Composition

Now we will look at how we can compose multiple React components together. 
Imagine you are building an app and have created three components: a Navbar, Dashboard, and Footer.

To compose these components together, you could create an App parent component which renders 
each of these three components as children. To render a component as a child in a React component, 
you include the component name written as a custom HTML tag in the JSX. For example, 
in the render method you could write:
*/

return (
    <App>
     <Navbar />
     <Dashboard />
     <Footer />
    </App>
   )

/*
When React encounters a custom HTML tag that references another component 
(a component name wrapped in < /> like in this example), 
it renders the markup for that component in the location of the tag. 
This should illustrate the parent/child relationship between the App component and 
the Navbar, Dashboard, and Footer.
*/

const ChildComponent = () => {
    return (
      <div>
        <p>I am the child</p>
      </div>
    );
  };
  
  class ParentComponent extends React.Component {
    constructor(props) {
      super(props);
    }
    render() {
      return (
        <div>
          <h1>I am the parent</h1>
  
          <ChildComponent />

        </div>
      );
    }
  };





/* Nested Components 

The last challenge showed a simple way to compose two components, but there are many different 
ways you can compose components with React.

Component composition is one of React's powerful features. When you work with React, 
it is important to start thinking about your user interface in terms of components like 
the App example in the last challenge. You break down your UI into its basic building blocks, 
and those pieces become the components. This helps to separate the code responsible for the UI 
from the code responsible for handling your application logic. It can greatly simplify 
the development and maintenance of complex projects.
*/

const TypesOfFruit = () => {
    return (
      <div>
        <h2>Fruits:</h2>
        <ul>
          <li>Apples</li>
          <li>Blueberries</li>
          <li>Strawberries</li>
          <li>Bananas</li>
        </ul>
      </div>
    );
  };
  
  const Fruits = () => {
    return (
      <div>

        <TypesOfFruit />

      </div>
    );
  };
  
  class TypesOfFood extends React.Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (
        <div>
          <h1>Types of Food:</h1>

          <Fruits />

        </div>
      );
    }
  };

/* There are two functional components defined in the code editor, called TypesOfFruit and Fruits. 
Take the TypesOfFruit component and compose it, or nest it, within the Fruits component. 
Then take the Fruits component and nest it within the TypesOfFood component. */





/* Render a Class Component to the DOM

None of the React code you write will render to the DOM without making a call to the ReactDOM API.

Here's a refresher on the syntax: ReactDOM.render(componentToRender, targetNode). 
The first argument is the React component that you want to render. The second argument is the 
DOM node that you want to render that component within.

React components are passed into ReactDOM.render() a little differently than JSX elements. 
For JSX elements, you pass in the name of the element that you want to render. However, for React 
components, you need to use the same syntax as if you were rendering a nested component, for example 
ReactDOM.render(<ComponentToRender />, targetNode). You use this syntax for both ES6 class components 
and functional components.
*/


class TypesOfFood extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>Types of Food:</h1>

        <Fruits />
        <Vegetables />

      </div>
    );
  }
};

ReactDOM.render(<TypesOfFood />,document.getElementById('challenge-node'));