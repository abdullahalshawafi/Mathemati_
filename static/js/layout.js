new WOW().init();

document.getElementById('clear').addEventListener('click', function () {
  inputs = document.getElementsByTagName("input");
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

function showVideo(url) {
  document.getElementsByTagName('main')[0].style.filter = "blur(0.5vw)";
  document.getElementsByTagName('header')[0].style.filter = "blur(0.5vw)";
  var video = document.getElementsByClassName('video')[0];
  var iframe = document.createElement("iframe");
  iframe.setAttribute("style", "position: absolute; left: 15.5vw; top: 12.2vw; width: 69vw; height: 33vw;");
  iframe.setAttribute("allow", "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture");
  iframe.setAttribute("src", "https://www.youtube.com/embed/" + url);
  iframe.setAttribute("frameborder", "0");
  iframe.setAttribute("allowfullscreen", "1");
  video.appendChild(iframe);
  video.style.display = "block";
}

document.getElementsByClassName('video')[0].addEventListener('click', function () {
  document.getElementsByTagName('main')[0].style.filter = null;
  document.getElementsByTagName('header')[0].style.filter = null;
  var video = document.getElementsByClassName('video')[0];
  video.removeChild(video.childNodes[0]);
  video.style.display = "none";
});
