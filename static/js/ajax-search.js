
$(document).ready(function() {
    $('#user-search-input').on("input", function(e) {
        e.preventDefault();
        var username = $(this).val();
        $.ajax( {
            type: 'POST',
            url: '/bookShare/search/',
            data: {"username":username, "csrfmiddlewaretoken":csrftoken},
            success: function (response) {
                var instances = response["instances"];
                if (instances.length == 0) {
                    $("#results-container").html("<li><h4>No users found.</h4></li>");
                }
                $("#results-container").empty();
                instances.forEach((username) => {
                    $("#results-container").append(`<li><a href = '/bookShare/${username}/profile'>${username}</a></li>`);
                })
            }
        })
    });
});
    