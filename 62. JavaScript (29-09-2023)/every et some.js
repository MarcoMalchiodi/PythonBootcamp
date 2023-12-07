/*
The every method works with arrays to check if every element passes a particular test. 
It returns a Boolean value - true if all values meet the criteria, false if not.

The some method works with arrays to check if any element passes a particular test. 
It returns a Boolean value - true if any of the values meet the criteria, false if not.
*/

const numbers = [1, 5, 8, 0, 10, 11];

numbers.every(function(currentValue) {
  return currentValue < 10;
});
// The every method would return false here.

numbers.some(function(currentValue) {
  return currentValue < 10;
});
// True

