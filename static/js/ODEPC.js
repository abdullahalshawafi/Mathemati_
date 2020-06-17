function DimInput() {
  var Dim2 = document.getElementsByName("Dim")[0].checked;
  var Pair1 = document.getElementsByName("Method")[0].checked || document.getElementsByName("Method")[1].checked;
  if (Dim2) {
    document.getElementsByClassName("Rectangle_17")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_17")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_21")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_21")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_24")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_24")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_25")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_25")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_26")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_26")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_27")[0].setAttribute("disabled", "true");
    document.getElementsByClassName("Rectangle_27")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_12")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_12_ba")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_12_bk")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_10_bi")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_11_bj")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_12_bk")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_13_bl")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_14_bm")[0].setAttribute("style", "background: #303030; color: #999999;");
  }
  else {
    document.getElementsByClassName("Rectangle_17")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_17")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_21")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_21")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_24")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_24")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_25")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_25")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_26")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_26")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_27")[0].removeAttribute("disabled");
    document.getElementsByClassName("Rectangle_27")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_12")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_12_ba")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_12_bk")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_10_bi")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_11_bj")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementsByClassName("Rectangle_13_bl")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_14_bm")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_12_bk")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

  }
  if (Pair1) {
    document.getElementsByClassName("Rectangle_10_")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_11_")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_12_ba")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_13_bb")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_14_bc")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_10_bi")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_11_bj")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_12_bk")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_13_bl")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementsByClassName("Rectangle_14_bm")[0].setAttribute("style", "background: #303030; color: #999999;");
    document.getElementById("_________________________").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("_s_________________________").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("_________________________bg").setAttribute("style", "color: #999999; text-decoration: line-through; ");
    document.getElementById("_s_________________________bh").setAttribute("style", "color: #999999; text-decoration: line-through; ");

  }
  else {
    document.getElementsByClassName("Rectangle_10_")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_11_")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_13_bb")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    document.getElementsByClassName("Rectangle_14_bc")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

    document.getElementById("_________________________").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("_s_________________________").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("_________________________bg").setAttribute("style", "color: white; text-decoration: normal; ");
    document.getElementById("_s_________________________bh").setAttribute("style", "color: white; text-decoration: normal; ");

    if (!Dim2) {
      document.getElementsByClassName("Rectangle_12_bk")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
      document.getElementsByClassName("Rectangle_12_ba")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
      document.getElementsByClassName("Rectangle_10_bi")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
      document.getElementsByClassName("Rectangle_11_bj")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");

      document.getElementsByClassName("Rectangle_13_bl")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
      document.getElementsByClassName("Rectangle_14_bm")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
    }
  }

}