function showSearchForm() {
    const form = document.getElementById("navbar-search-main");
    form.style.display = "block";
  }
  
  function hideSearchForm() {
    const form = document.getElementById("navbar-search-main");
    form.style.display = "none"; 
  }
  
  function init() {
    // Get current URL
    const currentURL = window.location.pathname;
    
    if (currentURL === '/map.html') {
      // Show form for map page
      showSearchForm();
    } else {  
      // Hide form for other pages
      hideSearchForm();  
    }
  }
  
  init();