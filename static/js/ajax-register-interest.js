var hidden = true;
$(document).ready(function() {
    $("#view-interest-users").on("click", function(e) {
        if (hidden) {
            $(this).text("Hide Interested Users");
            $("#interested-users").css("display", "block");
            hidden = false;
        }
        else {
            $(this).text("Show Interested Users");
            $("#interested-users").css("display", "none");
            hidden = true;
        }
    })
    $('#change-interest-button').on("click", function(e) {
        e.preventDefault();
        $.ajax( {
            type: 'POST',
            url: `/bookShare/book/${bookId}/${(isInterested ? "remove_interest/" : "add_interest/")}`,
            data: {"csrfmiddlewaretoken":csrftoken},
            success: function (response) {
                isInterested = !isInterested
                $('#change-interest-button').text((isInterested ? "Remove Interest" : "Register Interest"))
            }
        })
    });
});
    