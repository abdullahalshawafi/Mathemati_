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

function addtograph() {
    if (document.getElementsByClassName("Rectangle_Essam")[0].value) {
        var func = document.getElementsByClassName("Rectangle_Essam")[0].value;
        for (let i = 0; i < 9; i++)
            func = func.replace('**', '^');
        parameters.data[1].fn = '-y+' + func;
    }
    functionPlot(parameters);
}

window.onload = function () {
    addtograph();
};

function substitute(el) {
    var x = parseFloat(el.value);
    var F = document.getElementsByClassName('Rectangle_Essam')[0].value;
    F = F.replace(/\^/g, '**');
    F = F.replace(/sin/g, 'Math.sin');
    F = F.replace(/cos/g, 'Math.cos');
    F = F.replace(/tan/g, 'Math.tan');
    F = F.replace(/exp/g, 'Math.exp');
    F = F.replace(/log/g, 'Math.log');
    //De7k:
    F = F.replace(/sqrt/g, 'Math.sqrt');
    F = F.replace(/log2/g, '1/Math.log(2) * Math.log');
    F = F.replace(/log10/g, '1/Math.log(10) * Math.log');

    if (eval(F).toFixed(4) != "NaN")
        document.getElementsByClassName('Rectangle_42')[0].value = eval(F).toFixed(4);
    else
        document.getElementsByClassName('Rectangle_42')[0].value = '';
}

function DimInput() {
    var MethodFamily = document.getElementsByName('Method')[2];
    if (!MethodFamily.checked) {
        document.getElementById('R__x____').setAttribute("style", "color: #999999;");
        document.getElementsByClassName('Rectangle_32')[0].setAttribute("style", "background: #303030; text-align: left;");
    } else {
        document.getElementById('R__x____').setAttribute("style", "");
        document.getElementsByClassName('Rectangle_32')[0].setAttribute("style", "text-align: left;");
    }
}
