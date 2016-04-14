/**
 * Created by sobolevn on 01.04.16.
 */

(function (document, window) {
    function scoped() {
        console.log('scoped');
        console.log(window, document);
    }

    scoped();
})(document, window);
