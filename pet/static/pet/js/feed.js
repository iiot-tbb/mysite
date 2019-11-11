$(document).ready(function() {
    $( "#feed-btn" ).click(function() {
        $.getJSON("feed",function(result){
           // alert(result);
        }); 
      });
});

