img_resize = function(){
    var w = $('.wrap-image').width();
	$('.wrap-image').height(w);
	$('.preview-image').height(w);
};

$(window).resize(img_resize);
$(document).ready(img_resize);