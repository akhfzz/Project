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
function populateSelect() {
        // THE JSON ARRAY.
        var mydata = JSON.parse(provinsi);
        var ele = document.getElementById('daerah');
        for (var i = 0; i < mydata.length; i++) {
        // POPULATE SELECT ELEMENT WITH JSON.
            ele.innerHTML = ele.innerHTML +
                '<option value="' + mydata[i]['id'] + '">' + mydata[i]['nama'] + '</option>';
        }
     }
function show(ele) {
        // GET THE SELECTED VALUE FROM <select> ELEMENT AND SHOW IT.
        var msg = document.getElementById('did');
        msg.innerHTML = 'Selected city: <b>' + ele.options[ele.selectedIndex].text + '</b> </br>' +
            'ID: <b>' + ele.value + '</b>';
    }
function myFile(){
    var file = document.createElement("INPUT");
    file.setAttribute("type","file");
    document.body.appendChild(file);
}