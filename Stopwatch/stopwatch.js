let timerdisplay = document.querySelector('.timerdisplay');
let stopbtn = document.getElementById('stopbtn');
let startbtn = document.getElementById('startbtn');
let resetbtn = document.getElementById('resetbtn');

let msec = 0;
let secs = 0; 
let mins = 0;

let timerId = null;

startbtn.addEventListener('click', function() {
    if (timerId !== null) {
        clearInterval(timerId);
    }
    timerId = setInterval(startTimer, 10);
});

stopbtn.addEventListener('click', function() {
    clearInterval(timerId);
});

resetbtn.addEventListener('click', function() {
    clearInterval(timerId);
    msec = 0;
    secs = 0;
    mins = 0;
    timerdisplay.innerHTML = '00 : 00 : 00';
});

function startTimer() {
    msec++;
    if (msec == 100) {
        msec = 0;
        secs++;
        if (secs == 60) {
            secs = 0;
            mins++;
        }
    }

    let msecstring = msec < 10 ? '0' + msec : msec;
    let secsstring = secs < 10 ? '0' + secs : secs;
    let minsstring = mins < 10 ? '0' + mins : mins;

    timerdisplay.innerHTML = minsstring + ' : ' + secsstring + ' : ' + msecstring;
}
