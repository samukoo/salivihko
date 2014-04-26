

$.getJSON('http://localhost:8080/workouts', function(data) {
    	
    	var output="</ul>";

    	for(i=0;i<4;i++)
    	{	
    	output+= data.result[i].id+ ": " + data.result[i].workout+"<br>";
	    }
	    output+="</ul>";

document.getElementById("viimeiset_treenit").innerHTML=output;
});
