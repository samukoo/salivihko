//gymlog application.js. jQueryt (

$('#aioConceptName').on('click',function()
{
var data = $('#aioConceptName :selected').text();
jQuery(".testi").text(data);
});

//jQuery("#huoh").text(data);



      




//"button.send" click. POST funktio. Tähän täytyy kaivaa 
//cookiesta csrf -token joka vaaditaan POST bodyssä. 


$("#post_send").on('click',function()
	{
	var _toistot = parseInt(jQuery(".kg").text());
	var csrftoken = $.cookie('csrftoken');
	$.post( "/gymlog/save/", { csrfmiddlewaretoken: csrftoken , toistot: _toistot, date: "28.02.2014" }) 
		.done(function( data ) {
		jQuery(".post_response").text(data);

		setInterval(function(){
			var _hmm = ("testiresponse")
			jQuery(".post_response").text(_hmm)

		},10000);

});
});



//**************************************************************
//alasvetovalitsimen klikkailu, eli liikkeen valitsin
$("#Kyykky").on('click',function()
{
	$("#exercise").text("Kyykky");
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
var _kg = jQuery(".kg").text(); //"kg" -class tägin sisällä oleva numero intiksi
jQuery(".testi").text(data);
}
);


//"button.dec"click decrement funktio
$("#dec_kg").on('click',function()
{
var _kg = parseFloat(jQuery(".kg").text());
jQuery(".kg").text(_kg-2.5);
}
);