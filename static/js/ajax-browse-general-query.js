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
    "max_radius_query",
    "postcode",
    "available_only",
    "following_only",
    "mine_only",
    "reserved_for_me_only",
    "sort",
  ];

  var checkboxFields = ["genres", "publishers", "authors"];

  var data = { csrfmiddlewaretoken: csrftoken };
  fields.forEach((field) => {
    if (field == "available_only") {
      data[field] = $("#available_only_field").is(":checked");
    } else if (field == "following_only") {
      data[field] = $("#following_only_field").is(":checked");
    } else if (field == "mine_only") {
      data[field] = $("#mine_only_field").is(":checked");
    } else if (field == "reserved_for_me_only") {
      data[field] = $("#reserved_for_me_only_field").is(":checked");
    } else if (field == "postcode") {
      // If postcode is empty, set to placeholder
      if ($("#postcode_field").val() == "") {
        data[field] = $("#postcode_field").attr("placeholder");
      } else {
        data[field] = $("#postcode_field").val();
      }
    } else {
      data[field] = $("#" + field + "_field").val();
    }
  });

  var checkboxReturns = {};
  checkboxFields.forEach((field) => {
    document
      .querySelectorAll("#" + field + "_dropdownCheckbox input")
      .forEach((box) => {
        if (box.checked == true) {
          if (!(field in checkboxReturns)) {
            checkboxReturns[field] = [];
          }
          checkboxReturns[field].push(box.value);
        }
      });
  });

  data["checkbox_queries"] = JSON.stringify(checkboxReturns);

  $("#valid_postcode").html("&#8634");
  $.ajax({
    type: "POST",
    url: "/bookShare/browse/",
    data: data,
    success: function (response) {
      $("#results_container").html(response["results_container"]);
      const postcodeInput = document.querySelector("#postcode_field");
      const postcodeLabel = document.querySelector("#postcode_label");
      if (response["valid_postcode"]) {
        postcodeInput.classList.remove("invalid");
        postcodeInput.classList.add("valid");
        postcodeLabel.textContent = "Postcode: (valid)";
      } else {
        postcodeLabel.textContent = "Postcode: (invalid)";
        postcodeInput.classList.remove("valid");
        postcodeInput.classList.add("invalid");
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
