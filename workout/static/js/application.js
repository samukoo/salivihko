//gymlog application.js. Palvelun jQueryt (c)Sauli Kotisaari


//var data = "moi"
//jQuery(".response").text(data);






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
//jQuery(".dropdown-menu").on('click',function(e)
//{
//	console.log(e.target.Id);
//});

//"button.inc" click increment funktio.  
$("#inc_rep").on('click',function()
{
var _kg = parseFloat(jQuery(".rep").text()); //"kg" -class tägin sisällä oleva numero intiksi
jQuery(".rep").text(_kg+1);
}
);


//"button.dec"click decrement funktio
$("#dec_rep").on('click',function()
{
var _kg = parseFloat(jQuery(".rep").text());
jQuery(".rep").text(_kg-1);
}
);





//"button.inc" click increment funktio.  
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

//*****************************************************************************


//Ajastin funktio. tekee jotain 2s välein.


//jQuery(function(){    
  //  setInterval(function(){ 								//Calls a function every X ms as specified in param 2
    //    var _nbr = parseInt(jQuery('h1').text());			//Get number from element as int
      //  jQuery('h1').text(++_nbr);							//Increment variable and puts it in the element
    //},2000);												//Number of ms between function calls
//});

//$('.send').on('click',function()
//{
//$.post( "/gymlog/save/", function( data ) 
//{
//$( ".result" ).html( data );
//});
//});
