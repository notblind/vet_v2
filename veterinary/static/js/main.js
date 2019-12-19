

var sections = $('section'), 
nav = $('nav'),
button = $('button');



nav.find('a').on('click', function () {
  var $el = $(this)
    , id = $el.attr('href')
    , offset = $(id).offset()
    , height_nb = $('#none-block').outerHeight();
  
  $('html, body').animate({
    scrollTop: offset.top + height_nb
  }, 1400);
  
  return false;
});


$(function(){
  $('button').click(function(){
    if($(this).hasClass("button-back")){
      var top = $('#topsc').offset().top;
      $('html, body').animate({scrollTop: top}, 800);
    }
  });
});




$( document ).ready(function(){
 $( "div" ).hover(function(){ // задаем функцию при наведении курсора на элемент 
   if($(this).hasClass("doc-box")){
      $(this).find('img').css( "opacity", "0.85" );
    }
   }, function(){ // задаем функцию, которая срабатывает, когда указатель выходит из элемента  
   if($(this).hasClass("doc-box")){
      $(this).find('img').css( "opacity", "1" );
    }
  });
});


$(window).on('scroll', function () {
  var cur_pos = $(this).scrollTop();
  
  button.each(function() {


    if (cur_pos >= 150) {
      $(".button-back").css( "opacity", "1" );
    }

    if (cur_pos < 150) {
      $(".button-back").css( "opacity", "0" );
    }

  });
});


