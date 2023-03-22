function regenerate_items(instances) {
  if (instances.length == 0) {
    $("#results-container").html("No users found.");
    return;
  }
  $("#results-container").empty();
  instances.forEach((user) => {
    var username = user.username;
    var image_url = user.image_url;
    $("#results-container").append(`
    <div class="shadow-md rounded-lg ">
    <a class="w-full block relative h-[250px] bg-gray-50 rounded-t-lg"
    href="/bookShare/${username}/profile/">
        <img class="absolute top-0 left-0 w-full h-full object-contain z-0"
        src='${
          image_url != "none" ? image_url : "/static/images/default_pfp.jpg"
        }'/>
    </a>
    <div class="px-5 py-4 relative">
        <a class="block font-semibold text-xl mb-1"
           href="/bookShare/${username}/profile/">${username}</a>
        <p class="text-gray-600">${user.location}</p>
    </div>
</div>`);
  });
}

$(document).ready(function () {
  $("#user-search-input").on("input", function (e) {
    e.preventDefault();
    var username = $(this).val();
    $.ajax({
      type: "POST",
      url: "/bookShare/search/",
      data: { username: username, csrfmiddlewaretoken: csrftoken },
      success: function (response) {
        var instances = response["instances"];
        regenerate_items(instances);
      },
    });
  });

  $("#user_search_form").on("submit", function (e) {
    e.preventDefault();
  });

  // Get all at start
  $.ajax({
    type: "POST",
    url: "/bookShare/search/",
    data: { username: "", csrfmiddlewaretoken: csrftoken },
    success: function (response) {
      var instances = response["instances"];
      regenerate_items(instances);
    },
  });
});
