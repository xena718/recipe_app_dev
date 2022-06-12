let currentScrollPosition = 0;
let scrollAmount = 320;

const sCont = document.querySelector(".cuisines-container");
const hScroll = document.querySelector(".horizontal-scroll");
let maxScroll = -sCont.offsetWidth+ hScroll.offsetWidth;
function scrollHonrizontally(val){
    currentScrollPosition += (val*scrollAmount);
    if (currentScrollPosition >0){
        currentScrollPosition = 0;
    }
    if (currentScrollPosition<maxScroll){
        currentScrollPosition = maxScroll;
    }
    sCont.style.left = currentScrollPosition + 'px';
}