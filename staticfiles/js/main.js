window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (currentScrollPos > 300) {
      document.getElementById("navbar").style.top = "0";
    } else {
      document.getElementById("navbar").style.top = "-55px";
    }
  }

  $(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

function toggleParticles(event){
  var element = document.querySelector('.particles-js-canvas-el'),
  style = window.getComputedStyle(element),
  particleState = style.getPropertyValue('display');
  console.log(particleState)
  if (particleState == 'none'){
    element.style.display = 'block';
    // document.querySelector('.btn-toggle').innerHTML = 'Hide Particles'
  }
  else if (particleState == 'block'){
    element.style.display = 'none';
    // document.querySelector('.btn-toggle').innerHTML = 'Show Particles'
  }
  
}