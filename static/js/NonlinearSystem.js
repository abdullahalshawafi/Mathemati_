var parameters = {
    target: '#myFunction',
    data: [{
        fn: '',
        color: "#eb00ff",
        fnType: 'implicit'
    },
    {
        fn: '',
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

// functionPlot(parameters);

function addtograph() {
    var MethodFixedPoint = document.getElementsByName("Method")[1];
    if (MethodFixedPoint.checked) {
        if (document.getElementsByClassName("Rectangle_19")[0].value && document.getElementsByName("Dim")[0].checked) {
            parameters.data[0].fn = document.getElementsByClassName("Rectangle_19")[0].value + '-x';
        }
        if (document.getElementsByClassName("Rectangle_29")[0].value && document.getElementsByName("Dim")[0].checked) {
            parameters.data[1].fn = document.getElementsByClassName("Rectangle_29")[0].value + '-y';
        }
    } else {
        if (document.getElementsByClassName("Rectangle_19")[0].value && document.getElementsByName("Dim")[0].checked) {
            parameters.data[0].fn = document.getElementsByClassName("Rectangle_19")[0].value;
        }
        if (document.getElementsByClassName("Rectangle_29")[0].value && document.getElementsByName("Dim")[0].checked) {
            parameters.data[1].fn = document.getElementsByClassName("Rectangle_29")[0].value;
        }
    }
    functionPlot(parameters);
}

    window.onload = function () {
        DimInput();
        addtograph();
        MethodSelection();

    };

    function MethodSelection() {
        var MethodFixedPoint = document.getElementsByName("Method")[1];

        if (MethodFixedPoint.checked) {
            document.getElementById("F_x_y_z____0__").innerHTML = "x =";
            document.getElementById("G_x_y_z____0__").innerHTML = "y =";
            document.getElementById("H_x_y_z____0__").innerHTML = "z =";
        } else {
            document.getElementById("F_x_y_z____0__").innerHTML = "F(x,y,z) = 0 =";
            document.getElementById("G_x_y_z____0__").innerHTML = "G(x,y,z) = 0 =";
            document.getElementById("H_x_y_z____0__").innerHTML = "H(x,y,z) = 0 =";
        }
    }

    function DimInput() {
        var Dim2 = document.getElementsByName("Dim")[0].checked;
        var MethodFixedPoint = document.getElementsByName("Method")[1].checked;
        if (Dim2) {
            document.getElementsByClassName("Rectangle_30")[0].setAttribute("disabled", "true");
            document.getElementsByClassName("Rectangle_30")[0].setAttribute("style", "background: #303030; color: #999999; text-align: left;");
            document.getElementsByClassName("Rectangle_44")[2].setAttribute("disabled", "true");
            document.getElementsByClassName("Rectangle_44")[2].setAttribute("style", "background: #303030; color: #999999;");
            document.getElementById("H_x_y_z____0__").setAttribute("style", "color: #999999; text-decoration: line-through;");
            if (!MethodFixedPoint) {
                document.getElementById("F_x_y_z____0__").innerHTML = "F(x,y) = 0 =";
                document.getElementById("G_x_y_z____0__").innerHTML = "G(x,y) = 0 =";
            } else {
                document.getElementById("F_x_y_z____0__").innerHTML = "x =";
                document.getElementById("G_x_y_z____0__").innerHTML = "y =";
            }
            document.getElementById("z___").setAttribute("style", "color: #999999; text-decoration: line-through; ");
            document.getElementsByClassName("inChars")[2].setAttribute("style", "color: #999999; text-decoration: line-through;");
            document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "background: #303030; color: #999999;");
        } else {
            document.getElementsByClassName("Rectangle_30")[0].removeAttribute("disabled");
            document.getElementsByClassName("Rectangle_30")[0].setAttribute("style", "background: #282828; color: #FFFFFF; text-align: left;");
            document.getElementsByClassName("Rectangle_44")[2].removeAttribute("disabled");
            document.getElementsByClassName("Rectangle_44")[2].setAttribute("style", "background: #282828; color: #FFFFFF;");
            document.getElementById("H_x_y_z____0__").setAttribute("style", "color: white; text-decoration: normal;");
            document.getElementsByClassName("inChars")[2].setAttribute("style", "color: white; text-decoration: normal;");
            document.getElementById("z___").setAttribute("style", "color: white; text-decoration: normal;");
            document.getElementsByClassName("Rectangle_34")[0].setAttribute("style", "background: #282828; color: #FFFFFF;");
            if (!MethodFixedPoint) {
                document.getElementById("F_x_y_z____0__").innerHTML = "F(x,y,z) = 0 =";
                document.getElementById("G_x_y_z____0__").innerHTML = "G(x,y,z) = 0 =";
            } else {
                document.getElementById("F_x_y_z____0__").innerHTML = "x =";
                document.getElementById("G_x_y_z____0__").innerHTML = "y =";
            }
        }
    }
