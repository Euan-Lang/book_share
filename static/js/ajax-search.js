
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
                    $("#results-container").html("No users found.");
                    return;
                }
                $("#results-container").empty();
                instances.forEach((user) => {
                    var username = user.username;
                    var image_url = user.image_url;
                    $("#results-container").append(`
                    <div class="transition-colors transition-transform hover:bg-[rgb(51,121,252)] hover:translate-y-1 hover:text-white bg-white shadow-lg rounded-xl h-[150px] w-[120px] lg:h-[200px] lg:w-[160px]">
                        <a href="/bookShare/${username}/profile/">
                            <img class="bg-white rounded-xl w-full h-4/5" src='${image_url ? image_url : "/static/images/default_pfp.jpg"}'/>
                            <div class="text-center align-middle sm:text-lg mt-1"> <b>${username}</b> </div>
                        </a>
                    </div>`)
                })
            }
        })
    });
});
    