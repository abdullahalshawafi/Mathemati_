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

    document.getElementsByClassName("Rectangle_44")[2].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_44")[2].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_44")[3].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_44")[3].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_44")[4].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_44")[4].setAttribute("style", "background: #303030; color: #999999;");

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

    document.getElementsByClassName("Rectangle_44")[2].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_44")[2].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_44")[3].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_44")[3].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_44")[4].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_44")[4].setAttribute("style", "background: #303030; color: #999999;");

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

    document.getElementsByClassName("Rectangle_44")[2].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_44")[2].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_44")[3].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_44")[3].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_44")[4].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_44")[4].setAttribute("style", "background: #303030; color: #999999;");

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

    document.getElementsByClassName("Rectangle_44")[2].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_44")[2].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_44")[3].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_44")[3].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_44")[4].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_44")[4].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementById("x3__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("x4__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("x5__").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
  }


}


function saveTextAsFile()
    {

        inputs = document.getElementsByTagName("input");

        if( document.getElementById('2eqs').checked)
             {
                 var textToSave = "Inputs\n\nW = "+document.getElementsByName("w")[0].value+
                 "\nNumber of equations = 2\n\nIntial Vector = [" + document.getElementsByName("X1")[0].value+" "+document.getElementsByName("X2")[0].value+" ]\n"+
                 "\nEq_1 = [ " + document.getElementsByName("x00")[0].value+" , "+document.getElementsByName("x01")[0].value+" , "+document.getElementsByName("c0")[0].value+" ]"+
                 "\nEq_2 = [ " + document.getElementsByName("x10")[0].value+" , "+document.getElementsByName("x11")[0].value+" , "+document.getElementsByName("c1")[0].value+" ]\n"+
                 "\nNumber of iterations = " + document.getElementsByName("Number of iterations")[0].value+
                 "\nStopping Criteria = " + document.getElementsByName("Stopping Criteria")[0].value;
          
             }
        else if( document.getElementById('3eqs').checked)
             {
                 var textToSave = "Inputs\n\nW = "+document.getElementsByName("w")[0].value+
                 "\nNumber of equations = 3\n\nIntial Vector = [" + document.getElementsByName("X1")[0].value+" "+document.getElementsByName("X2")[0].value+" "+document.getElementsByName("X3")[0].value+" ]\n"+
                 "\nEq_1 = [ " + document.getElementsByName("x00")[0].value+" , "+document.getElementsByName("x01")[0].value+" , "+document.getElementsByName("x02")[0].value+" , "+document.getElementsByName("c0")[0].value+" ]"+
                 "\nEq_2 = [ " + document.getElementsByName("x10")[0].value+" , "+document.getElementsByName("x11")[0].value+" , "+document.getElementsByName("x12")[0].value+" , "+document.getElementsByName("c1")[0].value+" ]"+
                 "\nEq_3 = [ " + document.getElementsByName("x20")[0].value+" , "+document.getElementsByName("x21")[0].value+" , "+document.getElementsByName("x22")[0].value+" , "+document.getElementsByName("c2")[0].value+" ]\n"+
                 "\nNumber of iterations = " + document.getElementsByName("Number of iterations")[0].value+
                 "\nStopping Criteria = " + document.getElementsByName("Stopping Criteria")[0].value;
          
             }
              else if( document.getElementById('4eqs').checked)
             {
                 var textToSave = "Inputs\n\nW = "+document.getElementsByName("w")[0].value+
                 "\nNumber of equations = 4\n\nIntial Vector = [" + document.getElementsByName("X1")[0].value+" "+document.getElementsByName("X2")[0].value+" "+document.getElementsByName("X3")[0].value+" "+document.getElementsByName("X4")[0].value+" ]\n"+
                 "\nEq_1 = [ " + document.getElementsByName("x00")[0].value+" , "+document.getElementsByName("x01")[0].value+" , "+document.getElementsByName("x02")[0].value+" , "+document.getElementsByName("x03")[0].value+" , "+document.getElementsByName("c0")[0].value+" ]"+
                 "\nEq_2 = [ " + document.getElementsByName("x10")[0].value+" , "+document.getElementsByName("x11")[0].value+" , "+document.getElementsByName("x12")[0].value+" , "+document.getElementsByName("x13")[0].value+" , "+document.getElementsByName("c1")[0].value+" ]"+
                 "\nEq_3 = [ " + document.getElementsByName("x20")[0].value+" , "+document.getElementsByName("x21")[0].value+" , "+document.getElementsByName("x22")[0].value+" , "+document.getElementsByName("x23")[0].value+" , "+document.getElementsByName("c2")[0].value+" ]"+
                 "\nEq_4 = [ " + document.getElementsByName("x30")[0].value+" , "+document.getElementsByName("x31")[0].value+" , "+document.getElementsByName("x32")[0].value+" , "+document.getElementsByName("x33")[0].value+" , "+document.getElementsByName("c3")[0].value+" ]\n"+
                 "\nNumber of iterations = " + document.getElementsByName("Number of iterations")[0].value+
                 "\nStopping Criteria = " + document.getElementsByName("Stopping Criteria")[0].value;
          
             }
             else
             {
                 var textToSave = "Inputs\n\nW = "+document.getElementsByName("w")[0].value+
                 "\nNumber of equations = 5\n\nIntial Vector = [" + document.getElementsByName("X1")[0].value+" "+document.getElementsByName("X2")[0].value+" "+document.getElementsByName("X3")[0].value+" "+document.getElementsByName("X4")[0].value+" "+document.getElementsByName("X5")[0].value+" ]\n"+
                 "\nEq_1 = [ " + document.getElementsByName("x00")[0].value+" , "+document.getElementsByName("x01")[0].value+" , "+document.getElementsByName("x02")[0].value+" , "+document.getElementsByName("x03")[0].value+" , "+document.getElementsByName("x04")[0].value+" , "+document.getElementsByName("c0")[0].value+" ]"+
                 "\nEq_2 = [ " + document.getElementsByName("x10")[0].value+" , "+document.getElementsByName("x11")[0].value+" , "+document.getElementsByName("x12")[0].value+" , "+document.getElementsByName("x13")[0].value+" , "+document.getElementsByName("x14")[0].value+" , "+document.getElementsByName("c1")[0].value+" ]"+
                 "\nEq_3 = [ " + document.getElementsByName("x20")[0].value+" , "+document.getElementsByName("x21")[0].value+" , "+document.getElementsByName("x22")[0].value+" , "+document.getElementsByName("x23")[0].value+" , "+document.getElementsByName("x24")[0].value+" , "+document.getElementsByName("c2")[0].value+" ]"+
                 "\nEq_4 = [ " + document.getElementsByName("x30")[0].value+" , "+document.getElementsByName("x31")[0].value+" , "+document.getElementsByName("x32")[0].value+" , "+document.getElementsByName("x33")[0].value+" , "+document.getElementsByName("x34")[0].value+" , "+document.getElementsByName("c3")[0].value+" ]"+
                 "\nEq_5 = [ " + document.getElementsByName("x40")[0].value+" , "+document.getElementsByName("x41")[0].value+" , "+document.getElementsByName("x42")[0].value+" , "+document.getElementsByName("x43")[0].value+" , "+document.getElementsByName("x44")[0].value+" , "+document.getElementsByName("c3")[0].value+" ]\n"+

                 "\nNumber of iterations = " + document.getElementsByName("Number of iterations")[0].value+
                 "\nStopping Criteria = " + document.getElementsByName("Stopping Criteria")[0].value;
             }

            var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
            var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
            var fileNameToSaveAs = document.getElementById("inputFileNameToSaveAs").value;

            var downloadLink = document.createElement("a");
            downloadLink.download = fileNameToSaveAs;
            downloadLink.innerHTML = "Download File";
            downloadLink.href = textToSaveAsURL;
            downloadLink.onclick = destroyClickedElement;
            downloadLink.style.display = "none";
            document.body.appendChild(downloadLink);
            downloadLink.click();
    }

function destroyClickedElement(event)
{
    document.body.removeChild(event.target); 
}