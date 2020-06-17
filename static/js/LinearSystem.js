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

window.onload = function () {
  addtograph();
  DimInput();
}

function addtograph() {
  if (document.getElementsByClassName("Rectangle_19")[0].value && document.getElementsByClassName("Rectangle_36")[0].value
    && document.getElementsByClassName("Rectangle_40")[0].value && document.getElementsByName("Dim")[0].checked) {
    parameters.data[0].fn = document.getElementsByClassName("Rectangle_19")[0].value + " * x + "
      + document.getElementsByClassName("Rectangle_36")[0].value + " * y - " +
      + document.getElementsByClassName("Rectangle_40")[0].value;

  }
  if (document.getElementsByClassName("Rectangle_19_bo")[0].value && document.getElementsByClassName("Rectangle_36_bq")[0].value
    && document.getElementsByClassName("Rectangle_40_bu")[0].value && document.getElementsByName("Dim")[0].checked) {
    parameters.data[1].fn = document.getElementsByClassName("Rectangle_19_bo")[0].value + " * x + "
      + document.getElementsByClassName("Rectangle_36_bq")[0].value + " * y - " +
      + document.getElementsByClassName("Rectangle_40_bu")[0].value;
  }
  functionPlot(parameters);
}


function DimInput() {
  var Dim2 = document.getElementsByName("Dim")[0];
  var Dim3 = document.getElementsByName("Dim")[1];
  var Dim4 = document.getElementsByName("Dim")[2];

  if (Dim2.checked) {
    document.getElementsByClassName("Rectangle_37")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_37")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_37_br")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_37_br")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_19_bw")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_19_bw")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_36_by")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_36_by")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_37_bz")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_37_bz")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_40_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_40_b")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementsByClassName("Rectangle_38")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_bs")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_bs")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_19_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_19_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_36_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_36_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_37_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_37_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_ca")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_ca")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_40_ca")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_40_ca")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementsByClassName("Rectangle_39")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_bt")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_bt")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_ca")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_ca")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_19_cc")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_19_cc")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_36_ce")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_36_ce")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_37_cf")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_37_cf")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_cg")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_cg")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_ch")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_ch")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_40_ci")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_40_ci")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementById("x3__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("x4__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("x5__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "background: #303030; color: #999999;");
  }
  else if (Dim4.checked) {
    document.getElementsByClassName("Rectangle_37")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_br")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_br")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_19_bw")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_19_bw")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_36_by")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_36_by")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_bz")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_bz")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_40_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_40_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementsByClassName("Rectangle_38")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_38_bs")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38_bs")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_38_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_19_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_19_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_36_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_36_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_38_ca")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38_ca")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_40_ca")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_40_ca")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementsByClassName("Rectangle_39")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_bt")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_bt")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_ca")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_ca")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_19_cc")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_19_cc")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_36_ce")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_36_ce")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_37_cf")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_37_cf")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_cg")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_cg")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_ch")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_ch")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_40_ci")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_40_ci")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementById("x3__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("x4__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("x5__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "background: #303030; color: #999999;");
  }
  else if (Dim3.checked) {
    document.getElementsByClassName("Rectangle_37")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_br")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_br")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_19_bw")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_19_bw")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_36_by")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_36_by")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_bz")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_bz")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_40_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_40_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementsByClassName("Rectangle_38")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_bs")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_bs")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_19_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_19_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_36_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_36_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_37_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_37_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_ca")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_ca")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_40_ca")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_40_ca")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementsByClassName("Rectangle_39")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_bt")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_bt")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_ca")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_ca")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_b")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_b")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_19_cc")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_19_cc")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_36_ce")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_36_ce")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_37_cf")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_37_cf")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_38_cg")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_38_cg")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_39_ch")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_39_ch")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_40_ci")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_40_ci")[0].setAttribute("style", "background: #303030; color: #999999;");

    document.getElementById("x3__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("x4__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("x5__").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "background: #303030; color: #999999;");
  }
  else {
    document.getElementsByClassName("Rectangle_37")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_br")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_br")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_19_bw")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_19_bw")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_36_by")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_36_by")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_bz")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_bz")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_40_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_40_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementsByClassName("Rectangle_38")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_38_bs")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38_bs")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_38_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_19_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_19_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_36_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_36_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_38_ca")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38_ca")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_40_ca")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_40_ca")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementsByClassName("Rectangle_39")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_39")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_39_bt")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_39_bt")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_39_ca")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_39_ca")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_39_b")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_39_b")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_19_cc")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_19_cc")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_36_ce")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_36_ce")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_37_cf")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_37_cf")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_38_cg")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_38_cg")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_39_ch")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_39_ch")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_40_ci")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_40_ci")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementById("x3__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("x4__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("x5__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
  }
}
