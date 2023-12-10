/* Object constructors can easily lead to bugs in the long run.
Factory constructors are a good alternative. 
One of the biggest issues with constructors is that while they look just like regular functions, 
they do not behave like regular functions at all. If you try to use a constructor function without 
the new keyword, your program will not work as expected, but it won’t produce error messages that a
re easy to trace.*/

// Factories are simply plain old JavaScript functions that return objects for us to use in our code.

// Rule of thumb: if you only ever need ONE of something, use a module. 
// If you need multiples of something (ex players), create them with factories.

// The factory function pattern is similar to constructors, but instead of using new to create an object, 
// factory functions simply set up and return the new object when you call the function.

const personFactory = (name, age) => {
    const sayHello = () => console.log('hello!');
    return { name, age, sayHello };
  };
  
const jeff = personFactory('jeff', 27);
  
console.log(jeff.name); // 'jeff'
  
jeff.sayHello(); // calls the function and logs 'hello!'

// or

const Person = function(name, age) {
    this.sayHello = () => console.log('hello!');
    this.name = name;
    this.age = age;
  }; // same thing but as an object cosntructor

// Note that factory functions do not utilize the prototype



// Example
const FactoryFunction = string => {
    const capitalizeString = () => string.toUpperCase();
    const printString = () => console.log(`----${capitalizeString()}----`);
    return { printString };
  };
  
const taco = FactoryFunction('taco');
  
printString(); // ERROR!!
capitalizeString(); // ERROR!!
taco.capitalizeString(); // ERROR!!
taco.printString(); // this prints "----TACO----"
// the only way to use either of those functions is to return them in the object



// another example
const counterCreator = () => {
    let count = 0;
    return () => {
      console.log(count);
      count++;
    };
  };
  
  const counter = counterCreator();
  
  counter(); // 0
  counter(); // 1
  counter(); // 2
  counter(); // 3




// Back to Factory Functions
const Player = (name, level) => {
    let health = level * 2;
    const getLevel = () => level;
    const getName  = () => name;
    const die = () => {
      // uh oh
    };
    const damage = x => {
      health -= x;
      if (health <= 0) {
        die();
      }
    };
    const attack = enemy => {
      if (level < enemy.getLevel()) {
        damage(1);
        console.log(`${enemy.getName()} has damaged ${name}`);
      }
      if (level >= enemy.getLevel()) {
        enemy.damage(1);
        console.log(`${name} has damaged ${enemy.getName()}`);
      }
    };
    return {attack, damage, getLevel, getName};
  };
  
  const jimmie = Player('jim', 10);
  const badGuy = Player('jeff', 5);
  jimmie.attack(badGuy);




// Inheritance with Factories
const Persona = (name) => {
    const sayName = () => console.log(`my name is ${name}`);
    return {sayName};
  }
  
const Nerd = (name) => {
    // simply create a person and pull out the sayName function with destructuring assignment syntax!
    const {sayName} = Person(name);
    const doSomethingNerdy = () => console.log('nerd stuff');
    return {sayName, doSomethingNerdy};
    // If you want to go ahead and lump ALL of another object in, 
    // you can certainly do that as well with Object.assign:
    // return Object.assign({}, prototype, {doSomethingNerdy});
  }
  
const jeffo = Nerd('jeff');
  
jeffo.sayName(); // my name is jeff
jeffo.doSomethingNerdy(); // nerd stuff





// MODULE PATTERNS
// Modules are actually very similar to factory functions. The main difference is how they’re created.

const calculator = (() => {
    const add = (a, b) => a + b;
    const sub = (a, b) => a - b;
    const mul = (a, b) => a * b;
    const div = (a, b) => a / b;
    return {
      add,
      sub,
      mul,
      div,
    };
  })();
  
  calculator.add(3,5); // 8
  calculator.sub(6,2); // 4
  calculator.mul(14,5534); // 77476