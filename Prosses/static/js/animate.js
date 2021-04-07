$(document).ready(function(){
	var eks = $("#form");
	var teks = $(".word");
	$(teks).hide();
	$(eks).hide();
	$("#login").click(function(){
		$(eks).animate({
			height: "toggle"
		});
	});
	$("#register").click(function(){
		$(teks).animate({
			height: "toggle"
		});
	});
});