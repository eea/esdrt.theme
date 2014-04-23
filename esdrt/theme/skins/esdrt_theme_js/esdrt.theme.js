$(document).ready(function(){
	$("#showObservationDetails").click(function(e){
		$(".observationDetailsRow").toggle();
		if ($("#showObservationDetails").text() == "[+]"){
			$("#showObservationDetails").text("[-]");
		}else{
			$("#showObservationDetails").text("[+]");
		}
		return false;
	});
});