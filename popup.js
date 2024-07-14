document.getElementById('unfollowPages').addEventListener('click', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, {action: "unfollow"}, function(response) {
        document.getElementById('status').textContent = "Unfollowing pages...";
      });
    });
  });