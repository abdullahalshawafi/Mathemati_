function DimInput() {
  var Milnes = document.getElementsByName("Method")[1].checked;
    if (Milnes) {
        document.getElementById('decimalsORerr').textContent = "Stopping Error = ";
    } else {
        document.getElementById('decimalsORerr').textContent = "No. of decimal digits = ";
    }
}

window.onload = () => {
    DimInput();
}