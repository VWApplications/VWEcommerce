$(document).ready(function(){
  $('.parallax').parallax();
  $(".button-collapse").sideNav();
  $('.collapsible').collapsible();
  $(".dropdown-button").dropdown({
    hover: true,
    belowOrigin: true,
  });
  $('.tooltipped').tooltip({
    delay: 50,
    position: "left",
  });
  $('.modal').modal({
    dismissible: true,
    opacity: .5,
    in_duration: 300,
    out_duration: 200,
  });
});
