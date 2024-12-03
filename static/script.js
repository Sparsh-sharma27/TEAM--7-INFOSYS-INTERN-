const navbarMenu = document.querySelector(".navbar .links");
const hamburgerBtn = document.querySelector(".hamburger-btn");
const hideMenuBtn = navbarMenu.querySelector(".close-btn");
const showPopupBtn = document.querySelector(".login-btn");
const formPopup = document.querySelector(".form-popup");
const hidePopupBtn = formPopup.querySelector(".close-btn");
const signupLoginLink = formPopup.querySelectorAll(".bottom-link a");
const signupBtn = document.querySelector(".signup-btn");
const signupForm = formPopup.querySelector(".signup");

const loginBtn = document.querySelector(".login-btn");

const blurBg = document.querySelector(".blur-bg-overlay");



// Show mobile menu
hamburgerBtn.addEventListener("click", () => {
    navbarMenu.classList.toggle("show-menu");
});

// Hide mobile menu
hideMenuBtn.addEventListener("click", () =>  hamburgerBtn.click());

// Show login popup
showPopupBtn.addEventListener("click", () => {
    document.body.classList.toggle("show-popup");
});

// Hide login popup
hidePopupBtn.addEventListener("click", () => showPopupBtn.click());

// Show or hide signup form
signupLoginLink.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        formPopup.classList[link.id === 'signup-link' ? 'add' : 'remove']("show-signup");
    });
});

signupBtn.addEventListener("click", () => {
    formPopup.classList.add("show");
    document.querySelector(".form-box.signup").classList.add("show");
    document.querySelector(".blur-bg-overlay").classList.add("show");
});

// Add this to your existing JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const getStartedBtn = document.querySelector('.get-started-btn');
    
    getStartedBtn.addEventListener('click', () => {
        // Show signup form when "Get Started" is clicked
        const formPopup = document.querySelector(".form-popup");
        const blurBg = document.querySelector(".blur-bg-overlay");
        
        formPopup.classList.add("show");
        blurBg.classList.add("show");
        document.querySelector(".form-box.signup").style.display = "block";
        document.querySelector(".form-box.login").style.display = "none";
    });
});