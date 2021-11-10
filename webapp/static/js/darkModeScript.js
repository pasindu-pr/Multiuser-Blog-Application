const body = $("body");
const darkModeToggler = $("#darkmode-toggle");

// Post Page
const commentSubmitButton = $(".comment-submit-button");
const commentInputArea = $(".comment-type-area");

// Auth pages
const submitButton = $("#submit");
const authFormInputs = $(".authentication-form input");
const authFormSubmitButton = $(".authformsubmit-btn");
const postBodyInput = $(".postBodyInput");

// Myaccount
const myaccountButtons = $(".myaccount-button-container button");

darkModeToggler.click(() => {
  if (darkModeToggler.hasClass("fa-sun")) {
    darkModeToggler.removeClass("fa-sun").addClass("fa-moon");
    darkModeContent();
    localStorage.setItem("darkMode", true);
  } else {
    darkModeToggler.removeClass("fa-moon").addClass("fa-sun");
    whiteModeContent();
    localStorage.setItem("darkMode", false);
  }

  body.toggleClass("dark-mode");
});

const darkModeContent = () => {
  commentSubmitButton
    .add(submitButton)
    .add(myaccountButtons)
    .add(authFormSubmitButton)
    .add(postBodyInput)
    .add(commentInputArea)
    .css({
      color: "white",
      "background-color": "rgba(56, 56, 56, 0.473)",
      border: "none",
    });
};

const whiteModeContent = () => {
  commentSubmitButton
    .add(submitButton)
    .add(myaccountButtons)
    .add(authFormSubmitButton)
    .add(postBodyInput)
    .add(commentInputArea)
    .css({
      color: "#151616",
      "background-color": "rgb(214, 214, 214)",
      border: "1px solid rgb(194, 194, 194)",
    });
};

window.onload = () => {
  if (
    localStorage.getItem("darkMode") == "true" &&
    darkModeToggler.hasClass("fa-sun")
  ) {
    darkModeToggler.click();
  }
};
