/* TODO: input id="tracker_input" récupérer la valeur */

document.getElementById('tracker_form').addEventListener('submit', async function(e) {
    e.preventDefault();
    let tracker = document.getElementById('tracker_input').value;
/*    let response = await fetch('/api/trackers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({tracker: tracker})
    });
    let data = await response.json();
    if (data.error) {
        alert(data.error);
    } else {
        alert('Tracker ajouté');
    }*/
}