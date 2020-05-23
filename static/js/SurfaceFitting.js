x = 0;
var parameters = {
  target: '#myFunction',
  data: [
    {
      fn: '',
      color: "hsl(" + ((x * 3.6 + 180)) + ", 100%, 60%)",
      range: [0, Math.PI / 2],
      closed: false
    },
    {
      x: '',
      y: '',
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
  var x = parseFloat(document.getElementsByClassName('Rectangle_41')[0].value);
  var y = parseFloat(el.value);
  var F = document.getElementsByClassName('Rectangle_32')[0].value;
  F = F.replace(/\^/g, '**');
  F = F.replace(/sin/g, 'Math.sin');
  F = F.replace(/cos/g, 'Math.cos');
  F = F.replace(/tan/g, 'Math.tan');
  F = F.replace(/exp/g, 'Math.exp');
  F = F.replace(/log/g, 'Math.log');
  if (eval(F).toFixed(4) != "NaN")
    document.getElementsByClassName('Rectangle_42')[0].value = eval(F).toFixed(4);
  else
    document.getElementsByClassName('Rectangle_42')[0].value = '';
}
