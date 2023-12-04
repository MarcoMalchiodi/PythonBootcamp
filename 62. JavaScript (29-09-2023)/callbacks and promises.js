/* CALLBACKS
A callback function is a function passed into another function as an argument, 
which is then invoked inside the outer function to complete some kind of routine or action. */

// Callbacks are simply functions that get passed into other functions. For example:
myDiv.addEventListener("click", function(){
    // do something!
  });
// Here, the function addEventListener() takes a callback (the “do something” function) 
// and then calls it when myDiv gets clicked





/* PROMISES

There are multiple ways that you can handle asynchronous code in JavaScript, 
and they all have their use cases. Promises are one such mechanism, and they’re one you will 
see somewhat often when using other libraries or frameworks. Knowing what they are and how to use ù
them is quite useful.

Essentially, a promise is an object that might produce a value at some point in the future. 
Here’s an example:
Lets say getData() is a function that fetches some data from a server and returns it as an object 
that we can use in our code: */
const getData = function() {
    // go fetch data from some API...
    // clean it up a bit and return it as an object:
    return data
  };


// The issue with this example is that it takes some time to fetch the data, but unless we tell our 
// code that, it assumes that everything in the function happens essentially instantly.
// So, if we try to do this:
const myData = getData();
const pieceOfData = myData['whatever'];
// myData will be undefined (too quick).
// We need to tell our code to wait until the data is done fetching to continue. 
// Promises solve this issue:

const myDato = getData(); // if this is refactored to return a Promise...

myDato.then(function(data){ // .then() tells it to wait until the promise is resolved
  const pieceOfData = data['whatever'] // and THEN run the function inside
});




//Promise example

let p = new Promise((resolve,reject) => {
  let a = 1+1;
  if (a==2) {
    resolve('Success');
  } else {
    reject('Failed');
  }
});

p.then((message) => { // when a==2 True
  console.log('This is in the then '+message)
}).catch((message) => { // when a != 2
  console.log('This i in the catch '+message)
});

