$(document).ready(function() {
    setInterval(function(){  
        $.getJSON("get_sensor_data",function(result){
            $('#temperature').text(Math.round(result['temperature']*100)/100 + "°C")
            $('#humidity').text(Math.round(result['humidity']*100)/100 + "%")
            $('#health').text(Math.round(result['health']*100)/100 )
            $('#speed').text(Math.round(result['speed']*100)/100)

            var speed = result['speed'] 
            if(speed > 5) 
                $("#state").text("running")
            else if (speed <= 5 && speed > 1)
                $("#state").text("walking")
            else
                $("#state").text("standing")
            
            var health=result['health']
            if(health < 7)
                $("#state2").text("bad")
            else if (health >=7 && health<8)
                $("#state2").text("not bad")
            else if (health <=8)
                $("#state2").text("good")
            else if(health<= 9)
                $("#state2").text("health")
            else if(health <=10)
                $("#state2").text("very health")
        });    
    }, 3000);
});

