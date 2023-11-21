/*
In JSX you can no longer use the word class to define HTML classes. 
This is because class is a reserved word in JavaScript. Instead, JSX uses className.

The naming convention for all HTML attributes and event references in JSX become camelCase. 
For example, a click event in JSX is onClick, instead of onclick.
*/

const JSX = (
    <div className="myDiv">
      <h1>Add a class to this div</h1>
    </div>
  );