const body = $("body");
const darkModeToggler = $("#darkmode-toggle");

// Post Page
const commentSubmitButton = $(".comment-submit-button");
const commentInputArea = $(".comment-type-area");

// Auth pages
const submitButton = $(".authformsubmit-btn");
const authFormInputs = $(".authentication-form input");

// Myaccount
const myaccountButtons = $(".myaccount-button-container");

darkModeToggler.click(() => {
  if (darkModeToggler.hasClass("fa-sun")) {
    darkModeToggler.removeClass("fa-sun").addClass("fa-moon");
    darkModeContent();
  } else {
    darkModeToggler.removeClass("fa-moon").addClass("fa-sun");
    whiteModeContent();
  }

  body.toggleClass("dark-mode");
});

const darkModeContent = () => {
  (commentInputArea, authFormInputs).css("color", "white");
  (commentSubmitButton, submitButton).css({
    color: "white",
    "background-color": "rgba(56, 56, 56, 0.473)",
    border: "none",
  });
};

const whiteModeContent = () => {
  (commentInputArea, authFormInputs).css("color", "black");
  (commentSubmitButton, submitButton).css({
    color: "#151616",
    "background-color": "rgb(214, 214, 214)",
    border: "1px solid rgb(194, 194, 194)",
  });
};
