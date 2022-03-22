const hamburgerIcon = $(".hamburger-icon");
const mobileNavBar = $(".nav-items > ul");
const navBarElements = $(".nav-items a");
var isHamburgerClicked = false;

const handleHamburgerClick = () => {
  if (!isHamburgerClicked) {
    hamburgerIcon.removeClass("fa-bars");
    hamburgerIcon.addClass("fa-bars-staggered");
    mobileNavBar.css({
      transform: "translateY(0%)",
    });
    isHamburgerClicked = true;
  } else {
    hamburgerIcon.addClass("fa-bars");
    hamburgerIcon.removeClass("fa-bars-staggered");
    isHamburgerClicked = false;
    mobileNavBar.css({
      transform: "translateY(-100%)",
    });
  }
};

hamburgerIcon.click(handleHamburgerClick);

const postImageUploadBtn = $("#image-upload-icon");
const imageUploadElement = $("#image-upload");

postImageUploadBtn.click(() => {
  imageUploadElement.click();
});

imageUploadElement.change((e) => {
  $(".uploaded-file-text").text(e.target.files[0].name);
});

if (window.location.pathname == "/") {
  $("nav").add(navBarElements).css({
    color: "white",
  });
}
