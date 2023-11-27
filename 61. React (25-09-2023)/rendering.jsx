/*
You can also write JavaScript directly in your render methods, before the return statement, 
without inserting it inside of curly braces.
When you want to use a variable later in the JSX code inside the return statement, 
you place the variable name inside curly braces.
*/

const inputStyle = {
    width: 235,
    margin: 5
  };
  
  class MagicEightBall extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        userInput: '',
        randomIndex: ''
      };
      this.ask = this.ask.bind(this);
      this.handleChange = this.handleChange.bind(this);
    }
    ask() {
      if (this.state.userInput) {
        this.setState({
          randomIndex: Math.floor(Math.random() * 20),
          userInput: ''
        });
      }
    }
    handleChange(event) {
      this.setState({
        userInput: event.target.value
      });
    }
    render() {
      const possibleAnswers = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes, definitely',
        'You may rely on it',
        'As I see it, yes',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        "Don't count on it",
        'My reply is no',
        'My sources say no',
        'Most likely',
        'Outlook not so good',
        'Very doubtful'
      ];
      const answer = possibleAnswers[this.state.randomIndex]; // Change this line
      return (
        <div>
          <input
            type='text'
            value={this.state.userInput}
            onChange={this.handleChange}
            style={inputStyle}
          />
          <br />
          <button onClick={this.ask}>Ask the Magic Eight Ball!</button>
          <br />
          <h3>Answer:</h3>
          <p>
            {/* Change code below this line */}
            {answer}
            {/* Change code above this line */}
          </p>
        </div>
      );
    }
  }



/* Render with an If-Else Condition

Another application of using JavaScript to control your rendered view is to tie the elements that 
are rendered to a condition. When the condition is true, one view renders. When it's false, 
it's a different view. You can do this with a standard if/else statement in the render() method 
of a React component.
*/

class MyComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        display: true
      }
      this.toggleDisplay = this.toggleDisplay.bind(this);
    }
    toggleDisplay() {
      this.setState((state) => ({
        display: !state.display
      }));
    }
    render() {
      // Change code below this line
      if (this.state.display == true) {
      return (
         <div>
           <button onClick={this.toggleDisplay}>Toggle Display</button>
           <h1>Displayed!</h1>
         </div>
      ); }
      else {
        return (
         <div>
           <button onClick={this.toggleDisplay}>Toggle Display</button>
         </div>
      );
      }
    }
  };




/* Use && for a More Concise Conditional

There's a more concise way to achieve the same result. Imagine that you are tracking several 
conditions in a component and you want different elements to render depending on each of these 
conditions.
If you write a lot of else if statements to return slightly different UIs, you may repeat code 
which leaves room for error. Instead, you can use the && logical operator to perform conditional 
logic in a more concise way. This is possible because you want to check if a condition is true, 
and if it is, return some markup. Example:
*/

{condition && <p>markup</p>}

/*
If the condition is true, the markup will be returned. If the condition is false, the operation 
will immediately return false after evaluating the condition and return nothing. You can include 
these statements directly in your JSX and string multiple conditions together by writing && after
each one.
*/

class MyComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        display: true
      }
      this.toggleDisplay = this.toggleDisplay.bind(this);
    }
    toggleDisplay() {
      this.setState(state => ({
        display: !state.display
      }));
    }
    render() {
      // Change code below this line
      return (
         <div>
           <button onClick={this.toggleDisplay}>Toggle Display</button>
           {this.state.display && <h1>Displayed!</h1>}
           
         </div>
      );
    }
  };





/* Use a Ternary Expression for Conditional Rendering

there's one last way to use built-in JavaScript conditionals to render what you want: the ternary operator.
The ternary operator is often utilized as a shortcut for if/else statements in JavaScript.

Because of how JSX is compiled, if/else statements can't be inserted directly into JSX code.
(So far, whenever an if/else statement was required, it was always outside the return statement.)
A ternary operator has three parts, but you can combine several ternary expressions together. 

Here's the basic syntax:
*/

condition ? expressionIfTrue : expressionIfFalse;


// Example 

const inputStylee = {
  width: 235,
  margin: 5
};

class CheckUserAge extends React.Component {
  constructor(props) {
    super(props);
    // Change code below this line
    this.state = {
      input: '',
      userAge: ''}
    // Change code above this line
    this.submit = this.submit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(e) {
    this.setState({
      input: e.target.value,
      userAge: ''
    });
  }
  submit() {
    this.setState(state => ({
      userAge: state.input
    }));
  }
  render() {
    const buttonOne = <button onClick={this.submit}>Submit</button>;
    const buttonTwo = <button>You May Enter</button>;
    const buttonThree = <button>You Shall Not Pass</button>;
    return (
      <div>
        <h3>Enter Your Age to Continue</h3>
        <input
          style={inputStylee}
          type='number'
          value={this.state.input}
          onChange={this.handleChange}
        />
        <br />
        {/* Change code below this line */}
        {
          this.state.userAge === ''
            ? buttonOne
            : this.state.userAge >= 18
              ? buttonTwo
              : buttonThree
          }
        {/* Change code above this line */}
      </div>
    );
  }
}


 
/* Render Conditionally from Props

So far, you've seen how to use if/else, &&, and the ternary operator 
(condition ? expressionIfTrue : expressionIfFalse) to make conditional decisions about what to 
render and when. However, there's one important topic left to discuss that lets you combine any 
or all of these concepts with another powerful React feature: props.

In this challenge, you'll set up a child component to make rendering decisions based on props. 
You'll also use the ternary operator.
*/

class Results extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    {/* Change code below this line */}   
    return(
    <h1>
    {this.props.fiftyFifty === true
      ? 'You Win!'
      : 'You Lose!'
      }
    </h1>
    );
    {/* Change code above this line */}
  }
}

