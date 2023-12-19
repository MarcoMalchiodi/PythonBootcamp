/*
The sort method sorts the elements of an array according to the callback function.
*/

function ascendingOrder(arr) {
    return arr.sort(function(a, b) {
      return a - b;
    });
};
  
ascendingOrder([1, 5, 2, 3, 4]);
// This would return the value [1, 2, 3, 4, 5]


// reversed alphabetical order
function reverseAlpha(arr) {
    return arr.sort(function(a, b) {
      return a === b ? 0 : a < b ? 1 : -1;
    });
};
  
reverseAlpha(['l', 'h', 'z', 'b', 's']);
// This would return the value ['z', 's', 'l', 'h', 'b']



//alphabetical order:
function alphabeticalOrder(arr) {
    // Only change code below this line
    arr.sort(function(a,b){
        return a === b ? 0 : a < b ? -1 : 1;
    });
    return arr;
    // Only change code above this line
  }
  
console.log(alphabeticalOrder(["a", "d", "c", "a", "z", "g"]));
// [ 'a', 'a', 'c', 'd', 'g', 'z' ]



// Without Changing the Original Array
const globalArray = [5, 6, 3, 2, 9];

function nonMutatingSort(arr) {
  // Only change code below this line
  let newArr = [...arr];
  return newArr.sort(function(a,b){
    return a-b;
  });

  // Only change code above this line
}

nonMutatingSort(globalArray);