---
layout: default
name: "UX - Survey - Repeat"
position: "About/UX"
sidebarRoot: User Experiance
sidebarRootURL: ../UX_MicroSite-Home
masthead: MicroSite/heroimage.micro.ux.html
---
<div style="display:grid; place-items: center;">
<h1>Random Survey</h1>
<button id="randomUrlButton">Start Survey</button>
<script>
    document.addEventListener('DOMContentLoaded', function() {
    const urls = [
        "K78YLPR",
        "KV77ZKH",
        "LZ5YGPL",
        "LNSW26V",
        "SMXHDQS",
        "K9VY6BJ",
    ];
    const baseURL = "https://www.surveymonkey.com/r/";
    // Function to navigate to a random URL
    function goToRandomURL() {
          // Generate a random index to select a random URL from the array
          const randomIndex = Math.floor(Math.random() * urls.length);
    const randomURL = urls[randomIndex];
    // Construct the full URL
    const fullURL = baseURL + randomURL;

    // Navigate to the random URL
    window.location.href = fullURL;
      }

    // Add event listener to the button
    const randomUrlButton = document.getElementById('randomUrlButton');
    randomUrlButton.addEventListener('click', goToRandomURL);
  }
    );
</script>
</div>