class GameOfChance extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 1
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    this.setState(prevState => {
      // Complete the return statement:
      return {
        counter: prevState.counter+1
      }
    });
  }
  render() {
    const expression = (Math.random() >= .5); 
    return (
      <div>
        <button onClick={this.handleClick}>Play Again</button>
        {/* Change code below this line */}
        <Results fiftyFifty={expression}/>
        {/* Change code above this line */}
        <p>{'Turn: ' + this.state.counter}</p>
      </div>
    );
  }
}



/* Change Inline CSS Conditionally Based on Component State */

class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    const inputLength = this.state.input.length;
    // Change code below this line
    {inputLength > 15
      ? inputStyle.border = '3px solid red'
      : inputStyle.border = '1px solid black'}
    // Change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};




/* Array.map() to Dynamically Render Elements

Conditional rendering is useful, but you may need your components to render an unknown number of elements. 
Using Array.map() in React illustrates this concept.

For example, you create a simple "To Do List" app. As the programmer, you have no way of knowing how 
many items a user might have on their list. You need to set up your component to dynamically render 
the correct number of list elements.
*/

const textAreaStyles = {
  width: 235,
  margin: 5
};

class MyToDoList extends React.Component {
  constructor(props) {
    super(props);
    // Change code below this line
    this.state = {
      userInput: '',
      toDoList: []
    }
    // Change code above this line
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  handleSubmit() {
    const itemsArray = this.state.userInput.split(',');
    this.setState({
      toDoList: itemsArray
    });
  }
  handleChange(e) {
    this.setState({
      userInput: e.target.value
    });
  }
  render() {
    const items = this.state.toDoList.map(i => <li>{i}</li>); // Change this line
    return (
      <div>
        <textarea
          onChange={this.handleChange}
          value={this.state.userInput}
          style={textAreaStyles}
          placeholder='Separate Items With Commas'
        />
        <br />
        <button onClick={this.handleSubmit}>Create List</button>
        <h1>My "To Do" List:</h1>
        <ul>{items}</ul>
      </div>
    );
  }
}



/* Give Sibling Elements a Unique Key Attribute

In the last example there was essential piece missing: when you create an array of elements, 
each one needs a key attribute set to a unique value. React uses these keys to keep track 
of which items are added, changed, or removed. This helps make the re-rendering process more 
efficient when the list is modified in any way.
*/

const frontEndFrameworks = [
  'React',
  'Angular',
  'Ember',
  'Knockout',
  'Backbone',
  'Vue'
];

function Frameworks() {
  const renderFrameworks = frontEndFrameworks.map((i) => <li key={i}>{i}</li>); // Change this line
  return (
    <div>
      <h1>Popular Front End JavaScript Frameworks</h1>
      <ul>
        {renderFrameworks}
      </ul>
    </div>
  );
};


/* Array.filter() to Dynamically Filter an Array

Another method related to map is filter, which filters the contents of an array based on a condition, 
then returns a new array. 

For example, if you have an array of users that all have a property online which can be set to true 
or false, you can filter only those users that are online by writing:
*/

let onlineUsers = users.filter(user => user.online);



// Example

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [
        {
          username: 'Jeff',
          online: true
        },
        {
          username: 'Alan',
          online: false
        },
        {
          username: 'Mary',
          online: true
        },
        {
          username: 'Jim',
          online: false
        },
        {
          username: 'Sara',
          online: true
        },
        {
          username: 'Laura',
          online: true
        }
      ]
    };
  }
  render() {
    const usersOnline = this.state.users.filter(user => user.online === true); // Change this line
    const renderOnline = usersOnline.map(i => <li key={i.username}>{i.username}</li>); // Change this line
    return (
      <div>
        <h1>Current Online Users:</h1>
        <ul>{renderOnline}</ul>
      </div>
    );
  }
}



/* Render React on the Server with renderToString

So far, you have been rendering React components on the client. Normally, this is what you will always do. 
However, there are some use cases where it makes sense to render a React component on the server. 
Since React is a JavaScript view library and you can run JavaScript on the server with Node.

There are two key reasons why rendering on the server may be used in a real world app. 
First, without doing this, your React apps would consist of a relatively empty HTML file and a large 
bundle of JavaScript when it's initially loaded to the browser. This may not be ideal for search 
engines that are trying to index the content of your pages so people can find you. If you render 
the initial HTML markup on the server and send this to the client, the initial page load contains 
all of the page's markup which can be crawled by search engines. Second, this creates a faster 
initial page load experience because the rendered HTML is smaller than the JavaScript code of the 
entire app. 

The renderToString() method is provided on ReactDOMServer, which is available here as a global object. 
The method takes one argument which is a React element:
*/

class App extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <div/>
  }
};

// Change code below this line
ReactDOMServer.renderToString(<App/>);