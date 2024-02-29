// Add this JavaScript code to your HTML file, preferably just before the closing </body> tag.

// script.js

// Function to toggle the visibility of the "Scroll to Top" button
function toggleScrollToTopButton() {
    const scrollToTopButton = document.getElementById("scrollToTopButton");
    const aboutSection = document.getElementById("about");

    if (window.scrollY > aboutSection.offsetTop) {
        scrollToTopButton.style.display = "block";
    } else {
        scrollToTopButton.style.display = "none";
    }
}

// Function to scroll back to the top when the button is clicked
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth" // Smooth scrolling effect
    });
}

// Event listener to handle scroll and button click
document.addEventListener("DOMContentLoaded", function () {
    const scrollToTopButton = document.getElementById("scrollToTopButton");
    
    // Check the scroll position and toggle the button initially
    toggleScrollToTopButton();
    
    // Add a scroll event listener to toggle the button while scrolling
    window.addEventListener("scroll", toggleScrollToTopButton);

    // Add a click event listener to scroll back to the top when the button is clicked
    scrollToTopButton.addEventListener("click", scrollToTop);
});
