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
	$(".clickableRow").click(function() {
	    window.document.location = $(this).data("href");
	});	
	/**
	 * Observation table sorter
	*/
    var table = $(".observationList");

    //Make head header in the THEAD sortable.
    $("thead th", table).on("click", onSortableClicked);

    //Handle the sortable clicked event.
    function onSortableClicked(e) {
        //Find the column position.
        var c = -1, child = e.target, order;
        while ((child = child.previousSibling) != null)
            if (child.nodeType == 3) ++c;

        //Find the row position.
        var r = -1, child = e.target.parentNode;
        while ((child = child.previousSibling) != null)
            if (child.nodeType == 3) ++r;


        var subject = $("tbody", table);
        
        
        if ($(e.target).hasClass("asc")){
        	order = "desc";
        }else{
        	order = "asc";
        }
        var replacement = sort(subject, r, c, order);

        $("thead th", table).removeClass("asc").removeClass("desc");
        
        $(e.target).addClass(order);

        subject.replaceWith(replacement);
    }

    function sort(subject, r, c, order) {
        var rows = $("tr", subject); //Get all the rows from the tbody.
        var sorted = document.createElement("tbody");

        var vals = [];
        for (var i = 0; i < rows.length; i+=2) {
            var record = [rows.get(i), rows.get(i+1)]; //Record is two rows.

            if ($(record[r].children[c]).data("sorter") != undefined){
            	var sub = $(record[r].children[c]).data("sorter");
            }else {
            	var sub = record[r].children[c].innerText; //This is our sort subject.
            }
            
            vals.push({"sub": sub, "record": record});
        }
        if (order == "asc"){
        	vals.sort(compare);
        }else{
        	vals.sort(reverseCompare);
        }

        for (var i = 0; i < vals.length; ++i) {
            var val = vals[i];
            sorted.appendChild(val.record[0]);
            sorted.appendChild(val.record[1]);
        }

        return sorted;
    }

    function compare(a, b) {
        var atext = a.sub.toLowerCase();
        var btext = b.sub.toLowerCase();
        return atext < btext ? -1 : atext > btext ? 1 : 0;
    }	
    function reverseCompare(a, b) {
        var atext = a.sub.toLowerCase();
        var btext = b.sub.toLowerCase();
        return atext > btext ? -1 : atext < btext ? 1 : 0;
    }	  
    $("tbody tr", table).hover(onRowHoverIn, onRowHoverOut);   
    function onRowHoverIn(e){
    	var subject = $("tbody", table);
        var r = -1, child = e.target.parentNode;
        while ((child = child.previousSibling) != null)
            if (child.nodeType == 3) ++r;    
		
		var rows = $("tr", subject);

		$(rows.get(r)).addClass("hover");
		if (r % 2){
			$(rows.get(r - 1)).addClass("hover");
		}else{
			$(rows.get(r + 1)).addClass("hover");		
		}
    }   
    function onRowHoverOut(e){
    	var subject = $("tbody", table);
        var r = -1, child = e.target.parentNode;
        while ((child = child.previousSibling) != null)
            if (child.nodeType == 3) ++r;    
		
		var rows = $("tr", subject);

		$(rows.get(r)).removeClass("hover");
		if (r % 2){
			$(rows.get(r - 1)).removeClass("hover");
		}else{
			$(rows.get(r + 1)).removeClass("hover");			
		}
    }     
});