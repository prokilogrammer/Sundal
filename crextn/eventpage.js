

function annotate(response)
{
  // Respnose is a map from link to the score

  // sample map
  response = {"http://www.google.com": 0.1, "http://www.yahoo.com":0.2}
  
  for key, value in response
  {
    $("a[href="+key+"]").title += "\nScore: " + value;
  }

}


function annotateLinks(pageurl)
{
  $.ajax({
    url: "http://localhost:5000/api/v1/linkscore",
    data: {'url': pageurl},
    success: funciton(data) { annotate(data); },
    dataType: "json"
  });
}

// Respond to click on extension icon
chrome.browserAction.onClicked.addListener(function(tab) {

  // Register event to run after a page has completed loading
  chrome.webNavigation.onCompleted.addListener(function(tab) {
    annotateLinks(tab.url);
  });


});


