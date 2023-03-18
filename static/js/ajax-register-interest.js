
$(document).ready(function() {
    $('#change-follow-button').on("click", function(e) {
        e.preventDefault();
        $.ajax( {
            type: 'POST',
            url: `/bookShare/${username}/${(isFollowing ? "unfollow/" : "follow/")}`,
            data: {"csrfmiddlewaretoken":csrftoken},
            success: function (response) {
                isFollowing = !isFollowing
                $('#change-follow-button').text((isFollowing ? "Unfollow" : "Follow"))
                $("#follower-count").text(`Followers: ${response["follow_count"]}`);
            }
        })
    });
});
    