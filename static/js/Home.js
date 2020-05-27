$(window).load(function () {
  $("body").removeClass("Body-Class");
});

function ForwardAnimation(el) {
  const imagePath = 'static/HoverAnimations/' + el.id + '/' + el.id + '00';
  const totalFrames = 71;
  const timePerFrame = 10;
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

  console.log(el.id);
}

function BackwardAnimation(el) {
  const imagePath = 'static/HoverAnimations/' + el.id + '/' + el.id + '00';
  const timePerFrame = 15;
  let timeWhenLastUpdate;
  let timeFromLastUpdate;
  let length = document.getElementById(el.id + "0000").src.length;
  let frameNumber = parseInt(document.getElementById(el.id + "0000").src[length - 6] + document.getElementById(el.id + "0000").src[length - 5]);
  console.log(parseInt(document.getElementById(el.id + "0000").src[length - 6] + document.getElementById(el.id + "0000").src[length - 5]));

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

  console.log(el.id + ".b");
}
