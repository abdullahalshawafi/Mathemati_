var parameters = {
  target: '#myFunction',
  data: [{
    fn: 'x + 1000000',
    color: "#00ff88",
    range: [-10, 10]
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
  if (document.getElementsByClassName("Rectangle_43")[0].value && document.getElementsByName("Dim")[0].checked) {
    parameters.data[0].fn = document.getElementsByClassName("Rectangle_43")[0].value;
  }
  if (document.getElementsByClassName("Rectangle_59")[0].value && document.getElementsByClassName("Rectangle_60")[0].value && document.getElementsByName("Dim")[0].checked) {
    parameters.data[0].range = [parseInt(document.getElementsByClassName("Rectangle_60")[0].value), parseInt(document.getElementsByClassName("Rectangle_59")[0].value)];
    parameters.data[0].closed = true;
  }
  functionPlot(parameters);
}

window.onload = function () {
  addtograph();
  DimInput();
};

function DimInput() {
  var Dim1 = document.getElementsByName("Dim")[0];
  var Dim2 = document.getElementsByName("Dim")[1];

  if (Dim1.checked) {
    document.getElementsByClassName("Rectangle_62")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_62")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_63")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_63")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_64")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_64")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementsByClassName("Rectangle_65")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_65")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_66")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_66")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_67")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_67")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementById("Yf__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("Yi__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("N_in_the_Y_direction__").setAttribute("style", "color: #999999; text-decoration: line-through; ");

    document.getElementById("Zf__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("Zi__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("N_in_the_Z_direction__").setAttribute("style", "color: #999999; text-decoration: line-through; ");

    document.getElementById("f_x__y__z___").innerHTML = "<span>f(x) =</span>";
    document.getElementsByClassName("Rectangle_32E")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_46E")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementById("I___E").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("Error__E").setAttribute("style", "color: white; text-decoration: normal; ");
  }
  else if (Dim2.checked) {
    document.getElementsByClassName("Rectangle_62")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_62")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_63")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_63")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_64")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_64")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementsByClassName("Rectangle_65")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_65")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_66")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_66")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_67")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_67")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementById("Yf__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("Yi__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("N_in_the_Y_direction__").setAttribute("style", "color: white; text-decoration: normal; ");

    document.getElementById("Zf__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("Zi__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("N_in_the_Z_direction__").setAttribute("style", "color: #999999; text-decoration: line-through; ");

    document.getElementById("f_x__y__z___").innerHTML = "<span>f(x, y) =</span>";
    document.getElementsByClassName("Rectangle_32E")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_46E")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementById("I___E").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("Error__E").setAttribute("style", "color: #999999; text-decoration: line-through; ");



  }
  else {
    document.getElementsByClassName("Rectangle_62")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_62")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_63")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_63")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_64")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_64")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementsByClassName("Rectangle_65")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_65")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_66")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_66")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_67")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_67")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementById("Yf__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("Yi__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("N_in_the_Y_direction__").setAttribute("style", "color: white; text-decoration: normal; ");

    document.getElementById("Zf__").setAttribute("style", "color: white; text-decoration: normal;");
    document.getElementById("Zi__").setAttribute("style", "color: white; text-decoration: normal;");
    document.getElementById("N_in_the_Z_direction__").setAttribute("style", "color: white; text-decoration: normal;");

    document.getElementById("f_x__y__z___").innerHTML = "<span>f(x, y, z) =</span>";
    document.getElementsByClassName("Rectangle_32E")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_46E")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementById("I___E").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("Error__E").setAttribute("style", "color: #999999; text-decoration: line-through; ");

  }
}
