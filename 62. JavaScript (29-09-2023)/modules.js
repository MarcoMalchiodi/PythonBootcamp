// There are only 2 components to it - import and export
// <script type="module" src="modules.js"></script>

import myName from './module_example.js';
import {functionOne, functionTwo} from './myModule';

function component() {
    const element = document.createElement('div');
  
    // use your function!
    element.textContent = myName('Cody');
    return element;
  }
  
document.body.appendChild(component());
alert(functionOne);