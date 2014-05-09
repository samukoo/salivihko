$.getJSON("http://localhost:8080/exercises",function(data){
//alert(data.result[0].liike);

	var valikko="";

	for(var i = 0; i < data.result.length; i++){

		valikko += "<option value=" + data.result[i].liike +"id=" + data.result[i].liike + ">" +data.result[i].liike+"</option>"
	}

	//valikko += "<option value=/add > Lisää uusi liike </option>"; 

	document.getElementById("liike").innerHTML=valikko;

});




																				
									
						
											
//id="{{ liike }}" >{{ liike }}</option>

//<option value="{{ liike }}" id="{{ liike }}" >{{ liike }}</option>
									
										
							