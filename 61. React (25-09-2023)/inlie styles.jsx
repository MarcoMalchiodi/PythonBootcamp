/*
You apply inline styles to JSX elements similar to how you do it in HTML, 
but with a few JSX differences. Here's an example of an inline style in HTML:
*/
<div style="color: yellow; font-size: 16px">Mellow Yellow</div>

/*
JSX elements use the style attribute, but because of the way JSX is transpiled, 
you can't set the value to a string. Instead, you set it equal to a JavaScript object. 
Here's an example:
*/

inlineJsx = <div style={{color: "yellow", fontSize: 16}}>Mellow Yellow</div>
// React will not accept kebab-case keys in the style object. 


// Example

class Colorful extends React.Component {
    render() {
      return (
        <div style={{color:'red',fontSize:'72px'}}>Big Red</div>
        // fontSize instead of font-size!!!
      );
    }
  };


/* 
All property value length units (like height, width, and fontSize) are assumed to 
be in px unless otherwise specified. 

If you have a large set of styles, you can assign a style object to a constant to keep 
your code organized.
*/


const styles = {
    color: "purple", 
    fontSize: 40,
    border: '2px solid purple'};
// Change code above this line
class Colorful extends React.Component {
render() {
  // Change code below this line
  return (
    <div style={styles}>Style Me!</div>
  );
  // Change code above this line
}
};