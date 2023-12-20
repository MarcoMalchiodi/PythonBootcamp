/*
The split method splits a string into an array of strings. It takes an argument for the delimiter, 
which can be a character to use to break up the string or a regular expression. 

The join method is used to join the elements of an array together to create a string. 
It takes an argument for the delimiter that is used to separate the array elements in the string.

the trim() method is used to remove whitespace characters (such as spaces, tabs, and line breaks) 
from both the beginning and end of a string.
*/

const str = "Hello World";
const bySpace = str.split(" "); // ["Hello", "World"]

const otherString = "How9are7you2today"; 
const byDigits = otherString.split(/\d/); // ["How", "are", "you", "today"]


// Checking if a char is a letter
function isNotALetter(char) {
    // Use a regular expression to check if the character is not a letter
    if (/[^A-Za-z]/.test(char)) {
      return true; // Character is not a letter
    } else {
      return false; // Character is a letter
    }
  }


// Splitify function
function splitify(str) {
    // Only change code below this line
    let newStr = [];
    for (let n=0; n < str.length;n++) {
      if ((/[^A-Za-z]/.test(str[n]))) {
        newStr.push(" ");
      } else {
        newStr.push(str[n]);
      };
      }
    newStr = newStr.join("");
    return newStr.split(" ");
    // Only change code above this line
  };
  
splitify("Hello World,I-am code");




function sentensify(str) {
  return str.split(/[^A-Za-z]/).join(" ");
}

console.log(sentensify("May-the-force-be-with-you"));





// URL slug
var globalTitle = "Winter Is Coming";

// Add your code below this line
function urlSlug(title) {
  return title
    .toLowerCase()
    .trim()
    .split(/\s+/)
    .join("-");
}
// Add your code above this line

var winterComing = urlSlug(globalTitle); // Should be "winter-is-coming"