/*

first value > previous value
second value > current value
third value > current index
fourth value > the array itself

(p,c,i,a) =>...

The reduce method allows for more general forms of array processing, and it's possible to 
show that both filter and map can be derived as special applications of reduce. 
The reduce method iterates over each item in an array and returns a single value 
(i.e. string, number, object, array). This is achieved via a callback function that is called 
on each iteration.

The callback function accepts four arguments. The first argument is known as the accumulator, 
which gets assigned the return value of the callback function from the previous iteration, 
the second is the current element being processed, the third is the index of that element and 
the fourth is the array upon which reduce is called.

In addition to the callback function, reduce has an additional parameter which takes an initial 
value for the accumulator. If this second parameter is not used, then the first iteration is 
skipped and the second iteration gets passed the first element of the array as the accumulator.
*/





// find the sum

const numbers = [3,6,2,9,1];
let sum = numbers.reduce(
  // first we inser a function of its own that will run iterating over each item
  // it will take two arguments: previousValue (from the last function call) and currentValue
  (prev,curr) => {
    return prev + curr; // this returns whatever prev is going to be in the next iteration
  }, 0 // 0 is the initial value (NOT AN INDEX!!!)

);





// find the oldest age
const people = [
  {
    name: "Dom Perry",
    age:35
  },
  {
    name: "Dam Poorry",
    age:48
  },
  {
    name: "Dim Peerry",
    age:27
  }
];

let oldestAge = people.reduce(
  (prev,curr) => {
    // in this case prev and curr are both going to be objects
    if (curr.age > prev) { 
      // we don't need to write prev.age because the 
      // first prev is 0.
      return curr.age;
    } else {
      return prev;
    }
  }

,0);




const users = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 }
];

const sumOfAges = users.reduce((sum, user) => sum + user.age, 0);
console.log(sumOfAges); //64



// another example

const users2 = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 }
];

const usersObj = users2.reduce((obj, user) => {
  obj[user.name] = user.age;
  return obj;
}, {});
console.log(usersObj); // { John: 34, Amy: 20, camperCat: 10 }




// uaing all parameters to build a string

oldestAge = people.reduce(
  (prev,curr,currIndex,array) => {
    const split = curr.split(" "); // split is going to be an array cotnainign two items
    let part = `${split[0][0]}${split[1][0]}`; // getting the initials
    
    if (currIndex === array.length - 1) {
      part += ".";
    } else {
      part += ", ";
    };

    return prev+part;
  }
,"");

