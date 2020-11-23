$(document).ready(function() {
	
	var pathname = window.location.pathname;
	$('.navbar-nav > li >  a[href="'+pathname+'"]').css({'border-bottom':'.3rem solid #F50057'});

	if(pathname == '/profile/' || pathname == '/welcome/'){
		$('#section-footer1').hide()
	}

	if(pathname == '/drop/'){
		$('.navbar').hide()
		$('#section-footer1').hide()
	}

})

if($('.navbar-toggler-icon').is(':visible')){
   $('.navbar').addClass('navbar-dark bg-primary')
}

