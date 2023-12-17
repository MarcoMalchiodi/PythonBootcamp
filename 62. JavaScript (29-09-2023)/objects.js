const myObject = {
    property: 'Value!',
    otherProperty: 77,
    "obnoxious property": function() {
      // do stuff!
   }
  }


/* There are also 2 ways to get information out of an object: dot notation and bracket notation. */

// dot notation
myObject.property // 'Value!'

// bracket notation
myObject[property]
myObject["obnoxious property"] // [Function]




/* When you have a specific type of object that you need to duplicate like our player or inventory items,
a better way to create them is using an object constructor, which is a function that looks like this: */

function Player(name, marker)  {
    this.name = name
    this.marker = marker
    this.sayName = function() {
        console.log(name)
      }
  }

// and which you use by calling the function with the keyword new: 
const player = new Player('steve', 'X')
console.log(player.name) // 'steve'
player.sayName() // logs 'steve'


// exercises
function Book(name,author,pages,read) {
    this.name = name
    this.author = author
    this.pages = String(pages)
    this.read = read

    this.info = function() {
        read_status = ""
        if (read) {
            read_status = "Has already been read."
        } else {
            read_status = "Not read yet.";
        }

        console.log(`${name} by ${author}, number of pages: ${pages}. ${read_status}`)
    }
}

const my_book = new Book('YF1M','Dan Pena',320,true);
my_book.info();

/* Book is our prototype.
To check and object's prototype we can use Object.getPrototypeOf()
*/
Object.getPrototypeOf(my_book);


// creating prototypes to save memory

function Apple(color) {
    this.color = color
};

Apple.prototype = {
    throw () {
        console.log('bam')
    }
};

const Apple1 = new Apple('green');
const Apple2 = new Apple('red');

Apple1.throw();
