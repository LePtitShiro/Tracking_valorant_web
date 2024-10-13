/* TODO: input id="tracker_input" récupérer la valeur */
/* TODO: quand on clique profil, on redirige vers /profil/username */

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

