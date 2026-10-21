const racer1 = document.getElementById('racer1');
const racer2 = document.getElementById('racer2');
const racer3 = document.getElementById('racer3');

const sprite1 = racer1.querySelector('img');
const sprite2 = racer2.querySelector('img');
const sprite3 = racer3.querySelector('img');

const startBtn = document.getElementById('startBtn');
const resetBtn = document.getElementById('resetBtn');
const resultEl = document.getElementById('result');

const sprites1 = [
  'img/flash/flash1.png',
  'img/flash/flash2.png',
  'img/flash/flash3.png',
  'img/flash/flash4.png',
  'img/flash/flash5.png',
  'img/flash/flash6.png',
  'img/flash/flash7.png',
  'img/flash/flash8.png'
];

const sprites2 = [
  'img/reverse_flash/reverse_flash1.png',
  'img/reverse_flash/reverse_flash2.png',
  'img/reverse_flash/reverse_flash3.png',
  'img/reverse_flash/reverse_flash4.png',
  'img/reverse_flash/reverse_flash5.png',
  'img/reverse_flash/reverse_flash6.png'
];

const sprites3 = [
  'img/godspeed/godspeed1.png',
  'img/godspeed/godspeed2.png',
  'img/godspeed/godspeed3.png',
  'img/godspeed/godspeed4.png',
  'img/godspeed/godspeed5.png',
  'img/godspeed/godspeed6.png',
  'img/godspeed/godspeed7.png',
  'img/godspeed/godspeed8.png'
];

let pos1 = 0;
let pos2 = 0;
let pos3 = 0;

let frame1 = 0;
let frame2 = 0;
let frame3 = 0;

let raceInterval = null;
let animationInterval = null;
let finished = false;

function trackWidth(el){
  return el.parentElement.clientWidth - el.clientWidth - 12;
}

function updatePositions(){
  racer1.style.left = pos1 + 'px';
  racer2.style.left = pos2 + 'px';
  racer3.style.left = pos3 + 'px';
}

function animateRacers(){
  frame1 = (frame1 + 1) % sprites1.length;
  frame2 = (frame2 + 1) % sprites2.length;
  frame3 = (frame3 + 1) % sprites3.length;

  sprite1.src = sprites1[frame1];
  sprite2.src = sprites2[frame2];
  sprite3.src = sprites3[frame3];
}

function resetRace(){
  clearInterval(raceInterval);
  clearInterval(animationInterval);
  raceInterval = null;
  animationInterval = null;
  finished = false;
  pos1 = 0;
  pos2 = 0;
  pos3 = 0;
  frame1 = 0;
  frame2 = 0;
  frame3 = 0;
  sprite1.src = sprites1[0];
  sprite2.src = sprites2[0];
  sprite3.src = sprites3[0];
  updatePositions();
  resultEl.textContent = '';
  resultEl.className = 'result';
  startBtn.disabled = false;
  startBtn.textContent = 'Iniciar corrida';
}

function startRace(){
  if (raceInterval || finished) return;

  startBtn.disabled = true;
  startBtn.textContent = 'Corrida em andamento...';
  resultEl.textContent = '';
  resultEl.className = 'result';

  animationInterval = setInterval(() => {
    animateRacers();
  }, 90);

  raceInterval = setInterval(() => {
    const max1 = trackWidth(racer1);
    const max2 = trackWidth(racer2);
    const max3 = trackWidth(racer3);

    pos1 = Math.min(pos1 + Math.floor(Math.random() * 21) + 5, max1);
    pos2 = Math.min(pos2 + Math.floor(Math.random() * 21) + 5, max2);
    pos3 = Math.min(pos3 + Math.floor(Math.random() * 21) + 5, max3);

    updatePositions();

    const reached1 = pos1 >= max1;
    const reached2 = pos2 >= max2;
    const reached3 = pos3 >= max3;

    if (reached1 || reached2 || reached3){
      clearInterval(raceInterval);
      clearInterval(animationInterval);
      raceInterval = null;
      animationInterval = null;
      finished = true;
      startBtn.disabled = true;
      startBtn.textContent = 'Corrida finalizada';

      if (reached1 && reached2 && reached3){
        resultEl.textContent = 'Empate!';
      } else if (reached1){
        resultEl.textContent = 'Flash venceu a corrida!';
        resultEl.classList.add('win1');
      } else if (reached2) {
        resultEl.textContent = 'Flash Reverso venceu a corrida!';
        resultEl.classList.add('win2');
      } else {
        resultEl.textContent = 'Godspeed venceu a corrida!';
        resultEl.classList.add('win3');
      }
    }
  }, 200);
}

startBtn.addEventListener('click', startRace);
resetBtn.addEventListener('click', resetRace);
window.addEventListener('resize', updatePositions);

updatePositions();
