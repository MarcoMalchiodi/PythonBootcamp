/* 
Controlled Input

Form control elements for text input, such as input and textarea, maintain their own state in 
the DOM as the user types. With React, you can move this mutable state into a React component's state. 
The user's input becomes part of the application state, so React controls the value of that input field.
*/

class ControlledInput extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        input: ''
      };
  
      this.handleChange = this.handleChange.bind(this);
  
    }
  
    handleChange(event) {
      this.setState({
        input: event.target.value
      });
    }
  
    render() {
      return (
        <div>
          
          <input value={this.state.input} onChange = {this.handleChange}></input>
          
          <h4>Controlled Input:</h4>
          <p>{this.state.input}</p>
        </div>
      );
    }
  };
// the text appears as it is written


// This applies to other form elements as well, including the regular HTML form element.

class MyForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: '',
      submit: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  handleChange(event) {
    this.setState({
      input: event.target.value
    });
  }
  handleSubmit(event) {
    event.preventDefault()
    this.setState({
      submit: this.state.input
    });
  }
  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input
            value={this.state.input}
            onChange={this.handleChange} />
          <button type='submit'>Submit!</button>
        </form>
        <h1>{this.state.submit}</h1>
      </div>
    );
  }
};