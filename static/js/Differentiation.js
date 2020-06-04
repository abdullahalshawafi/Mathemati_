var parameters = {
	target: '#myFunction',
	data: [{
		fn: '0',
		color: "rgba(0,0,0,0)",
		range: [-10, 10]
	},
	{
		points: [],
		fnType: 'points',
		graphType: 'scatter',
		color: "#000000"
	}],
	grid: true,
	yAxis: { domain: [-5, 5] },
	xAxis: { domain: [-5, 5] },
	height: window.innerWidth / 100 * 18.45,
	width: window.innerWidth / 100 * 19.13
};
functionPlot(parameters);

function addtograph() {
	if (document.getElementsByClassName("Rectangle_43")[0].value && document.getElementsByName("Method")[0].checked) {
		parameters.data[0].color = "#00ff88";
		parameters.data[0].fn = document.getElementsByClassName("Rectangle_43")[0].value;
	}
	functionPlot(parameters);
}

function Scatter(el) {
    var elx = el.parentElement.parentElement.childNodes[1].childNodes[0];
    var ely = el.parentElement.parentElement.childNodes[3].childNodes[0];

    if (elx.value && ely.value) {
        var point = [parseFloat(elx.value), parseFloat(ely.value)];
        parameters.data[1].points.push(point);
    }
    functionPlot(parameters);
}

document.getElementById('clear').addEventListener('click', function () {
	parameters.data[1].points = [];
	functionPlot(parameters);
});

window.onload = function() {
    addtograph();
		for (var i = 0; i <= 14; i++) {
        Scatter(document.getElementsByName("x" + i)[0]);
        Scatter(document.getElementsByName("y" + i)[0]);
    }
}
