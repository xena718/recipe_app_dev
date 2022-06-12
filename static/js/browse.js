let curentScrollPosition =0;
let scrollAmount = 320;

const sCont = document.querySelector(".cuisines-container");
const hScroll = document.querySelector(".horizontal-scroll");
let maxScroll = -sCont.offsetWidth+ hScroll.offsetWidth;
function scrollHonrizontally(val){
    curentScrollPosition += (val*scrollAmount);
    sCont.style.left = currentScrollPosition + 'px';
}