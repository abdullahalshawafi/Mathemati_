var x = 0;
var parameters = {
  target: '#myFunction',
  data: [
    {
      fn: 'x * x + y * y - 2',
      fnType: 'implicit',
      color: "rgb(0,100,255)",
      interval2d: [0.5, 0.8]
    },
    {
      fn: 'x^2',
      color: "rgb(0,100,255)"
    }
  ],
  grid: true,
  yAxis: { domain: [-2, 2] },
  xAxis: { domain: [-3, 3] },
  height: window.innerWidth / 100 * 16,
  width: window.innerWidth / 100 * 23.5
};
functionPlot(parameters);

function MethodSelection() {
  var Irregular = document.getElementsByName("Method")[1];
  if (Irregular.checked) {
    document.getElementById("UXY1").style.display="none";
    document.getElementById("UXY2").style.display="none";

  } else {
    document.getElementById("UXY1").style.display="inline";
    document.getElementById("UXY2").style.display="inline";
  }
}
