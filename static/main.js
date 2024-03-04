
function getCookie(c_name) {
    var i,x,y,ARRcookies=document.cookie.split(";");
    for (i=0;i<ARRcookies.length;i++){
       x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
       y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
       x=x.replace(/^\s+|\s+$/g,"");
       if (x==c_name) {
         return unescape(y);
       }
    }
 }
 function setCookie(c_name,value,exdays) {
    var exdate=new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
    document.cookie=c_name + "=" + c_value;
 }

 function checkForm() {
    // Assuming there are two inputs with IDs 'input1' and 'input2'
    var input1 = document.getElementById('id_search_origin').value;
    var input2 = document.getElementById('id_searchstate_origin').value;
    var input3 = document.getElementById('id_search_destination').value;
    var input4 = document.getElementById('id_searchstate').value;

  
    if (input1 === '' && input2 === '' && input3 === '' && input4 === '') {
      // Prevent form submission if all fields are empty
      alert('Please fill in the search fields.');
      return false;
    } 
    
    else if (input1.toLowerCase() === 'elon musk' || input2.toLowerCase() === 'elon musk' || input3.toLowerCase() === 'elon musk' || input4.toLowerCase() === 'elon musk') {
      // Show popup if the search is for 'Elon Musk'
      alert("He's not here.");
      return false;
    }

    return true; // Proceed with form submission if validation passes
  }
  
  // Use this function on the page load to check for the cookie and redirect if necessary
  function checkFirstVisit() {
    var visited = getCookie('visited');
    if (visited !== 'true') {
      // If the cookie doesn't exist, it's the user's first visit
      setCookie('visited', 'true', 365); // Save a cookie for 365 days
      window.location.href = '/'; // Redirect to the splash page
    }
  }
  
  // Call this function when the page loads
  window.onload = checkFirstVisit;

  
  
 