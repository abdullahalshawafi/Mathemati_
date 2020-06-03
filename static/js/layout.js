new WOW().init();

document.getElementById('clear').addEventListener('click', function () {
  inputs = document.getElementsByTagName("input");
  console.log(inputs);
  lengthInputs = inputs.length;
  for (var i = 0; i < lengthInputs; i++) {
    if (!inputs[i].disabled) {
      switch (inputs[i].type) {
        case 'text':
          inputs[i].value = '';
          break;
        case 'radio':
          inputs[i].checked = false;
          break;
        default:
          break;
      }
    }
  }
});
