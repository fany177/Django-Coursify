$(document).ready(function() {
	var pathname = window.location.pathname;
	$('.navbar-nav > li >  a[href="'+pathname+'"]').css({'border-bottom':'.3rem solid #F50057'});
})

var back1 = $('.exercise .exercise__content .exercise__content--back')
var next1 = $('.exercise .exercise__content .exercise__content--next')
var chips1 = $('.exercise .exercise__content .chips .chips__box')
var chips__width1 = parseInt($('.exercise .exercise__content .chips .chips__box .chips__box--item').css('width')) + parseInt($('.exercise .exercise__content .chips .chips__box').css('column-gap'))

back1.on('click',function (event){
   event.preventDefault();
   chips1.animate({
      scrollLeft: `-=${chips__width1+22}`
    }, "slow");
})

next1.on('click',function (event){
   event.preventDefault();
   chips1.animate({
      scrollLeft: `+=${chips__width1+22}`
    }, "slow");
})

var back2 = $('.maths .maths__content .maths__content--back')
var next2 = $('.maths .maths__content .maths__content--next')
var chips2 = $('.maths .maths__content .chips .chips__box')
var chips__width2 = parseInt($('.maths .maths__content .chips .chips__box .chips__box--item').css('width')) + (parseInt($('.science .science__content .chips .chips__box').css('column-gap')))

back2.on('click',function (event){
   event.preventDefault();
   chips2.animate({
      scrollLeft: `-=${chips__width2}`
    }, "slow");
})

next2.on('click',function (event){
   event.preventDefault();
   chips2.animate({
      scrollLeft: `+=${chips__width2}`
    }, "slow");
})

var back3 = $('.science .science__content .science__content--back')
var next3 = $('.science .science__content .science__content--next')
var chips3 = $('.science .science__content .chips .chips__box')
var chips__width3 = parseInt($('.science .science__content .chips .chips__box .chips__box--item').css('width')) + parseInt($('.science .science__content .chips .chips__box').css('column-gap'))


back3.on('click',function (event){
   event.preventDefault();
   chips3.animate({
      scrollLeft: `-=${chips__width3}`
    }, "slow");
})

next3.on('click',function (event){
   event.preventDefault();
   chips3.animate({
      scrollLeft: `+=${chips__width3}`
    }, "slow");
})

var back4 = $('.viewed .viewed__content .viewed__content--back')
var next4 = $('.viewed .viewed__content .viewed__content--next')
var chips4 = $('.viewed .viewed__content .chips .chips__box')
var chips__width4 = parseInt($('.viewed .viewed__content .chips .chips__box .chips__box--item').css('width'))


back4.on('click',function (event){
   event.preventDefault();
   chips4.animate({
      scrollLeft: `-=${chips__width4+19}`
    }, "slow");
})

next4.on('click',function (event){
   event.preventDefault();
   chips4.animate({
      scrollLeft: `+=${chips__width4+19}`
    }, "slow");
})

var back5 = $('.need .need__content .need__content--back')
var next5 = $('.need .need__content .need__content--next')
var chips5= $('.need .need__content .chips .chips__box')
var chips__width5 = parseInt($('.need .need__content .chips .chips__box .chips__box--item').css('width'))


back5.on('click',function (event){
   event.preventDefault();
   chips5.animate({
      scrollLeft: `-=${chips__width5+64.5}`
    }, "slow");
})

next5.on('click',function (event){
   event.preventDefault();
   chips5.animate({
      scrollLeft: `+=${chips__width5+64.5}`
    }, "slow");
})

if($('.navbar-toggler-icon').is(':visible')){
   $('.navbar').addClass('navbar-dark bg-primary')
}