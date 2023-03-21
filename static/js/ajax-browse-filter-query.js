
$(document).ready(function() {
    $('#book_search_form').on("submit", function(e) {
        e.preventDefault();
        $.ajax( {
            type: 'POST',
            url: '/bookShare/browse/',
            data: new FormData(this),
            processData: false,
            contentType: false,
            success: function (response) {
                $("#results_container").html(response);
            }
        });
    });
});
    