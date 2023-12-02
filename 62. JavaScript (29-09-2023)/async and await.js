/* Asynchronous code can become difficult to follow when it has a lot of things going on. 
async and await are two keywords that can help make asynchronous read more like synchronous code. 

For example, the two code blocks below do the exact same thing. 
They both get information from a server, process it, and return a promise:
*/
function getPersonsInfo(name) {
    return server.getPeople().then(people => {
      return people.find(person => { return person.name === name });
    });
  };

  async function getPersonsInfo(name) {
    const people = await server.getPeople();
    const person = people.find(person => { return person.name === name });
    return person;
  };




/* ASYNC
The async keyword is what lets the JavaScript engine know that you are declaring an asynchronous function. 
This is required to use await inside any function. When a function is declared with async, 
it automatically returns a promise; returning in an async function is the same as resolving a promise. 
Likewise, throwing an error will reject the promise.

The async keyword can also be used with any of the ways a function can be created. 
Said differently: it is valid to use an async function anywhere you can use a normal function. */

const yourAsyncFunction = async () => {
    // do something asynchronously and return a promise
    return result;
  }

  anArray.forEach(async item => {
    // do something asynchronously for each item in 'anArray'
    // one could also use .map here to return an array of promises to use with 'Promise.all()'
  });

  server.getPeople().then(async people => {
    people.forEach(person => {
      // do something asynchronously for each person
    });
  });


/* AWAIT
await is pretty simple: it tells JavaScript to wait for an asynchronous action to finish before 
continuing the function. It’s like a ‘pause until done’ keyword. The await keyword is used to get a 
value from a function where you would normally use .then(). Instead of calling .then() after the 
asynchronous function, you would simply assign a variable to the result using await. 
Then you can use the result in your code as you would in your synchronous code. */



// Example

// From this:
const img = document.querySelector('img');
  fetch('https://api.giphy.com/v1/gifs/translate?api_key=YOUR_KEY_HERE&s=cats', {mode: 'cors'})
    .then(function(response) {
      return response.json();
    })
    .then(function(response) {
      img.src = response.data.images.original.url;
    });

// to this:

const img1 = document.querySelector('img');

  async function getCats() {
    const response = await fetch('https://api.giphy.com/v1/gifs/translate?api_key=YOUR_KEY_HERE&s=cats', {mode: 'cors'});
    const catData = await response.json();
    img1.src = catData.data.images.original.url;
  }
  getCats();

  