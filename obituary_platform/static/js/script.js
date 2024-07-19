// scripts.js

document.addEventListener('DOMContentLoaded', () => {
    // Example of adding an event listener for a button click
    const submitButton = document.querySelector('form button');
    
    if (submitButton) {
        submitButton.addEventListener('click', () => {
            alert('Form submitted!');
        });
    }
});
document.addEventListener("DOMContentLoaded", function() {
    // Example script: Show a confirmation before form submission
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        if (!confirm("Are you sure you want to submit this obituary?")) {
            event.preventDefault();
        }
    });

    // Additional JavaScript functionality can be added here
});
