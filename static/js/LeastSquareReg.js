var parameters = {
  target: '#myFunction',
  data: [{
    fn: 'x * x + y * y -1000000',
    color: "#eb00ff",
    fnType: 'implicit'
  },
  {
    fn: 'x * x + y * y -1000000',
    color: "#2c00ff",
    fnType: 'implicit'
  }
  ],
  grid: true,
  yAxis: { domain: [-5, 5] },
  xAxis: { domain: [-5, 5] },
  height: window.innerWidth / 100 * 18.45,
  width: window.innerWidth / 100 * 19.13
};

functionPlot(parameters);

function addtograph() {
  if (document.getElementsByClassName("Rectangle_Essam")[0].value) {
    var func = document.getElementsByClassName("Rectangle_Essam")[0].value;
    func = func.replace('**', '^')
    parameters.data[1].fn = '-y+' + func;
  }
  functionPlot(parameters);
}

window.onload = function () {
  addtograph();
};

function substitute(el) {
  var x = parseFloat(el.value);
  console.log(x);
  var F = document.getElementsByClassName('Rectangle_Essam')[0].value;
  F = F.replace('**', '^');
  F = F.replace('sin', 'Math.sin');
  F = F.replace('cos(', 'Math.cos(');
  F = F.replace('tan(', 'Math.tan(');
  F = F.replace('exp(', 'Math.exp(');
  F = F.replace('log(', 'Math.log()');
  console.log(F);
  document.getElementsByClassName('Rectangle_42')[0].value = eval(F);
}
