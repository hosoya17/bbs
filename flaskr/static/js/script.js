'use strict';
const body = document.querySelector('body');
const text = document.querySelector('.text');
const a = document.querySelector('a');

const time = () => {
    const now = new Date();
    let hour = now.getHours();

    if (hour >= 19 || hour <= 5) {
        body.style.backgroundImage = 'linear-gradient(90deg, rgba(0,33,175,1) 0%, rgba(0,1,54,1) 100%)';
        text.style.color = 'green';
        a.style.color = 'yellow';
    } else if (hour >= 6 && hour <= 15) {
        body.style.backgroundImage = 'linear-gradient(90deg, rgba(65, 164, 253, 1), rgba(14, 244, 255, 1))'
    } else if (hour >= 16 && hour <= 18) {
        body.style.backgroundImage = 'linear-gradient(90deg, rgba(255,183,0,1) 0%, rgba(255,32,32,1) 100%)';
    }
    
    requestAnimationFrame(time);
};
time();
