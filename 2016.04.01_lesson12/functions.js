/**
 * Created by sobolevn on 01.04.16.
 */

function log(value) {
    console.log(value);
}


var namedLog = function(value) {
    console.log('named', value);
};


var nfe = function namedFunctionalExpression (i) {
    if (i == 0) {
        return 0;
    }
    return i + namedFunctionalExpression(i - 1); // i-- or --i
};

log(123);
namedLog('asd');
console.log(nfe(5));
// namedFunctionalExpression(5);

log = console.log;
log(1, 2, 3);

console.log(typeof namedLog);
namedLog = null;
// namedLog(23);
