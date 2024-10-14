
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('tracker_form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const input = document.getElementById('tracker_input').value;
        if (input) {
            window.location.href = `/profil/${encodeURIComponent(input)}`;
        }
    });
});

document.getElementById("sign_up_button").addEventListener("click", function() {
    window.location.href = "/signup";
});

