var parameters = {
    target: '#myFunction',
    data: [
        {
            fn: '-1000000000000000000',
            color: "#FF3300",
            graphType: 'polyline'
        },
        {
            points: [],
            fnType: 'points',
            graphType: 'scatter',
            color: "#000000"

        },
        {
            x: '-1000000',
            y: '-1000000',
            range: [0, 1],
            color: "#FFAA00",
            fnType: 'parametric',
            graphType: 'polyline'
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
    for(var i = 0; i < 20; i++){
        Scatter(document.getElementsByName("X_" + i)[0]);
        Scatter(document.getElementsByName("Y_" + i)[0]);
    }
};
function GetHue(el) {
      x = el.value;
      var elementindex = 3;
      if(el.parentElement.parentElement.childNodes[1].id == "LinesP") elementindex = 1;
      else if(el.parentElement.parentElement.childNodes[1].id == "LinesB") elementindex = 1;

      el.parentElement.parentElement.childNodes[elementindex].setAttribute("style", "filter:hue-rotate(" + (x * 3.6 + 160) + "deg) saturate(1.5) brightness(1.5)");
      el.setAttribute("style", "filter:hue-rotate(" + x * 3.6 + "deg) saturate(1.5) brightness(1.5)");

      var index = 0;
      if(el.parentElement.parentElement.childNodes[elementindex].id == "Points") index = 1;
      else if(el.parentElement.parentElement.childNodes[elementindex].id == "LinesP") index = 0;
      else if(el.parentElement.parentElement.childNodes[elementindex].id == "LinesB") index = 2;

			parameters.data[index].color =  "hsl(" + ((x * 3.6 + 180)) + ", 100%, 30%)";
			functionPlot(parameters);


		}

function Scatter(el) {
    var elx = el.parentElement.parentElement.childNodes[1].childNodes[0];
    var ely = el.parentElement.parentElement.childNodes[3].childNodes[0];

    if (elx.value && ely.value) {
        var point = [parseFloat(elx.value), parseFloat(ely.value)];
        parameters.data[1].points.push(point);
    }

    functionPlot(parameters);
};

function addtograph() {
    if (document.getElementsByClassName("Rectangle_32")[0].value) {
        var func = document.getElementsByClassName("Rectangle_32")[0].value;
        for (let i = 0; i < 9; i++)
            func = func.replace('**', '^');
        parameters.data[0].fn = func;
    }

    if (document.getElementsByClassName("Rectangle_32B")[0].value) {
        var func = document.getElementsByClassName("Rectangle_32B")[0].value;
        for (let i = 0; i < 9; i++)
            func = func.replace('**', '^');
        parameters.data[2].x = func;
    }

    if (document.getElementsByClassName("Rectangle_32D")[1].value) {
        var func = document.getElementsByClassName("Rectangle_32D")[1].value;
        for (let i = 0; i < 9; i++)
            func = func.replace('**', '^');
        parameters.data[2].y = func;
    }
    functionPlot(parameters);
}



function substitute(el, box1="", box2="") {

    if (el.classList[0] != "Rectangle_41B") {
      var x = parseFloat(el.value);
      var F = document.getElementsByClassName(box1)[0].value;
      F = F.replace(/\^/g, '**');

      if (box1 == "Rectangle_32") {
        if (eval(F).toFixed(4) != "NaN")
            document.getElementsByClassName('Rectangle_42')[0].value = eval(F).toFixed(4);
        else
            document.getElementsByClassName('Rectangle_42')[0].value = '';
      } else if (box1 == "Rectangle_32D") {
        if (eval(F).toFixed(4) != "NaN")
            document.getElementsByClassName('Rectangle_42D')[0].value = eval(F).toFixed(4);
        else
            document.getElementsByClassName('Rectangle_42D')[0].value = '';
      }
    } else {
      var t = parseFloat(el.value);
      var x = document.getElementsByClassName(box1)[0].value;
      x = x.replace(/\^/g, '**');
      if (eval(x).toFixed(4) != "NaN")
          document.getElementsByClassName('Rectangle_42B')[0].value = eval(x).toFixed(4);
      else
        document.getElementsByClassName('Rectangle_42B')[0].value = '';

      var y = document.getElementsByClassName(box2)[1].value;
      y = y.replace(/\^/g, '**');
      if (eval(y).toFixed(4) != "NaN") {
        document.getElementsByClassName('Rectangle_42B2')[0].value = eval(y).toFixed(4);
      } else {
        document.getElementsByClassName('Rectangle_42B2')[0].value = '';
      }
    }
}
