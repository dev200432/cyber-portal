document.addEventListener('DOMContentLoaded', function() {
    console.log("🔒 Cyber Security Workshop Portal Loaded Successfully!");

    // Add interactive feedback on form submission buttons
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerText = "Processing & Sending Email...";
                submitBtn.classList.add('disabled');
            }
        });
    });
});