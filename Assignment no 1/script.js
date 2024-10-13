// Function to smooth scroll to different sections of the page
document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll("nav ul li a");

    navLinks.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault(); // Prevent default anchor click behavior

            const targetId = this.getAttribute("href"); // Get the target section ID
            const targetSection = document.querySelector(targetId); // Select the target section

            // Smooth scroll to the target section
            targetSection.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        });
    });
});

// Optional: Change header background on scroll
window.addEventListener("scroll", function() {
    const header = document.querySelector("header");

    if (window.scrollY > 50) {
        header.style.backgroundColor = "#222"; // Darker background when scrolled
    } else {
        header.style.backgroundColor = "#333"; // Original background color
    }
});