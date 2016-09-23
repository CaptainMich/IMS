fontsize = function () {
	var fontSize = $(".read-more").height()  * 0.7; // 10% of container width
	$(".read-more").css('font-size', fontSize);
};
$(window).resize(fontsize);
$(document).ready(fontsize);