
$(document).ready(function(e) {
    $('#book_search_form').on("submit", submitHandler);
    $('#filter_search_form').on("input", submitHandler);
    $('#sort_form').on("input", submitHandler);
    submitHandler(null); // Load in results initially
});

function submitHandler(e) {
    if (e) {
        e.preventDefault();
    }
    var fields = ["general_query","genre_query","publisher_query","author_query","max_radius","postcode","available_only","sort"]
    
    var data = {"csrfmiddlewaretoken":csrftoken};
    for (var field in fields) {
        data[fields[field]] = $("#"+fields[field]+"_field").val();
    }
    $("#valid_postcode").html("&#8634");
    console.log(data);
    $.ajax( {
        type: 'POST',
        url: '/bookShare/browse/',
        data: data,
        success: function (response) {
            $("#book_search_form")[0].reset(); // Clear input field on search
            $("#results_container").html(response["results_container"]);
            if (response["valid_postcode"]) {
                $("#valid_postcode").html("&#10003");
            } else {
                $("#valid_postcode").html("&#10007");
            }
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