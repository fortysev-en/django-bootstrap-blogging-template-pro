window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (currentScrollPos > 300) {
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-50px";
    }
  }