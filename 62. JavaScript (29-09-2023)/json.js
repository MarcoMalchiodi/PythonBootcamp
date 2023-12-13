/* 
JSON is a text-based data format following JavaScript object syntax, 
which was popularized by Douglas Crockford. Even though it closely resembles JavaScript object 
literal syntax, it can be used independently from JavaScript, and many programming environments feature 
the ability to read (parse) and generate JSON.

JSON exists as a string — useful when you want to transmit data across a network. It needs to be 
converted to a native JavaScript object when you want to access the data. This is not a big issue — 
JavaScript provides a global JSON object that has methods available for converting between the two.
*/


fetch('example.json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Work with the JSON data here
    console.log(data);
    console.log(data.homeTown);
    console.log(data["active"]);
  })
  .catch(error => {
    console.error('Fetch error:', error);
});



// To access data further down the hierarchy, you have to chain the required property names 
// and array indexes together. For example, to access the third superpower of the second hero listed 
// in the members list, you'd do this:

data["members"][1]["powers"][2];


/* JSON.parse()
A common use of JSON is to exchange data to/from a web server.
When receiving data from a web server, the data is always a string.
Parse the data with JSON.parse(), and the data becomes a JavaScript object. */

const obj1 = JSON.parse('{"name":"John", "age":30, "city":"New York"}');
alert(obj1.name); //John



/* DATES
Date objects are not allowed in JSON.
If you need to include a date, write it as a string.
You can convert it back into a date object later:
*/
const text1 = '{"name":"John", "birth":"1986-12-14", "city":"New York"}';
const obj = JSON.parse(text1);
obj.birth = new Date(obj.birth);

document.getElementById("demo").innerHTML = obj.name + ", " + obj.birth;


/* FUNCTIONS
Functions are not allowed in JSON.
If you need to include a function, write it as a string.
You can convert it back into a function later:
*/
const texto = '{"name":"John", "age":"function () {return 30;}", "city":"New York"}';
const obj = JSON.parse(texto);
obj.age = eval("(" + obj.age + ")");

document.getElementById("demo").innerHTML = obj.name + ", " + obj.age();
// You should avoid using functions in JSON, the functions will lose their scope, 
//and you would have to use eval() to convert them back into functions.




/* JSON.stringify()
A common use of JSON is to exchange data to/from a web server.
When sending data to a web server, the data has to be a string.
Assume: */
const obj = {name: "John", age: 30, city: "New York"};
//converting it into a string
const mioJSON = JSON.stringify(obj);
// myJSON is now a string, and ready to be sent to a server


// It is also possible to stringify JavaScript arrays:
const arr = ["John", "Peter", "Sally", "Jane"];
const yourJSON = JSON.stringify(arr);



/* STORING DATA
When storing data, the data has to be a certain format, 
and regardless of where you choose to store it, text is always one of the legal formats. */
// Storing data:
const myObj = {name: "John", age: 31, city: "New York"};
const myJSON = JSON.stringify(myObj);
localStorage.setItem("testJSON", myJSON);

// Retrieving data:
let text = localStorage.getItem("testJSON");
let obj = JSON.parse(text);
document.getElementById("demo").innerHTML = obj.name;


