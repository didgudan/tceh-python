/**
 * Created by sobolevn on 01.04.16.
 */

'use strict';  // https://learn.javascript.ru/strict-mode

// Primitives:
var str = "A string";
var alsoString = 'A string';

console.log(str == alsoString);
console.log(str === alsoString);
console.log(typeof str, typeof alsoString);

var num1 = 1;
var num2 = 2.0;

console.log(num1 * num2);
console.log(1 === 1.0);

var x;
console.log(x);

x = null;
console.log(x);

// Objects:

var obj = {property: 'value'};
console.log(obj.property);
console.log(typeof(obj), obj);

var array = [obj, obj];
console.log(typeof(array), array);

// Mutability:
var newObject = obj;
newObject.newProperty = 'new value';
newObject.property = 'replace';
