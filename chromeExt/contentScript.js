function parseTask(message, sender, sendResponse) {
    if (sender.tab)
        return;
    var title
    if(message === 'codechef')
        title = document.getElementsByTagName("h1")[1].innerText.split('Problem Code')[0].trim();
    else if(message === 'hackerearth')
        title = document.getElementById("fullscreen-problem-title").innerText;
    // console.log(message+ "  " + title);
    chrome.runtime.sendMessage(title);
}

chrome.runtime.onMessage.addListener(parseTask);