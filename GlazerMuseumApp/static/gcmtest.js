// Image SLider
const slides = document.querySelectorAll(".slides img");
let slideIndex = 0
let IntervalId = null;

//Initialize Slider
document.addEventListener("DOMContentLoaded", initializeSlider);


function initializeSlider(){
    if(slides.length > 0){
        slides [slideIndex].classList.add("displaySlide");
        IntervalId = setInterval(nextSlide, 5000);
}

}
function showSlide(index) {

    if(index >= slides.length){
        slideIndex = 0;

    }
    else if (index < 0){
        slideIndex = slides.length - 1
    }
    slides.forEach(slide => { 
        slide.classList.remove("displaySlide");
    });
    slides[slideIndex].classList.add("displaySlide");

}
function prevSlide(){
    clearInterval(IntervalId);
    slideIndex--;
    showSlide(slideIndex);

}
function nextSlide(){
    slideIndex++;
    showSlide(slideIndex);

}
function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}