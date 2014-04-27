
$.getJSON("http://localhost:8080/search_date?date=13.03.2014",function(data){                
        var taulu = "<ol>";
        var apu = ""; 
            for( i=0 ; i < data.result.length ; i++ )
            	{
            	if( data.result[i].liike == apu )
            		{
            		taulu += "<ol>" + data.result[i].toistot + " x " + data.result[i].painot + "kg" + "<br>";
            		}
            	else
            		{
            		apu = data.result[i].liike;
            		taulu += "<br>" + data.result[i].liike+ "<br>";
                  	taulu += "<ol>" + data.result[i].toistot + " x " + data.result[i].painot + "kg" + "</ol>";
            		}
       			}
            taulu += "</ol>";
          	document.getElementById("viimeisin_treeni").innerHTML=taulu;
        });