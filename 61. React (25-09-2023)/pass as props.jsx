/* Pass State as Props to Child Components

A common pattern is to have a stateful component containing the state important to your app, 
that then renders child components. You want these components to have access to some pieces 
of that state, which are passed in as props.

For example, maybe you have an App component that renders a Navbar, among other components. 
In your App, you have state that contains a lot of user information, but the Navbar only needs 
access to the user's username so it can display it. You pass that piece of state to the Navbar 
component as a prop.

Unidirectional Data Flow > The child components only receive the state data they need. 

complex stateful apps can be broken down into just a few, or maybe a single, stateful component. 
The rest of your components simply receive state from the parent as props, and render a UI from 
that state. 
*/


class MyApp extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        name: "CamperBot"
      };
    }
    render() {
      return (
        <div>
          {/*Here we will call this.state.name in order to pass the value of
          CamperBot to the NavBar component */}
          <Navbar name={this.state.name} />
        </div>
      );
    }
  }
  
  class Navbar extends React.Component {
    constructor(props) {
      super(props);
    }
    render() {
      return (
        <div>
          {/* Since we passed in the CamperBot state value into the the NavBar
          component above the h1 element below will render the value passed
      from state */}
          <h1>Hello, my name is: {this.props.name}</h1>
        </div>
      );
    }
  }



/* Pass a Callback as props 

You can also pass handler functions or any method that's defined 
on a React component to a child component.

This is how you allow child components to interact with their parent components. 
You pass methods to a child just like a regular prop. It's assigned a name and you have access 
to that method name under this.props in the child component.
*/

class MyApp extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        inputValue: ''
      }
      this.handleChange = this.handleChange.bind(this);
    }
    handleChange(event) {
      this.setState({
        inputValue: event.target.value
      });
    }
    render() {
      return (
         <div>
          { /* Change code below this line */ }
          <GetInput input={this.state.inputValue} handleChange={this.handleChange}/>
          <RenderInput input={this.state.inputValue}/>
          { /* Change code above this line */ }
         </div>
      );
    }
  };
  