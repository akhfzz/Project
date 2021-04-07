$(function() {
    $('#btnSignUp').click(function() {
 
        $.ajax({
            url: '/form',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
$(function() {
    $('#ok').click(function() {
 
        $.ajax({
            url: '/admins',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});