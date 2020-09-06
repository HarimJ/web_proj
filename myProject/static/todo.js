$("#new-todo").keypress(function (event) {
    var keycode = event.keyCode ? event.keyCode : event.which;
    if (keycode == "13") {
        console.log("pressed");

        if ($(this).val().length !== 0) {
            var toDoCount = $("span.box").length + 1;

            $("#todos").prepend(
                '<li><input id="checkbox-' +
                toDoCount +
                '" type="checkbox"><label for="checkbox-' +
                toDoCount +
                '">' +
                $(this).val() +
                '<span class="box"></span></label></li>'
            );
            $(this).val("");
        }
    }
});
