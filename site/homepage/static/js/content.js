col_resize = function(){
    var h= $('#rg_grid').outerHeight();
	console.log(h);
	$('#sk_content').height(h+100);
};

$(window).load(col_resize);
$(window).resize(col_resize);