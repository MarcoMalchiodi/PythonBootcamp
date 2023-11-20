const JSX = <h1>Hello JSX!</h1>;

/*
One important thing to know about nested JSX is that it must return a single element.
This one parent element would wrap all of the other levels of nested elements.
For instance, several JSX elements written as siblings with no parent wrapper element will not transpile.


Here's an example:                  */

<div>
  <p>Paragraph One</p>
  <p>Paragraph Two</p>
  <p>Paragraph Three</p>
</div>


/* Invalid JSX:

<p>Paragraph One</p>
<p>Paragraph Two</p>
<p>Paragraph Three</p> */


// Example
const JSX2 = <div>
                <h1></h1>
                <p></p>
                {/* this is a comment */}
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </div>;


