/**
 * Created by sobolevn on 01.04.16.
 */

var apples = "2";
var oranges = "3";

console.log(apples + oranges);
console.log(+apples + +oranges);

console.log(parseInt('02.34ssd'));
console.log(parseFloat('2.34ssd'));

console.log(Number('2.3'));

var toBool = 'string';
console.log(!!toBool);
console.log(Boolean(toBool));

console.log(String(null));
console.log(+undefined);

/**
 > !!'s'
true
> !!''
false
> !!'1'
true
> !!'0'
true
> !!0
false
> !!!!0
false
> !![]
true
> !!{}
true
> !!null
false
> !!undefined
 false
 **/

// Comparing different types:
console.log(1 == '1');
console.log(1 === '1');
console.log(0 == false);
console.log(1 == true);
console.log(1 === true);
console.log('' == null);
console.log(null == undefined);
console.log(null === undefined);
console.log(0 == []);
console.log(1 == {});
