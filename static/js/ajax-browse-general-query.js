
$(document).ready(function(e) {
    $('#book_search_form').on("submit", submitHandler);
    $('#filter_search_form').on("input", submitHandler);
    $('#filter_search_form').on("submit", submitHandler);
    $('#sort_form').on("input", submitHandler);
    submitHandler(null); // Load in results initially

    $('.filter_box .collapsible').css({'display':'none'});
    $('.filter_box h2').on("click", function (e) {
        if (this.contentsVisible) {
            this.contentsVisible = false;
            console.log(this);
            $(this.parentNode).find('.collapsible').css({'display':'none'});
            $(this.parentNode).find('.open_indicator').html("&#9660");
            $(this.parentNode).find('input').val(""); // Reset input field when closed
        } else {
            this.contentsVisible = true;
            $(this.parentNode).find('.collapsible').css({'display':'block'});
            $(this.parentNode).find('.open_indicator').html("&#9650");
        }
    });
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
    $(".search_submit").css({"background-image":"url('/static/images/loading.png')"});
    console.log(data);
    $.ajax( {
        type: 'POST',
        url: '/bookShare/browse/',
        data: data,
        success: function (response) {
            $("#results_container").html(response["results_container"]);
            $(".search_submit").css({"background-image":"url('/static/images/search.png')"});
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