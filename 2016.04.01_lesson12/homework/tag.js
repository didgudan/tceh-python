'use strict';

// Пятнашки в браузере. Берем полюбившийся вам пример из Python, реализовываем его на Javascript.
// Задача: реализовать игру пятнашки, поле: 15 <div> тегов с цифрами, один пустой. Пустой тег можно двигать, используя клавиатуру.
// Задачи со звездочками:
// Добавить оформление css стилями, можно использовать Bootstrap
// Реализовать `Drag-n-Drop` для передвижения фишек

(function (document, window) {
    var EMPTY_MARK = " "

    function shuffle(array) {
        var currentIndex = array.length, temporaryValue, randomIndex;

        // While there remain elements to shuffle...
        while (0 !== currentIndex) {

            // Pick a remaining element...
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;

            // And swap it with the current element.
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
        }

        // return array;
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, EMPTY_MARK, 13, 14, 15, 12];
    }

    function make_game_array(arr_length) {
        var arr = []
        for (var i = 1; i <= arr_length; i++) {
            arr.push(i);
        }
        arr.push(EMPTY_MARK);
        arr = shuffle(arr);

        return arr;
    }

    function can_i_move(new_position) {
        for (var i = 0; i < 2; i++ ) {
            if (new_position[i] < 1 || new_position[i] > 4){
                return false
            }
        }
        return true
    }

    function get_key_by_position(position){
        return (position[0]-1)*4 + position[1] - 1
    }

    document.addEventListener('keydown', function(event) {
        switch(event.keyCode) {
            case 38: 
                var direction = "up";
                break;
            case 40: 
                var direction = "down";
                break;
            case 37: 
                var direction = "left";
                break;
            case 39: 
                var direction = "right";
                break;
            default:
                return
        }

        var current_index = tag_arr.indexOf(EMPTY_MARK);
        var current_position = [ Math.floor((current_index / 4) + 1), current_index%4 + 1 ];

        if (direction === "up") {
            var new_position = [ current_position[0] - 1, current_position[1] ];
        }
        else if (direction === "down"){
            var new_position = [ current_position[0] + 1, current_position[1] ];
        } 
        else if (direction === "left"){
            var new_position = [ current_position[0], current_position[1] - 1 ];  
        } 
        else if (direction === "right"){
            var new_position = [ current_position[0], current_position[1] + 1 ];
        } 

        if (can_i_move(new_position) === true) {
            var current_key = get_key_by_position(current_position);
            var new_key = get_key_by_position(new_position); 

            var temp = tag_arr[current_key];
            tag_arr[current_key] = tag_arr[new_key];
            tag_arr[new_key] = temp;

            render_field();
            
            if (is_game_finished() === true) {
                document.body.innerHTML = '\
                 <div class="container-fluid"><div class="row"><div class="col-md-12"> \
                <h1 style="font-size: 1000%;" class="text-center">YOU WIN!</h1>\
                </div></div></div>\
                <img src="win1.gif" class="win"><br>\
                <img src="win4.gif" class="win"><br>\
                <img src="win2.gif" class="win"><br>\
                <img src="win3.gif" class="win"><br>\
                ';
            }
        }
    });

    function render_field() {
         for (var i = 1; i <= 16; i++) {
            var current_div = document.getElementById('div'.concat(i));
            
            if (tag_arr[i-1] === EMPTY_MARK) {
               current_div.className = "empty"; 
            } else {
                current_div.className = "ordinary";
            }

            current_div.innerText = tag_arr[i-1];
        }
        
        var random_number = Math.floor(Math.random()*(11)+1);
        document.getElementById('dance').src = "dance".concat(random_number, ".gif");
    }

    function is_game_finished() {
        if (tag_arr[ tag_arr.length-1 ] != EMPTY_MARK) {
            return false;
        }

        for (var i = 0; i < 15; i++) {
            if (tag_arr[i] != i+1) {
                return false;  
            } 
        }

        return true;
    }

    var tag_arr = make_game_array(15);
    render_field();
})(document, window);

