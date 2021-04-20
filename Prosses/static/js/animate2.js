$(document).ready(function(){
	var animate = $(".navbar");
	$(animate).hide();
	$("#navbarDropdown").click(function(){
		$(animate).animate({
			height: "toggle",
		});
	});
});
// $(document).ready(function(){
//     var animate = $(".animated-gift");
//     $(animate).hide();
//     $(".btn-primary").click(function(){
//         $(animate).animate({
//             height: "toggle",
//         });
//     });
// });
function show() {
        var txt, data, i
	txt = "<select>";
	data = JSON.parse(provinsi);
	for (i = 0; i < data.length; i++){
	txt += "<option value = " +  data[i]["id"] + ">" + data[i]['nama'] + '</option>'
	};
	txt += "</select>"
	document.getElementById("daerah").innerHTML = txt
    }
function myFile(){
    var file = document.createElement("INPUT");
    file.setAttribute("type","file");
    document.body.appendChild(file);
}
