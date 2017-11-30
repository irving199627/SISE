$( document ).ready(function() {
  $(".button-collapse").sideNav();
});

  $(document).ready(function(){
    $('.carousel').carousel();
  });



  $(document).ready(function() {
var options = [{
  selector: '#staggered-test',
  offset: 300,
  callback: function(el) {
    Materialize.showStaggeredList($(el));
  }
}, {
  selector: '#image-test',
  offset: 300,
  callback: function(el) {
    Materialize.fadeInImage($(el));
  }
}];

Materialize.scrollFire(options);
});
