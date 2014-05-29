

var user = jQuery("#user").text();

$.getJSON('http://localhost:8080/workouts?user='+user, function(dates) {
    	
    	data=dates;
    	dates_NO_DOTS = JSON.stringify(dates).replace(/\./g,"_");
    	dates_NO_DOTS = JSON.parse(dates_NO_DOTS);
		
		var output="</ul>";
    	
        var length=data.result.length;

        if(length > 4)
        {
            length = "5";
        }

    	for(i=0; i < length ; i++)
    	{	
    	output+= data.result[i].id+ ": "+ "<a id='"+data.result[i].workout+	"' href='uusi_treeni/"+	dates_NO_DOTS.result[i].workout+	"'>"+ data.result[i].workout+"</a><br>";
	    }
	    output+="</ul>";

document.getElementById("viimeiset_treenit").innerHTML=output;
});

     