/* Stateful Component

State consists of any data your application needs to know about, that can change over time. 
You want your apps to respond to state changes and present an updated UI when necessary. 

You create state in a React component by declaring a state property on the component class in its constructor. 
This initializes the component with state when it is created. The state property must be set 
to a JavaScript object. Declaring it looks like this:
*/

this.state = {

}

/*
You have access to the state object throughout the life of your component. 
You can update it, render it in your UI, and pass it as props to child components. 
The state object can be as complex or as simple as you need it to be. Note that you must 
create a class component by extending React.Component in order to create state like this.
*/

class StatefulComponent extends React.Component {
  constructor(props) {
    super(props);

  this.state = {
    firstName:'My name',
  }

  }
  render() {
    return (
      <div>
        <h1>{this.state.firstName}</h1>
      </div>
    );
  }
};


/*
Once you define a component's initial state, you can display any part of it in the UI that is rendered. 
If a component is stateful, it will always have access to the data in state in its render() method. 
You can access the data with this.state.

state allows you to track important data in your app and render a UI in response to changes in this data. 
If your data changes, your UI will change. React uses what is called a virtual DOM, to keep track of 
changes behind the scenes. When state data updates, it triggers a re-render of the components using 
that data - including child components that received the data as a prop. React updates the actual DOM, 
but only where necessary. This means you don't have to worry about changing the DOM. 
You simply declare what the UI should look like.
*/

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'freeCodeCamp'
    }
  }
  render() {
    return (
      <div>

        <h1>{this.state.name}</h1>

      </div>
    );
  }
};



/*
There is another way to access state in a component. In the render() method, before the return 
statement, you can write JavaScript directly. 

For example, you could declare functions, access data from state or props, 
perform computations on this data, and so on. Then, you can assign any data to variables, 
which you have access to in the return statement.
*/

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'freeCodeCamp'
    }
  }
  render() {

    const name = this.state.name; // JS syntax doesn't require {}

    return (
      <div>

        <h1>{name}</h1>

      </div>
    );
  }
};



/* Set State with this.setState

React provides a method for updating component state called setState. 
You call the setState method within your component class like so: this.setState(), 
passing in an object with key-value pairs. 
The keys are your state properties and the values are the updated state data. 
For instance, if we were storing a username in state and wanted to update it, it would look like this:
*/

this.setState({
  username: 'Lewis'
});


/* React expects you to never modify state directly, 
instead always use this.setState() when state changes occur. */


class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'Initial State'
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {

    this.setState(this.state = { name: 'React Rocks!'})

  }
  render() {
    return (
      <div>
        <button onClick={this.handleClick}>Click Me</button>
        <h1>{this.state.name}</h1>
      </div>
    );
  }
};



/* Bind 'this' to a Class Method

In addition to setting and updating state, you can also define methods for your component class. 
A class method typically needs to use the this keyword so it can access properties on the 
class (such as state and props) inside the scope of the method.

One common way is to explicitly bind this in the constructor so this becomes bound to the 
class methods when the component is initialized. {ex. this.handleClick = this.handleClick.bind(this)}
Then, when you call a function like this.setState() within your class method, 
this refers to the class and will not be undefined.
*/

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      text: "Hello"
    };
    // binding this to handleClick
    this.handleClick = this.handleClick.bind(this);
    
  }
  handleClick() {
    this.setState({
      text: "You clicked!"
    });
  }
  render() {
    return (
      <div>
        { /* adding click handler to button */ }
        <button onClick = {this.handleClick}>Click Me</button>

        <h1>{this.state.text}</h1>
      </div>
    );
  }
};



/*
Sometimes you might need to know the previous state when updating the state. 
However, state updates may be asynchronous - this means React may batch multiple setState() 
calls into a single update. This means you can't rely on the previous value of this.state 
or this.props when calculating the next value. So, you should not use code like this:
*/

this.setState({
  counter: this.state.counter + this.props.increment
});

/*
Instead, you should pass setState a function that allows you to access state and props. 
Using a function with setState guarantees you are working with the most current 
values of state and props. This means that the above should be rewritten as:
*/

this.setState((state, props) => ({
  counter: state.counter + props.increment
}));

// You can also use a form without props if you need only the state:

this.setState(state => ({
  counter: state.counter + 1
}));


// Example

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      visibility: false
    };

    this.toggleVisibility = this.toggleVisibility.bind(this);

  }

  toggleVisibility() {
    this.setState(state => {
      if (state.visibility === true) {
         return { visibility: false };
       } else {
         return { visibility: true };
      }
    });
  }

  render() {
    if (this.state.visibility) {
      return (
        <div>
          <button onClick={this.toggleVisibility}>Click Me</button>
          <h1>Now you see me!</h1>
        </div>
      );
    } else {
      return (
        <div>
          <button onClick={this.toggleVisibility}>Click Me</button>
        </div>
      );
    }
  }
}


// Example 2

class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };

    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
    this.reset = this.reset.bind(this);

  }

  increment() {
    this.setState(state => ({
      count: state.count +1
    }));
  }

  decrement() {
    this.setState(state => ({
      count: state.count -1
    }));
  }

  reset() {
    this.setState(state => ({
      count: 0
    }));
  }
 
  render() {
    return (
      <div>
        <button className='inc' onClick={this.increment}>Increment!</button>
        <button className='dec' onClick={this.decrement}>Decrement!</button>
        <button className='reset' onClick={this.reset}>Reset</button>
        <h1>Current Count: {this.state.count}</h1>
      </div>
    );
  }
};