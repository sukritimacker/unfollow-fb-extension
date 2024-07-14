chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "unlike" || request.action === "unfollow") {
      fetch('http://localhost:5000/perform_action', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({action: request.action, url: window.location.href}),
      })
      .then(response => response.text())
      .then(data => console.log(data))
      .catch((error) => console.error('Error:', error));
    }
  });