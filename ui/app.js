function addVideo() {
    const videoUrl = document.getElementById('video-url').value;

    fetch('/add_video', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        updateVideoList();
    })
    .catch(error => console.error('Error:', error));
}

function updateVideoList() {
    // Code to update the video list dynamically
}
