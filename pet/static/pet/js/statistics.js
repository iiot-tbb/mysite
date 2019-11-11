$(document).ready(function() {
    var myChart = echarts.init(document.getElementById('mainchart'));

	// 指定图表的配置项和数据
	var option = {
		title: {
			text: 'Pet activity'
		},
		tooltip: {},
		legend: {
			data:['times']
		},
		xAxis: {
			data: ["stand still","walking","running"]
		},
		yAxis: {},
		series: [{
			name: 'times',
			type: 'bar',
			data: [0, 0, 0]
		}]
	};
	// 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    

    var statictics = [0, 0, 0]

    setInterval(function(){  
        $.getJSON("get_speed_history",function(result){
            var speed_history = result['speed_history']
            statictics[0] = speed_history.filter(function(speed) {
                return speed <=1
            }).length;
            statictics[1] = speed_history.filter(function(speed) {
                return (speed > 1 && speed <= 5)
            }).length;
            statictics[2] = speed_history.filter(function(speed) {
                return speed > 5
            }).length;
            option['series'][0]['data'] = statictics
            myChart.setOption(option)
        });    
    }, 1000);
});

