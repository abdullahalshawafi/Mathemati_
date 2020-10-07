var parameters = {
    target: '#myFunction',
    data: [
        {
            fn: '-1000000',
            color: "#000000",
            graphType: 'polyline'
        },
        {
            fn: '-1000000',
            color: "#0000FF",
            graphType: 'polyline'
        },
        {
            points: [],
            fnType: 'points',
            graphType: 'scatter',
            color: "#000000"

        }
    ],
    grid: false,
    yAxis: { domain: [-10, 10] },
    xAxis: { domain: [-10, 10] },
    height: window.innerWidth / 100 * 18.45,
    width: window.innerWidth / 100 * 19.13
}

document.getElementById('clear').addEventListener('click', function () {
    parameters.data[2].points = [];
    functionPlot(parameters);
});

function Scatter(el) {
    var elx = el.parentElement.parentElement.childNodes[1].childNodes[0];
    var ely = el.parentElement.parentElement.childNodes[3].childNodes[0];


    if (elx.value && ely.value) {
        var point = [parseFloat(elx.value), parseFloat(ely.value)];
        parameters.data[2].points.push(point);
    }

    functionPlot(parameters);
};



functionPlot(parameters);

function addtograph() {
    if (document.getElementsByClassName("Rectangle_Essam")[0].value) {
        var func = document.getElementsByClassName("Rectangle_Essam")[0].value;
        for (let i = 0; i < 9; i++)
            func = func.replace('**', '^');
        parameters.data[0].fn = func;
    }
    if (document.getElementsByClassName("Rectangle_32")[0].value) {
        var func = document.getElementsByClassName("Rectangle_32")[0].value;
        for (let i = 0; i < 9; i++)
            func = func.replace('**', '^');
        if (func !== "Unable to converge.")
          parameters.data[1].fn = func;
    }
    functionPlot(parameters);
}

window.onload = function () {
    addtograph();
    for(var i = 0; i <= 14; i++){
        Scatter(document.getElementsByName("x_coordinates" + i)[0]);
        Scatter(document.getElementsByName("y_coordinates" + i)[0]);
    }
};

function substitute(el) {
    var x = parseFloat(el.value);
    var F1 = document.getElementsByClassName('Rectangle_Essam')[0].value;
    var F2 = document.getElementsByClassName('Rectangle_32')[0].value !== "Unable to converge." ? document.getElementsByClassName('Rectangle_32')[0].value : "";

    if (F2) {
    if (eval(F1) != "NaN" && eval(F2) != "NaN")
        document.getElementsByClassName('Rectangle_42')[0].value = `Ya=${eval(F2).toFixed(4)}, Ys=${eval(F1).toFixed(4)}`;
    else
        document.getElementsByClassName('Rectangle_42')[0].value = '';
    } else document.getElementsByClassName('Rectangle_42')[0].value = `Ys=${eval(F1).toFixed(4)}`;
}
