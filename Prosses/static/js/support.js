$(document).ready(function() {
    	var par = $('h4');
    	$(par).hide();
    	$("button").click(function() {
       		$(par).toggle();
       		var username = $("#name").val();
       		var password_user = $("#password").val();
       		var gender = $("#jenis_kelamin").val();
       		var alamat = $("#address").val();
       		var regex = /^[A-Z][a-z0-9_-]{5,15}$/;
       		if(username != "" && password_user != "" && gender != "" && alamat != ""){
       			if(!regex.test(username)){
       				$("h4").hide()
       				$("#comment").html("<span style='color:red;'>Huruf awal besar</span>")
       			return false
       			}
       		}else{
       			$("h4").hide()
       			$("#msg").html("<span style='color:red;'>Lengkapi form</span>")
       		}
    	});
	});