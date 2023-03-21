var hidden = true;
$(document).ready(function () {
  $("#change-interest-button").on("click", function (e) {
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: `/bookShare/book/${bookId}/${
        isInterested ? "remove_interest/" : "add_interest/"
      }`,
      data: { csrfmiddlewaretoken: csrftoken },
      success: function (response) {
        isInterested = !isInterested;
        $("#change-interest-button").text(
          isInterested ? "Remove Interest" : "Register Interest"
        );
      },
    });
  });
});
