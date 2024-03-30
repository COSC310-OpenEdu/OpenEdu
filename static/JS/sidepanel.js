let currentPage = "";

function openPanel() {
    document.getElementById("courseSidepanel").style.width = "250px";
    document.getElementById("course").classList.add("active");

    if (document.getElementById("home").classList.contains("active")) {
        currentPage = "home";
        document.getElementById("home").classList.remove("active");
    } else if (document.getElementById("search").classList.contains("active")) {
        currentPage = "search";
        document.getElementById("search").classList.remove("active");
    } else {
        currentPage = "course";
    }
  }
  
  function closePanel() {
    document.getElementById("courseSidepanel").style.width = "0";
    if (currentPage != "course") {
        document.getElementById("course").classList.remove("active");
        document.getElementById(currentPage).classList.add("active");
    }
  }