// gcmtest.js

// Initialize slide index
var slideIndex = 0;

// Function to show slides
function showSlides() {
    var slides = document.getElementsByClassName("slide");
    
    // Hide all slides
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    
    // Increment slide index
    slideIndex++;
    
    // Reset slide index if it exceeds the number of slides
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    
    // Display the current slide
    slides[slideIndex - 1].style.display = "block";
}

// Function to show previous slide
function prevSlide() {
    var slides = document.getElementsByClassName("slide");
    
    // Decrement slide index
    slideIndex--;
    
    // Reset slide index if it goes below 1
    if (slideIndex < 1) {
        slideIndex = slides.length;
    }
    
    // Hide all slides
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    
    // Display the current slide
    slides[slideIndex - 1].style.display = "block";
}

// Function to show next slide
function nextSlide() {
    var slides = document.getElementsByClassName("slide");
    
    // Increment slide index
    slideIndex++;
    
    // Reset slide index if it exceeds the number of slides
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    
    // Hide all slides
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    
    // Display the current slide
    slides[slideIndex - 1].style.display = "block";
}

// Call the showSlides function to start the slideshow
showSlides();
