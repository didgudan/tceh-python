/**
 * Created by sobolevn on 01.04.16.
 */

'use strict';

(function (window, document) {
    function colorizeTexts() {
        var body = document.getElementsByTagName('body')[0];
        body.style.color = 'red';
    }

    function setStatus(status) {
        var statusAlert = document.getElementById('status');
        var successColor = statusAlert.getAttribute('data-success-color');
        var failureColor = statusAlert.getAttribute('data-failure-color');

        var textStatus = status ? 'Success' : 'Failure';
        var element = document.createElement('p');
        element.style.backgroundColor = status ? successColor : failureColor;
        element.innerText = textStatus; // test this on firefox and safari.
        statusAlert.appendChild(element);
    }

    // http://stackoverflow.com/questions/9899372/pure-javascript-equivalent-to-jquerys-ready-how-to-call-a-function-when-the

    document.addEventListener('DOMContentLoaded', function () {
        var control = document.getElementById('toggle');
        control.onclick = function (event) {
            colorizeTexts();
            setStatus(Math.round(Math.random()));
        };

        // or:
        //control.addEventListener('click', function() {
        //    colorizeTexts();
        //    setStatus(Math.round(Math.random()));
        //});
    });
})(window, document);
