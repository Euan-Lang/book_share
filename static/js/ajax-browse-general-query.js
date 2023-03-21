
$(document).ready(function(e) {
    $('#book_search_form').on("submit", submitHandler);
    $('#filter_search_form').on("input", submitHandler);
    $('#filter_search_form').on("submit", submitHandler);
    $('#sort_form').on("input", submitHandler);
    submitHandler(null); // Load in results initially

    collapseAllFilterboxes();
    $('.filter_box h2').on("click", function (e) {
        if (this.parentNode.contentsVisible) {
            collapseFilterbox(this.parentNode);
        } else {
            openFilterbox(this.parentNode);
        }
    });
});

function openFilterbox(elem) {
    elem.contentsVisible = true;
    $(elem).find('.collapsible').css({'display':'block'});
    $(elem).find('.open_indicator').html("&#9650");
}

function collapseFilterbox(elem) {
    elem.contentsVisible = false;
    $(elem).find('.collapsible').css({'display':'none'});
    $(elem).find('.open_indicator').html("&#9660");
    $(elem).find('input').val(""); // Reset input field when closed
}

function collapseAllFilterboxes() {
    var elements = $('.filter_box');
    for (var i=0; i<elements.length; i++) {
        collapseFilterbox(elements[i]);
    }
}

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

function searchField(field, value) {
    field = "#"+ field +"_query_field";
    $("#book_search_form")[0].reset();
    $("#filter_search_form")[0].reset();
    collapseAllFilterboxes();
    console.log($(field));
    openFilterbox($(field)[0].parentNode.parentNode);
    $(field).val(value);
    submitHandler(null);
}