col_resize = function(){
	var window_h = $(window).height();
	//console.log(window_h);
	
    if($('#rg_grid').length) { //if it exists
		var h= $('#rg_grid').outerHeight();
		if(window_h < h) {
			$('#sk_content').height(h+100);
			console.log(h);
		}
	}
};

$(window).load(col_resize);
$(window).resize(col_resize);