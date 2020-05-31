var z1 = [[1, 2, 1, 10, 3], [1, 4, 3, 1, 2], [8, 4, 5, 1, 2]];
var x1 = [2, 4, 6, 8, 10];
var y1 = [3, 6, 9];


var data_z1 = { z: z1, x: x1, y: y1, type: 'surface', colorscale: 'Lava', };
var layout = {
  scene: { camera: { eye: { x: 1.8, y: 1.8, z: 1.5 } } },
  width: window.innerWidth / 100 * 31.5,
  height: window.innerWidth / 100 * 26,
  margin: {
    l: 0,
    r: 0,
    b: 0,
    t: window.innerWidth / 100 * 1.94
  }
};

Plotly.newPlot('myFunction', [data_z1], layout);
