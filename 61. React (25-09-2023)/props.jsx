/*
In React, you can pass props, or properties, to child components. 
Say you have an App component which renders a child component called Welcome which 
is a stateless functional component. You can pass Welcome a user property by writing:
*/

<App>
  <Welcome user='Mark' />
</App>


/*
You use custom HTML attributes created by you and supported by React to be passed to the component. 
In this case, the created property user is passed to the component Welcome. 
Since Welcome is a stateless functional component, it has access to this value like so:                     */

const Welcome = (props) => <h1>Hello, {props.user}!</h1>


/*
It is standard to call this value props and when dealing with stateless functional components, 
you basically consider it as an argument to a function which returns JSX. 
You can access the value of the argument in the function body. With class components, 
this is a little different.
*/


// Example

const CurrentDate = (props) => {
    return (
      <div>

        <p>The current date is: {props.date}</p>
 
      </div>
    );
  };
  
  class Calendar extends React.Component {
    constructor(props) {
      super(props);
    }
    render() {
      return (
        <div>
          <h3>What date is it?</h3>
          
          <CurrentDate date={Date()} />
          
        </div>
      );
    }
  };





/* Pass an Array as Props

The last challenge demonstrated how to pass information from a parent component to a child 
component as props or properties. This challenge looks at how arrays can be passed as props. 
To pass an array to a JSX element, it must be treated as JavaScript and wrapped in curly braces.
*/

<ParentComponent>
  <ChildComponent colors={["green", "blue", "red"]} />
</ParentComponent>

/*
The child component then has access to the array property colors. 
Array methods such as join() can be used when accessing the property.
*/

const ChildComponent = (props) => <p>{props.colors.join(', ')}</p>

// This will join all colors array items into a comma separated string and produce: <p>green, blue, red</p>.


// Example

const List = (props) => {
  
  return <p>{props.tasks.join(", ")}</p>
  
};

class ToDo extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>To Do Lists</h1>
        <h2>Today</h2>
        
        <List tasks={["walk dog", "workout"]} />
        <h2>Tomorrow</h2>
        <List tasks={["walk dog", "workout","have dinner"]} />
        
      </div>
    );
  }
};





/* Use Default Props

React also has an option to set default props. You can assign default props to a 
component as a property on the component itself and React assigns the default prop 
if necessary. This allows you to specify what a prop value should be if no value is explicitly provided.

For example, if you declare MyComponent.defaultProps = { location: 'San Francisco' }, 
you have defined a location prop that's set to the string San Francisco, unless you specify otherwise. 
React assigns default props if props are undefined, but if you pass null as the value for a prop, 
it will remain null.
*/

const ShoppingCart = (props) => {

  return (
    <div>
      <h1>Shopping Cart Component</h1>
    </div>
  )
};

ShoppingCart.defaultProps= {items: 0};




/* Override Default Props

The ShoppingCart component now renders a child component Items. This Items component 
has a default prop quantity set to the integer 0. Override the default prop by passing 
in a value of 10 for quantity.

Note: Remember that the syntax to add a prop to a component looks similar to how 
you add HTML attributes. However, since the value for quantity is an integer, 
it won't go in quotes but it should be wrapped in curly braces. For example, {100}. 
This syntax tells JSX to interpret the value within the braces directly as JavaScript.
*/

const Items = (props) => {
  return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
}

Items.defaultProps = {
  quantity: 0
}

class ShoppingCarto extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    
    return <Items quantity={100} />
    
  }
};


/* Use PropTypes to Define the Props You Expect

For example, your application makes an API call to retrieve data that you expect to be in an array, 
which is then passed to a component as a prop. You can set propTypes on your component to require 
the data to be of type array. This will throw a useful warning when the data is of any other type.

You can define a propTypes property for a component in the same way you defined defaultProps. 
Here's an example to require the type function for a prop called handleClick:
*/

MyComponent.propTypes = { handleClick: PropTypes.func.isRequired }


/*
In the example above, the PropTypes.func part checks that handleClick is a function. 
Adding isRequired tells React that handleClick is a required property for that component. 
You will see a warning if that prop isn't provided. Also notice that func represents function. 
Among the seven JavaScript primitive types, function and boolean (written as bool) are the only 
two that use unusual spelling. In addition to the primitive types, there are other types available. 
For example, you can check that a prop is a React element.
*/

// Example
const Items = (props) => {
  return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
};

Items.propTypes = {quantity: PropTypes.number.isRequired} 
//specifying that quantity is a number type and required

Items.defaultProps = {
  quantity: 0
};

class ShoppingCartoo extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <Items />
  }
};




/* Access Props Using this.props

What if the child component that you're passing a prop to is an ES6 class component, 
rather than a stateless functional component?

Anytime you refer to a class component within itself, you use the this keyword. 
To access props within a class component, you preface the code that you use to access it with this. 
For example, if an ES6 class component has a prop called data, you write {this.props.data} in JSX.
*/

class App extends React.Component {
  constructor(props) {
    super(props);

  }
  render() {
    return (
        <div>
            
            <Welcomee name="Balubba"/>
            
        </div>
    );
  }
};

class Welcomee extends React.Component {
  constructor(props) {
    super(props);

  }
  render() {
    return (
        <div>
          
          <p>Hello, <strong>{this.props.name}</strong>!</p>
          
        </div>
    );
  }
};




/* REVIEW
A stateless functional component is any function you write which accepts props and returns JSX. 
A stateless component, on the other hand, is a class that extends React.Component, but does not 
use internal state (covered in the next challenge). Finally, a stateful component is a class 
component that does maintain its own internal state. You may see stateful components referred to 
simply as components or React components.

A common pattern is to try to minimize statefulness and to create stateless functional components 
wherever possible. This helps contain your state management to a specific area of your application. 
In turn, this improves development and maintenance of your app by making it easier to follow how 
changes to state affect its behavior.



Exercise:
The code editor has a CampSite component that renders a Camper component as a child. 
Define the Camper component and assign it default props of { name: 'CamperBot' }. 
Inside the Camper component, render any code that you want, but make sure to have one p element 
that includes only the name value that is passed in as a prop. Finally, define propTypes on 
the Camper component to require name to be provided as a prop and verify that it is of type string.
*/

class CampSite extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <Camper/>
      </div>
    );
  }
};

const Camper = function(props) {
  
  return <p>{props.name}</p>
};

Camper.defaultProps = {name:'CamperBot'};
Camper.propTypes = {name: PropTypes.string.isRequired}





