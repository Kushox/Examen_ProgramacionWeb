
const cat_btn = document.getElementById('cat_btn');
const cat_result = document.getElementById('cat_result');

cat_btn.addEventListener("click", function() {
  var XHR = new XMLHttpRequest();
  
  XHR.onreadystatechange = function() {
    if (XHR.readyState == 4 && XHR.status == 200) {
      cat_result.src = JSON.parse(XHR.responseText).file;  
    }
  }
  XHR.open("GET", "https://aws.random.cat/meow");
  XHR.send();
});


