/* Property getters and setters
There are two kinds of object properties.

The first kind is data properties. All properties that we’ve been using until now were data properties.

The second type of property is something new. It’s an accessor property. 
They are essentially functions that execute on getting and setting a value, 
but look like regular properties to an external code. */


// GETTERS AND SETTERS
// Accessor properties are represented by “getter” and “setter” methods. 
// In an object literal they are denoted by get and set:
let obj = {
    get propName() {
      // getter, the code executed on getting obj.propName
    },
  
    set propName(value) {
      // setter, the code executed on setting obj.propName = value
    }
  };
// The getter works when obj.propName is read, the setter – when it is assigned.



// Example

let user = {
    name: "John",
    surname: "Smith",

    get fullName() {
        return `${this.name} ${this.surname}`;
      },
    
// As of now, fullName has only a getter. If we attempt to assign user.fullName=, there will be an error
// Let’s fix it by adding a setter for user.fullName:    
    set fullName(value) {
        [this.name, this.surname] = value.split(" ");
    },
    
  };

alert(user.fullName); // John Smith
// We don’t call user.fullName as a function, we read it normally: the getter runs behind the scenes.


// set fullName is executed with the given value.
user.fullName = "Alice Cooper";

alert(user.name); // Alice
alert(user.surname); // Cooper





// ACESSOR DESCRIPTORS
/* Descriptors for accessor properties are different from those for data properties.

For accessor properties, there is no value or writable, but instead there are get and set functions.

That is, an accessor descriptor may have:

get – a function without arguments, that works when a property is read,
set – a function with one argument, that is called when the property is set,
enumerable – same as for data properties,
configurable – same as for data properties. */


// for instance, to create an accessor fullName with defineProperty, 
// we can pass a descriptor with get and set:

let user1 = {
    name: "John",
    surname: "Smith"
  };
  
  Object.defineProperty(user1, 'fullName', {
    get() {
      return `${this.name} ${this.surname}`;
    },
  
    set(value) {
      [this.name, this.surname] = value.split(" ");
    }
  });
  
  alert(user1.fullName); // John Smith
  
  for(let key in user1) alert(key); // name, surname


/* 
Please note that a property can be either an accessor (has get/set methods) or a data property 
(has a value), not both.
If we try to supply both get and value in the same descriptor, there will be an error:
*/