const texts = {
  button1: {
    h1: "Button A",
    span: 'There are two momentary push buttons, you can use these in any of your projects to change modes, indicate when to start or stop, modify behavior, etc.'
  },
  slide: {
    h1: 'Slide Switch',
    span: 'The slide switch is near the center. There is a little nub that you can slide left or right.'
  },
  neopixel: {
    h1: 'NeoPixels',
    span: 'There are 10 NeoPixels on the board that can display any color.'
  },
  on: {
    h1: 'Green "On" LED',
    span: 'This LED indicates that the Circuit Playground Express is powered.'
  },
  d13: {
    h1: 'Red "D13" LED',
    span: 'This LED is used for basic blinking.'
  },
  button2: {
    h1: 'Button B',
    span: 'There are two momentary push buttons, you can use these in any of your projects to change modes, indicate when to start or stop, modify behavior, etc.'
  },
  reset: {
    h1: 'Reset Button',
    span: 'The reset button is at the dead center of the Circuit Playground Express. It re-starts your device (turning it off and back on).'
  },
  speaker: {
    h1: 'Built-in Speaker',
    span: 'This mini speaker can play basic tones and audio files.'
  },
};

const blue = '#4C7EF3';
const black = '#000000';

window.onload = function () {

    Array.prototype.forEach.call(document.querySelectorAll('#selectors *'), (elem) => {
      elem.addEventListener(
        'mouseover',
        (event) => {
          const innerDot = document.querySelector(`#dot-${event.target.id} #inner`)
          innerDot.setAttribute('fill', blue)
          elem.setAttribute('fill-opacity', 0.25);
          replaceCaption(texts[event.target.id].h1, texts[event.target.id].span)

        });
      elem.addEventListener(
        'mouseout',
        (event) => {
          const innerDot = document.querySelector(`#dot-${event.target.id} #inner`)
          innerDot.setAttribute('fill', black)
          elem.setAttribute('fill-opacity', 0);
        });
      });
}

/********
Helper Functions
********/

function replaceCaption(header, body) {
  const a = document.querySelector('#caption-a');
  const b = document.querySelector('#caption-b');
  if (a.classList.contains('hidden')) {
    a.querySelector('h1').innerText = header;
    a.querySelector('span').innerText = body;

  } else {
    b.querySelector('h1').innerText = header;
    b.querySelector('span').innerText = body;

  }
  a.classList.toggle('hidden');
  b.classList.toggle('hidden');
}