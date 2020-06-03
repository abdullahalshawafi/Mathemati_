
x = 0;
var parameters = {
    target: '#myFunction',
    data: [
    ],
    grid: true,
    yAxis: { domain: [-3, 3] },
    xAxis: { domain: [-3, 3] },
    height: window.innerWidth / 100 * 18.45,
    width: window.innerWidth / 100 * 19.13
};
functionPlot(parameters);

var x = [];



function Expand(el, x, intervals, eq) {

    // var con = document.getElementsByClassName("Quadratic")[0];

    con = el.parentElement.parentElement;

    console.log(con.childNodes[3].innerHTML);

    if (!con.childNodes[3].innerHTML.includes("label")) {
        con.innerHTML = con.innerHTML.replace('width="25.98vw" height="4.56vw"', "width='25.98vw' height='" + (4.6 + x * 3) + "vw'");
        con.innerHTML = con.innerHTML.replace('viewBox="127.353 308 21.741 23.895"', 'viewBox="127.353 288 21.741 23.895"');
        con.childNodes[3].setAttribute("style", "height:" + (x * 3 + 9) + "vw");
        for (var i = 0; i < x; i++) {
            var div = document.createElement("div");
            var input = document.createElement("input");
            var label = document.createElement("label");
            var span = document.createElement("span");

            input.setAttribute("type", "text");
            input.setAttribute("name", "interval" + i);
            input.setAttribute("value", eq[i]);
            input.setAttribute("disabled", true);


            span.innerHTML = intervals[i];

            label.setAttribute("for", "interval" + i);

            div.style.cssText = "margin: 1.2vw; color: white; top: 3.5vw; position: relative; width: 24vw; font-size: calc(20vw/" + span.innerHTML.length + ");";

            input.style.cssText = "text-align: left; margin-right: 1vw; width: 15vw;";

            con.childNodes[3].appendChild(div);
            div.appendChild(input);
            div.appendChild(label);
            label.appendChild(span);
        }
        con.innerHTML = con.innerHTML.replace(`<img src="static/Assets/Expand.svg">`, ``);
    }
}