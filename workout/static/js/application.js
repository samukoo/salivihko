//gymlog application.js.  jQueryt 


/*Liike listasta poimitaan data muuttujaan valittu valinta. 
Tämän jälkeen muuttuja injektoidaan id="exercise" -elementtiin
*/
$('#liike').on('click',function()
{
var data = $('#liike :selected').text();
jQuery("#exercise").text(data);
});


/*"button.send" click. POST funktio. Tähän täytyy kaivaa 
cookiesta csrf -token joka vaaditaan POST bodyssä. 
*/
$("#send_set").on('click',function()
	{
	var _toistot = parseInt(jQuery("#rep").text());
	var _kilot = parseInt(jQuery("#kg").text());
	var _liike = jQuery("#exercise").text();
	var _pvm = jQuery("#pvm").text();
	var csrftoken = $.cookie('csrftoken');
	$.post( "/gymlog/save/", { 	csrfmiddlewaretoken: csrftoken, 
								toistot: _toistot, 
								kilot: _kilot,
								liike: _liike,
								date: _pvm})
		.always(function( data ){
			alert(data);
		});

	});

//*************************************************************
//Tämä on toistojen asettamiselle
//"button.inc_rep" click increment funktio.  
$("#inc_rep").on('click',function()
{
var _kg = parseFloat(jQuery(".rep").text()); //"rep" -class tägin sisällä oleva numero intiksi
jQuery(".rep").text(_kg+1);
}
);


//"button.dec_rep"click decrement funktio
$("#dec_rep").on('click',function()
{
var _kg = parseFloat(jQuery(".rep").text());
jQuery(".rep").text(_kg-1);
}
);

//************************************************************

//"button.inc" click increment funktio. Tämä on kilojen säätämiselle 
$("#inc_kg").on('click',function()
{
var _kg = parseFloat(jQuery(".kg").text()); //"kg" -class tägin sisällä oleva numero intiksi
jQuery(".kg").text(_kg+2.5);
}
);


//"button.dec"click decrement funktio
$("#dec_kg").on('click',function()
{
var _kg = parseFloat(jQuery(".kg").text());
jQuery(".kg").text(_kg-2.5);
}
);

