function ForwardAnimation(el) {
  let elid = el.id;
  if (el.id.includes("_")) {
    elid = el.id.substring(0, el.id.length - 1);
  }
  let imagePath = 'static/HoverAnimations/' + elid + '/' + elid + '00';
  const totalFrames = 71;
  let timePerFrame = 30;
  if (elid == "EP" || elid == "LS") {
    timePerFrame = 15;
  }
  let timeWhenLastUpdate;
  let timeFromLastUpdate;
  let length = document.getElementById(el.id + "0000").src.length;
  let frameNumber = parseInt(document.getElementById(el.id + "0000").src[length - 6] + document.getElementById(el.id + "0000").src[length - 5]);;

  function step(startTime) {
    if (!timeWhenLastUpdate) timeWhenLastUpdate = startTime;

    timeFromLastUpdate = startTime - timeWhenLastUpdate;

    if (timeFromLastUpdate > timePerFrame) {
      if (frameNumber < 10)
        document.getElementById(el.id + "0000").setAttribute('src', imagePath + `0${frameNumber}.png`);
      else
        document.getElementById(el.id + "0000").setAttribute('src', imagePath + `${frameNumber}.png`);
      timeWhenLastUpdate = startTime;

      if (frameNumber >= totalFrames) {
        return;
      } else {
        el.addEventListener("mouseleave", function () { frameNumber = 70; });
        frameNumber = frameNumber + 1;
      }
    }
    requestAnimationFrame(step);

  }
  step(0);


}
function BackwardAnimation(el) {
  let elid = el.id;
  if (el.id.includes("_")) {
    elid = el.id.substring(0, el.id.length - 1);
  }
  let imagePath = 'static/HoverAnimations/' + elid + '/' + elid + '00';
  let timePerFrame = 15;
  if (elid == "EP" || elid == "LS") {
    timePerFrame = 5;
  }
  let timeWhenLastUpdate;
  let timeFromLastUpdate;
  let length = document.getElementById(el.id + "0000").src.length;
  let frameNumber = parseInt(document.getElementById(el.id + "0000").src[length - 6] + document.getElementById(el.id + "0000").src[length - 5]);

  function step(startTime) {
    if (!timeWhenLastUpdate) timeWhenLastUpdate = startTime;

    timeFromLastUpdate = startTime - timeWhenLastUpdate;

    if (timeFromLastUpdate > timePerFrame) {
      if (frameNumber < 10)
        document.getElementById(el.id + "0000").setAttribute('src', imagePath + `0${frameNumber}.png`);
      else
        document.getElementById(el.id + "0000").setAttribute('src', imagePath + `${frameNumber}.png`);
      timeWhenLastUpdate = startTime;

      if (frameNumber <= 0) {
        return;
      } else {
        el.addEventListener("mouseleave", function () { frameNumber = 1; });
        frameNumber = frameNumber - 1;
      }
    }

    requestAnimationFrame(step);
  }

  step(0);

}
