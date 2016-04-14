/**
 * Created by sobolevn on 01.04.16.
 */

var flag = true;

if (!flag) {
    console.log('if');
} else if (flag && 1 < 2) {
    console.log('elseif');
} else {
    // do nothing.
}


var ternary = 40 > 13 ? 'yes' : 'no';
console.log(ternary);

var value = '123';

switch (value) {
    case '321':
        console.log('1');
        break;
    case '123':
        console.log('2');
        break;
    default:
        console.log('other');
        break;
}


for (var i = 0; i < 10; i++) {
    console.log(i);
}


var iterable = [1, 2, 3, 4, 5];
for (var item in iterable) {
    console.log(item);
}


// var i = 0;
var s = 0;

do {
    console.log(s);
    s++;
} while (s < 4);