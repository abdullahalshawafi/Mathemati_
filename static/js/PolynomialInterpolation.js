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
      fn: '',
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
