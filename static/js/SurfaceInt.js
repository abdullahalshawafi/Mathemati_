

function substitute(el) {
    var x = parseFloat(document.getElementsByClassName('Rectangle_41')[0].value);
    var y = parseFloat(el.value);
    var F = document.getElementsByClassName('Rectangle_32')[0].value;
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

