import { debounce } from "./utils.js";

$(document).ready(function (e) {
  $("#book_search_form").on("submit", submitHandler);
  $("#filter_search_form").on("input", debounce(submitHandler, 200));
  $("#sort_form").on("input", submitHandler);
  submitHandler(null); // Load in results initially

  document.querySelectorAll(".dropdownCheckboxButton").forEach((dropdown) => {
    dropdown.onclick = dropDownClickHandler;
  });

  window.onresize = debounce(resizeHandler);
  resizeHandler(); // closes all dropdowns when window is resized to mobile size
});

function submitHandler(e) {
  if (e) {
    e.preventDefault();
  }
  var fields = [
    "general_query",
    // "genre_query",
    // "publisher_query",
    // "author_query",
    "max_radius_query",
    "postcode",
    "available_only",
    "sort",
  ];

  var data = { csrfmiddlewaretoken: csrftoken };
  console.log($("#available_only_field").is(":checked"));

  fields.forEach((field) => {
    if (field == "available_only") {
      data[field] = $("#available_only_field").is(":checked");
    } else {
      data[field] = $("#" + field + "_field").val();
    }
  });
  $("#valid_postcode").html("&#8634");
  $.ajax({
    type: "POST",
    url: "/bookShare/browse/",
    data: data,
    success: function (response) {
      // $("#book_search_form")[0].reset(); // Clear input field on search
      $("#results_container").html(response["results_container"]);
      if (response["valid_postcode"]) {
        $("#valid_postcode").html("&#10003");
      } else {
        $("#valid_postcode").html("&#10007");
      }
    },
  });
}

function searchAuthor(e, author) {
  e.preventDefault();
  $("#book_search_form")[0].reset();
  $("#filter_search_form")[0].reset();
  $("#author_query_field").val(author);
  submitHandler(null);
}

function dropDownClickHandler(e) {
  e.preventDefault();
  const { dropdownType, dropdownClass } = e.target.dataset;
  const dropdown = document.querySelector(`#${dropdownType}_${dropdownClass}`);
  if (dropdown) {
    dropdown.classList.toggle("hidden");
  }
}

function resizeHandler() {
  // closes all dropdowns when window is resized to mobile size
  const screenWidth = window.screen.width;
  if (screenWidth >= 768) {
    return;
  }
  const dropdownBtns = document.querySelectorAll(".dropdownCheckboxButton");
  dropdownBtns.forEach((dropdownBtn) => {
    const { dropdownType, dropdownClass } = dropdownBtn.dataset;
    const dropdown = document.querySelector(
      `#${dropdownType}_${dropdownClass}`
    );
    dropdown.classList.add("hidden");
  });
}
