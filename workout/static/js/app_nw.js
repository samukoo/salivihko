
$.getJSON("http://localhost:8080/search_date?date=13.03.2014",function(data){                
          var taulu = "<ul>";
            for( i=0 ; i < data.result.length ; i++ )
              {
                taulu += data.result[i].liike+ "<br>";
                  taulu += "<li>" + data.result[i].toistot + " x " + data.result[i].painot + "kg" + "<br>";
              }
              taulu += "</ul>";
          document.getElementById("viimeisin_treeni").innerHTML=taulu;
        });