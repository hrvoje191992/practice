$( document ).ready(function() {
    // Hero Section FUll Height
    $(function(){
    	var windowH = $(window).height();
    	var wrapperH = $('.hero').height();
    	if(windowH > wrapperH) {                            
    		$('.hero').css({'height':($(window).height())+'px'});
    	}
    	$(window).resize(function(){
    		var windowH = $(window).height();
    		var wrapperH = $('.hero').height();
    		var differenceH = windowH - wrapperH;
    		var newH = wrapperH + differenceH;
    		var truecontentH = $('#truecontent').height();
    		if(windowH > truecontentH) {
    			$('.hero').css('height', (newH)+'px');
    		}

    	})          
    });
});

function search() {
	if (!$('div#bannerDiv').hasClass('hidden')) {
		$('div#bannerDiv').addClass('hidden');
	}
	text = $('input#searchText').val()
	$.ajax({
		url: '/booking/api/hospitals',
		type: 'GET',
		success: function (result) {
			console.log(result);
			result.foreach((item, index) => {
				if (item.name.toLowerCase().includes(text.toLowerCase())) {
					console.log("Found");
				} else {
					console.log("Not Found");
				}
			});
		},
		error: function (error) {
			console.log(error);
		}
	});
}