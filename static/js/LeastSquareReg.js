x = 0;
var parameters = {
  target: '#myFunction',
  data: [
    {
      fn: 'sin(x)',
      color: "hsl(" + ((x * 3.6 + 180)) + ", 100%, 60%)",
      range: [0, Math.PI / 2],
      closed: false
    },
    {
      x: 'cos(t)',
      y: 'sin(t)',
      fnType: 'parametric',
      graphType: 'polyline'
    },
    {
      fn: 'x * x + y * y - 2',
      fnType: 'implicit'
    }
  ],
  grid: true,
  yAxis: { domain: [-3, 3] },
  xAxis: { domain: [-3, 3] },
  height: window.innerWidth / 100 * 18.45,
  width: window.innerWidth / 100 * 19.13
};
functionPlot(parameters);

function substitute(el) {
  var x = el.value;
  console.log(x);
  var F = document.getElementsByClassName('Rectangle_Essam')[0].value;
  F.replace('**', '^');
  F.replace('sin', '(1)*')
  F.replace('cos(', 'Math.cos(')
  F.replace('tan(', 'Math.tan(')
  F.replace('exp(', 'Math.exp(')
  console.log(F);
  document.getElementsByClassName('Rectangle_42')[0].value = eval(F);
}
