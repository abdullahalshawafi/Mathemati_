DimInput();
function DimInput() {
  var Eu = document.getElementsByName("Method")[0].checked;

  document.getElementsByClassName("Rectangle_42E")[0].setAttribute("style", "filter: contrast(1);");
  document.getElementById("x4__E").setAttribute("style", "filter: contrast(1);");
  document.getElementById("ExTab").setAttribute("style", "opacity: 1;");


  if (Eu) {

    document.getElementsByClassName("Rectangle_42E")[0].setAttribute("style", "filter: contrast(0.9);");
    document.getElementById("x4__E").setAttribute("style", "filter: contrast(0.4);");
    document.getElementById("ExTab").setAttribute("style", "opacity: 0;	");


    document.getElementById("Number_of_iterations__").innerHTML = 'Number of steps (n) =';
    document.getElementById("Stopping_Criteria__s___").innerHTML = "Step Size (h) = ";

    document.getElementById("1ODEs").setAttribute("disabled", "true");
    document.getElementById("2ODEs").setAttribute("disabled", "true");
    document.getElementById("3ODEs").setAttribute("disabled", "true");

    document.getElementById("1ODEs").checked = false;
    document.getElementById("2ODEs").checked = false;
    document.getElementById("3ODEs").checked = false;

    document.getElementById("3ODEs").parentElement.parentElement.setAttribute("style", "filter: contrast(0.4);");

    document.getElementById("3eqs").removeAttribute("disabled");
    document.getElementById("3eqs").parentElement.setAttribute("style", "filter: contrast(1);");

    document.getElementById("1eqs").removeAttribute("disabled");
    document.getElementById("1eqs").parentElement.setAttribute("style", "filter: contrast(1);");
    document.getElementById("2eqs").removeAttribute("disabled");
    document.getElementById("2eqs").parentElement.setAttribute("style", "filter: contrast(1);");

    document.getElementsByClassName("Y2")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Y2")[0].setAttribute("style", "filter: contrast(0.9);");
    document.getElementsByClassName("Y3")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Y3")[0].setAttribute("style", "filter: contrast(0.9);");

    document.getElementById("y2").setAttribute("style", "filter: contrast(0.4);");
    document.getElementById("y3").setAttribute("style", "filter: contrast(0.4);");

    document.getElementsByClassName("Rectangle_352I")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_352I")[0].setAttribute("style", "filter: contrast(0.9);");
    document.getElementsByClassName("Rectangle_332I")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_332I")[0].setAttribute("style", "filter: contrast(0.9);");

    document.getElementById("y2___I").setAttribute("style", "filter: contrast(0.4);");
    document.getElementById("_s2___I").setAttribute("style", "filter: contrast(0.4);");

    document.getElementsByClassName("Rectangle_34")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "filter: contrast(0.9);");
    document.getElementsByClassName("Rectangle_35")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_35")[0].setAttribute("style", "filter: contrast(0.9);");

    document.getElementById("x5__").setAttribute("style", "filter: contrast(0.4);");
    document.getElementById("_s___").setAttribute("style", "filter: contrast(0.4);");

    // making sure T is accesable

    document.getElementsByClassName("T1")[0].removeAttribute("disabled");
    document.getElementsByClassName("T1")[0].setAttribute("style", "filter: contrast(1);");
    document.getElementById("t1").setAttribute("style", "filter: contrast(1);");
    document.getElementsByClassName("Rectangle_35I")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_35I")[0].setAttribute("style", "filter: contrast(1);");
    document.getElementById("_s___I").setAttribute("style", "filter: contrast(1);");
    document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(1);");
    document.getElementById("x4__").setAttribute("style", "filter: contrast(1);");



    //document.getElementById("y___I").setAttribute("style", "filter: contrast(1);");
    //document.getElementById("y1").setAttribute("style", "filter: contrast(1);");
    //document.getElementById("x3__").setAttribute("style", "filter: contrast(1);");


    var eqDim1 = document.getElementsByName("Dim")[0].checked;
    var eqDim2 = document.getElementsByName("Dim")[1].checked;
    var eqDim3 = document.getElementsByName("Dim")[2].checked;

    if (eqDim1) {
      document.getElementsByClassName("Z1")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Z1")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("T1")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("T1")[0].setAttribute("style", "filter: contrast(0.9);");

      document.getElementById("z1").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("t1").setAttribute("style", "filter: contrast(0.4);");

      document.getElementsByClassName("Rectangle_34I")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Rectangle_34I")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("Rectangle_35I")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Rectangle_35I")[0].setAttribute("style", "filter: contrast(0.9);");


      document.getElementById("z___I").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("_s___I").setAttribute("style", "filter: contrast(0.4);");

      document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(0.9);");

      document.getElementById("x4__").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("x3__").setAttribute("style", "filter: contrast(0.4);");

      document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("x,z, y, t", "x, y");
      document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("x,z, y", "x, y");

    }
    else if (eqDim2) {
      document.getElementsByClassName("Z1")[0].removeAttribute("disabled");
      document.getElementsByClassName("Z1")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("T1")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("T1")[0].setAttribute("style", "filter: contrast(0.9);");

      document.getElementById("z1").setAttribute("style", "filter: contrast(1);");
      document.getElementById("t1").setAttribute("style", "filter: contrast(0.4);");

      document.getElementsByClassName("Rectangle_34I")[0].removeAttribute("disabled");
      document.getElementsByClassName("Rectangle_34I")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("Rectangle_35I")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Rectangle_35I")[0].setAttribute("style", "filter: contrast(0.9);");


      document.getElementById("z___I").setAttribute("style", "filter: contrast(1);");
      document.getElementById("_s___I").setAttribute("style", "filter: contrast(0.4);");

      document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(0.9);");

      document.getElementById("x3__").setAttribute("style", "filter: contrast(1);");
      document.getElementById("x4__").setAttribute("style", "filter: contrast(0.4);");

      document.getElementById("z1").innerHTML = document.getElementById("z1").innerHTML.replace("z, y, t", "z, y");

      document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("x,z, y, t", "x,z, y");
      document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("x, y", "x,z, y");

    }
    else if (eqDim3) {
      document.getElementsByClassName("Z1")[0].removeAttribute("disabled");
      document.getElementsByClassName("Z1")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("T1")[0].removeAttribute("disabled");
      document.getElementsByClassName("T1")[0].setAttribute("style", "filter: contrast(1);");

      document.getElementById("z1").setAttribute("style", "filter: contrast(1);");
      document.getElementById("t1").setAttribute("style", "filter: contrast(1);");

      document.getElementsByClassName("Rectangle_34I")[0].removeAttribute("disabled");
      document.getElementsByClassName("Rectangle_34I")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("Rectangle_35I")[0].removeAttribute("disabled");
      document.getElementsByClassName("Rectangle_35I")[0].setAttribute("style", "filter: contrast(1);");


      document.getElementById("z___I").setAttribute("style", "filter: contrast(1);");
      document.getElementById("_s___I").setAttribute("style", "filter: contrast(1);");

      document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(1);");

      document.getElementById("x3__").setAttribute("style", "filter: contrast(1);");
      document.getElementById("x4__").setAttribute("style", "filter: contrast(1);");

      document.getElementById("z1").innerHTML = document.getElementById("z1").innerHTML.replace("z, y", "z, y, t");

      document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("x,z, y", "x,z, y, t");
      document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("x, y", "x,z, y, t");

    }

  }
  else {

    document.getElementById("Number_of_iterations__").innerHTML = 'Number of iterations =';
    document.getElementById("Stopping_Criteria__s___").innerHTML = "Stopping Criteria es% =";

    document.getElementById("1ODEs").removeAttribute("disabled");
    document.getElementById("2ODEs").removeAttribute("disabled");
    document.getElementById("3ODEs").removeAttribute("disabled");
    document.getElementById("3ODEs").parentElement.parentElement.setAttribute("style", "filter: contrast(1);");

    document.getElementById("3eqs").checked = false;


    document.getElementById("3eqs").setAttribute("disabled", "true");
    document.getElementById("3eqs").parentElement.setAttribute("style", "filter: contrast(0.4);");
    document.getElementById("1eqs").setAttribute("disabled", "true");
    document.getElementById("1eqs").parentElement.setAttribute("style", "filter: contrast(0.4);");
    document.getElementById("2eqs").setAttribute("disabled", "true");
    document.getElementById("2eqs").parentElement.setAttribute("style", "filter: contrast(0.4);");


    document.getElementsByClassName("Y2")[0].removeAttribute("disabled");
    document.getElementsByClassName("Y2")[0].setAttribute("style", "filter: contrast(1);");
    document.getElementsByClassName("Y3")[0].removeAttribute("disabled");
    document.getElementsByClassName("Y3")[0].setAttribute("style", "filter: contrast(1);");

    document.getElementById("y2").setAttribute("style", "filter: contrast(1);");
    document.getElementById("y3").setAttribute("style", "filter: contrast(1);");

    document.getElementsByClassName("Rectangle_352I")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_352I")[0].setAttribute("style", "filter: contrast(1);");
    document.getElementsByClassName("Rectangle_332I")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_332I")[0].setAttribute("style", "filter: contrast(1);");

    document.getElementById("y2___I").setAttribute("style", "filter: contrast(1);");
    document.getElementById("_s2___I").setAttribute("style", "filter: contrast(1);");

    document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "filter: contrast(1);");
    document.getElementsByClassName("Rectangle_35")[0].setAttribute("style", "filter: contrast(1);");

    document.getElementById("x5__").setAttribute("style", "filter: contrast(1);");
    document.getElementById("_s___").setAttribute("style", "filter: contrast(1);");

    document.getElementsByClassName("T1")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("T1")[0].setAttribute("style", "filter: contrast(0.9);");
    document.getElementById("t1").setAttribute("style", "filter: contrast(0.4);");
    document.getElementsByClassName("Rectangle_35I")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_35I")[0].setAttribute("style", "filter: contrast(0.9);");
    document.getElementById("_s___I").setAttribute("style", "filter: contrast(0.4);");
    document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(0.9);");
    document.getElementById("x4__").setAttribute("style", "filter: contrast(0.4);");

    document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("z, y, t", "x, y");
    document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("z, y", "x, y");
    document.getElementById("z1").innerHTML = document.getElementById("z1").innerHTML.replace("z, y, t", "x, y");


    var ODim1 = document.getElementsByName("ODim")[0].checked;
    var ODim2 = document.getElementsByName("ODim")[1].checked;
    var ODim3 = document.getElementsByName("ODim")[2].checked;

    if (ODim1) {
      document.getElementById("1eqs").removeAttribute("disabled");
      document.getElementById("1eqs").parentElement.setAttribute("style", "filter: contrast(1);");
      document.getElementById("2eqs").removeAttribute("disabled");
      document.getElementById("2eqs").parentElement.setAttribute("style", "filter: contrast(1);");


      var eqDim1 = document.getElementsByName("Dim")[0].checked;
      var eqDim2 = document.getElementsByName("Dim")[1].checked;

      if (eqDim1) {
        document.getElementsByClassName("Z1")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Z1")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementsByClassName("Y3")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Y3")[0].setAttribute("style", "filter: contrast(0.9);");

        document.getElementById("z1").setAttribute("style", "filter: contrast(0.4);");
        document.getElementById("y3").setAttribute("style", "filter: contrast(0.4);");

        document.getElementsByClassName("Rectangle_34I")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Rectangle_34I")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementsByClassName("Rectangle_352I")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Rectangle_352I")[0].setAttribute("style", "filter: contrast(0.9);");

        document.getElementById("z___I").setAttribute("style", "filter: contrast(0.4);");
        document.getElementById("_s2___I").setAttribute("style", "filter: contrast(0.4);");

        document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(0.9);");

        document.getElementById("x4__").setAttribute("style", "filter: contrast(0.4);");
        document.getElementById("x3__").setAttribute("style", "filter: contrast(0.4);");

        // making sure Y2 is inaccesable

        document.getElementsByClassName("Y2")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Y2")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementById("y2").setAttribute("style", "filter: contrast(0.4);");
        document.getElementsByClassName("Rectangle_332I")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Rectangle_332I")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementById("y2___I").setAttribute("style", "filter: contrast(0.4);");
        document.getElementsByClassName("Rectangle_35")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementById("_s___").setAttribute("style", "filter: contrast(0.4);");

        document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementById("x5__").setAttribute("style", "filter: contrast(0.4);");
      }
      if (eqDim2) {


        document.getElementsByClassName("Y2")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Y2")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementsByClassName("Y3")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Y3")[0].setAttribute("style", "filter: contrast(0.9);");

        document.getElementById("y2").setAttribute("style", "filter: contrast(0.4);");
        document.getElementById("y3").setAttribute("style", "filter: contrast(0.4);");

        document.getElementsByClassName("Rectangle_332I")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Rectangle_332I")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementsByClassName("Rectangle_352I")[0].setAttribute("disabled", "true");
        document.getElementsByClassName("Rectangle_352I")[0].setAttribute("style", "filter: contrast(0.9);");

        document.getElementById("y2___I").setAttribute("style", "filter: contrast(0.4);");
        document.getElementById("_s2___I").setAttribute("style", "filter: contrast(0.4);");

        document.getElementsByClassName("Rectangle_35")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(0.9);");

        document.getElementById("_s___").setAttribute("style", "filter: contrast(0.4);");
        document.getElementById("x4__").setAttribute("style", "filter: contrast(0.4);");

        document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "filter: contrast(0.9);");
        document.getElementById("x5__").setAttribute("style", "filter: contrast(0.4);");

        // making sure Z1 is accesable

        document.getElementsByClassName("Z1")[0].removeAttribute("disabled");
        document.getElementsByClassName("Z1")[0].setAttribute("style", "filter: contrast(1);");
        document.getElementById("z1").setAttribute("style", "filter: contrast(1);");
        document.getElementsByClassName("Rectangle_34I")[0].removeAttribute("disabled");
        document.getElementsByClassName("Rectangle_34I")[0].setAttribute("style", "filter: contrast(1);");
        document.getElementById("z___I").setAttribute("style", "filter: contrast(1);");
        document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "filter: contrast(1);");
        document.getElementById("x3__").setAttribute("style", "filter: contrast(1);");

        document.getElementById("y1").innerHTML = document.getElementById("y1").innerHTML.replace("x, y", "z, y");
        document.getElementById("z1").innerHTML = document.getElementById("z1").innerHTML.replace("x, y", "z, y");


      }
    }
    else {
      document.getElementById("1eqs").checked = false;
      document.getElementById("2eqs").checked = false;


    }

    if (ODim2) {
      document.getElementsByClassName("Z1")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Z1")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("Y3")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Y3")[0].setAttribute("style", "filter: contrast(0.9);");

      document.getElementById("z1").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("y3").setAttribute("style", "filter: contrast(0.4);");

      document.getElementsByClassName("Rectangle_34I")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Rectangle_34I")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("Rectangle_352I")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Rectangle_352I")[0].setAttribute("style", "filter: contrast(0.9);");

      document.getElementById("z___I").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("_s2___I").setAttribute("style", "filter: contrast(0.4);");

      document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(0.9);");

      document.getElementById("x4__").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("x3__").setAttribute("style", "filter: contrast(0.4);");

      // making sure Y2 is accesable

      document.getElementsByClassName("Y2")[0].removeAttribute("disabled");
      document.getElementsByClassName("Y2")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementById("y2").setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("Rectangle_332I")[0].removeAttribute("disabled");
      document.getElementsByClassName("Rectangle_332I")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementById("y2___I").setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("Rectangle_35")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementById("_s___").setAttribute("style", "filter: contrast(0.4);");
    }
    if (ODim3) {
      document.getElementsByClassName("Z1")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Z1")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("Y3")[0].removeAttribute("disabled");
      document.getElementsByClassName("Y3")[0].setAttribute("style", "filter: contrast(1);");

      document.getElementById("z1").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("y3").setAttribute("style", "filter: contrast(1);");

      document.getElementsByClassName("Rectangle_34I")[0].setAttribute("disabled", "true");
      document.getElementsByClassName("Rectangle_34I")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("Rectangle_352I")[0].removeAttribute("disabled");
      document.getElementsByClassName("Rectangle_352I")[0].setAttribute("style", "filter: contrast(1);");

      document.getElementById("z___I").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("_s2___I").setAttribute("style", "filter: contrast(1);");

      document.getElementsByClassName("Rectangle_41")[0].setAttribute("style", "filter: contrast(0.9);");
      document.getElementsByClassName("Rectangle_42")[0].setAttribute("style", "filter: contrast(0.9);");

      document.getElementById("x4__").setAttribute("style", "filter: contrast(0.4);");
      document.getElementById("x3__").setAttribute("style", "filter: contrast(0.4);");

      // making sure Y2 is accesable

      document.getElementsByClassName("Y2")[0].removeAttribute("disabled");
      document.getElementsByClassName("Y2")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementById("y2").setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("Rectangle_332I")[0].removeAttribute("disabled");
      document.getElementsByClassName("Rectangle_332I")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementById("y2___I").setAttribute("style", "filter: contrast(1);");
      document.getElementsByClassName("Rectangle_35")[0].setAttribute("style", "filter: contrast(1);");
      document.getElementById("_s___").setAttribute("style", "filter: contrast(1);");
    }
  }
}
