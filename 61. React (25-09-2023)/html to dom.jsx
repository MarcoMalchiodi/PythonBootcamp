/* 
With React, we can render this JSX directly to the HTML DOM using React's rendering API known as ReactDOM.

ReactDOM offers a simple method to render React elements to the DOM which looks like this: 
ReactDOM.render(componentToRender, targetNode), where the first argument is the React element 
or component that you want to render, and the second argument is the DOM node that you want to render 
the component to.

ReactDOM.render() must be called after the JSX element declarations.
*/



const JSX = (
    <div>
      <h1>Hello World</h1>
      <p>Lets render this to the DOM</p>
    </div>
  );
  // Add your code below this line
  
  ReactDOM.render(JSX,document.getElementById('some-id'));