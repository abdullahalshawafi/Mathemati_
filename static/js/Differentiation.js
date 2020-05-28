var parameters = {
	target: '#myFunction',
	data: [{
		fn: '',
		color: "#00ff88",
		range: [-10, 10]
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
		parameters.data[0].fn = document.getElementsByClassName("Rectangle_43")[0].value;
	}
	functionPlot(parameters);
}

window.onload = function() {
    addtograph();
};
