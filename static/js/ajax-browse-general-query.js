
$(document).ready(function(e) {
    $('#book_search_form').on("submit", submitHandler);
    $('#filter_search_form').on("input", submitHandler);
    submitHandler(null); // Load in results initially
});

function submitHandler(e) {
    if (e) {
        e.preventDefault();
    }
    var fields = ["general_query","genre_query","publisher_query","author_query","max_radius_query","available_only"]
    console.log(csrftoken);
    var data = {"csrfmiddlewaretoken":csrftoken};
    for (var field in fields) {
        data[fields[field]] = $("#"+fields[field]+"_field").val();
    }
    console.log(data);
    $.ajax( {
        type: 'POST',
        url: '/bookShare/browse/',
        data: data,
        success: function (response) {
            $("#book_search_form")[0].reset(); // Clear input field on search
            $("#results_container").html(response);
        }
    });
}

function searchAuthor(e, author) {
    e.preventDefault();
    $("#book_search_form")[0].reset();
    $("#filter_search_form")[0].reset();
    $("#author_query_field").val(author);
    submitHandler(null);
}