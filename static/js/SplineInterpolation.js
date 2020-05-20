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

function Expand(el, x) {

  // var con = document.getElementsByClassName("Quadratic")[0];

  con = el.parentElement.parentElement;
  // el.classList.toggle("CC")

  if (!el.classList.contains("CC")) {
    el.classList.add("CC");
    con.innerHTML = con.innerHTML.replace('width="25.98vw" height="4.56vw"', "width='25.98vw' height='" + (4.6 + x * 3) + "vw'");
    con.innerHTML = con.innerHTML.replace('viewBox="127.353 308 21.741 23.895"', 'viewBox="127.353 288 21.741 23.895"');
    con.childNodes[3].setAttribute("style", "height:" + (x * 3 + 9) + "vw");
    for (var i = 0; i < x; i++) {
      var div = document.createElement("div");
      var input = document.createElement("input");
      var label = document.createElement("label");
      var span = document.createElement("span");

      input.setAttribute("type", "text");
      input.setAttribute("name", "interval" + i)

      span.innerHTML = '[' + i + ', ' + (i + 1) + ']';

      label.setAttribute("for", "interval" + i);

      div.style.cssText = "margin: 1.2vw; color: white; top: 3.5vw; position: relative; width: 24vw;";

      input.style.cssText = "text-align: left; margin-right: 1vw; width: 19vw;";

      con.childNodes[3].appendChild(div);
      div.appendChild(input);
      div.appendChild(label);
      label.appendChild(span);
    }
    con.innerHTML = con.innerHTML.replace(`<img src="static/Assets/Expand.svg">`, `<img src="static/Assets/Expand.svg" style="transform: scaleY(-1)">`);
  }
  else {

    con.innerHTML = con.innerHTML.replace('width="25.98vw" height="' + (4.6 + x * 3) + 'vw"', 'width="25.98vw" height="4.56vw"');
    con.innerHTML = con.innerHTML.replace('viewBox="127.353 288 21.741 23.895"', 'viewBox="127.353 308 21.741 23.895"');
    con.childNodes[3].setAttribute("style", "height:" + 9 + "vw");
    con.childNodes[3].innerHTML = `<button class="Expand" onclick="Expand(this, 9)">	<img src="static/Assets/Expand.svg"> 	</button> <div id="Best_fitting_curves_are__"> 	<span>` + con.className + ' Spline: </span> 	</div> 	<div id="R___"> 		<span>' + con.className[0] + ' ( </span> 	</div> <div id="____"> <span>) = </span> </div> <input type="text" class="Rectangle_41" /> <input type="text" class="Rectangle_42" />';

  }
}
