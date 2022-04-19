$(document).ready( function () {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", 'https://api.quotable.io/random?tags=wisdom', false ); // false for synchronous request
    xmlHttp.send( null );
  
    let data = xmlHttp.responseText;
    let dataJSON = JSON.parse(data);
  
    document.getElementById('quoteOne').innerHTML = dataJSON.content
    document.getElementById('quoteOneAuthor').innerHTML = dataJSON.author
  });
  
  $(document).ready( function () {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", 'https://api.quotable.io/random?tags=famous-quotes', false ); // false for synchronous request
    xmlHttp.send( null );
  
    let data = xmlHttp.responseText;
    let dataJSON = JSON.parse(data);
  
    document.getElementById('quoteTwo').innerHTML = dataJSON.content
    document.getElementById('quoteTwoAuthor').innerHTML = dataJSON.author
  });
  
  $(document).ready( function () {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", 'https://api.quotable.io/random?minLength=100&maxLength=280', false ); // false for synchronous request
    xmlHttp.send( null );
  
    let data = xmlHttp.responseText;
    let dataJSON = JSON.parse(data);
  
    document.getElementById('quoteThree').innerHTML = dataJSON.content
    document.getElementById('quoteThreeAuthor').innerHTML = dataJSON.author
  });