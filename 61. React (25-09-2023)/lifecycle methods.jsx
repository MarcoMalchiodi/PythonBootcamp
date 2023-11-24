/* 
React components have several special methods that provide opportunities to perform actions 
at specific points in the lifecycle of a component. These are called lifecycle methods.
Thhey allow you to catch components at certain points in time. This can be before they are rendered, 
before they update, before they receive props etc.

Here is a list of some of the main lifecycle methods: 

componentWillMount() 
componentDidMount() 
shouldComponentUpdate() 
componentDidUpdate() 
componentWillUnmount()
*/



/* componentWillMount

The componentWillMount() method is called before the render() method when a component is being 
mounted to the DOM. 
*/

class MyComponent extends React.Component {
    constructor(props) {
      super(props);
    }
    componentWillMount() {
      // Change code below this line
      console.log('Heyo')
      // Change code above this line
    }
    render() {
      return <div />
    }
  };




/* componentDidMount

Most web developers, at some point, need to call an API endpoint to retrieve data. 
If you're working with React, it's important to know where to perform this action.

The best practice with React is to place API calls or any calls to your server in the 
lifecycle method componentDidMount(). 

This method is called after a component is mounted to the DOM. Any calls to setState() 
here will trigger a re-rendering of your component. When you call an API in this method, 
and set your state with the data that the API returns, it will automatically trigger an 
update once you receive the data.
*/

// In the render method, render the value of activeUsers in the h1 after the text Active Users:

class MyComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        activeUsers: null
      };
    }
    componentDidMount() {
      setTimeout(() => {
        this.setState({
          activeUsers: 1273
        });
      }, 2500);
    }
    render() {
      return (
        <div>
          {/* Change code below this line */}
          <h1>Active Users: {this.state.activeUsers}</h1>
          {/* Change code above this line */}
        </div>
      );
    }
  }



/* Add Event Listeners

The componentDidMount() method is also the best place to attach any event listeners you 
need to add for specific functionality. 

React provides a synthetic event system which behaves the same regardless of the user's browser.
You've already been using some of these synthetic event handlers such as onClick().
*/

class MyComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        message: ''
      };
      this.handleEnter = this.handleEnter.bind(this);
      this.handleKeyPress = this.handleKeyPress.bind(this);
    }
    // Change code below this line
    componentDidMount() {
      document.addEventListener("keydown",this.handleKeyPress);
    }
    componentWillUnmount() {
      document.removeEventListener("keydown",this.handleKeyPress);
    }
    // Change code above this line
    handleEnter() {
      this.setState((state) => ({
        message: state.message + 'You pressed the enter key! '
      }));
    }
    handleKeyPress(event) {
      if (event.keyCode === 13) {
        this.handleEnter();
      }
    }
    render() {
      return (
        <div>
          <h1>{this.state.message}</h1>
        </div>
      );
    }
  };




/* Optimize Re-Renders with shouldComponentUpdate

React provides a lifecycle method you can call when child components receive new state or props, 
and declare specifically if the components should update or not. The method is shouldComponentUpdate(), 
and it takes nextProps and nextState as parameters.

the default behavior is that your component re-renders when it receives new props, 
even if the props haven't changed. You can use shouldComponentUpdate() to prevent this by 
comparing the props. The method must return a boolean value that tells React whether or not 
to update the component. You can compare the current props (this.props) to the next props (nextProps) 
to determine if you need to update or not, and return true or false accordingly.
*/


class OnlyEvens extends React.Component {
  constructor(props) {
    super(props);
  }
  shouldComponentUpdate(nextProps, nextState) {
    console.log('Should I update?');
    // Change code below this line
    if (nextProps.value % 2 == 0) {
        return true;
      }
      return false;
    // Change code above this line
  }
  componentDidUpdate() {
    console.log('Component re-rendered.');
  }
  render() {
    return <h1>{this.props.value}</h1>;
  }
}

class Controller extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 0
    };
    this.addValue = this.addValue.bind(this);
  }
  addValue() {
    this.setState(state => ({
      value: state.value + 1
    }));
  }
  render() {
    return (
      <div>
        <button onClick={this.addValue}>Add</button>
        <OnlyEvens value={this.state.value} />
      </div>
    );
  }
}

