let currentBrowseByCuisineScrollPosition = 0;
let BrowseByCuisineScrollAmount = 800;

const sContBrowseByCuisine = document.querySelector(".cuisines-container");
const hScrollBrowseByCuisine = document.querySelector(".browse-by-cuisines-horizontal-scroll");
let maxScrollBrowseByCuisine = -sContBrowseByCuisine.offsetWidth+ hScrollBrowseByCuisine.offsetWidth; 
function browseByCuisineScrollHonrizontally(val){
    currentBrowseByCuisineScrollPosition += (val*BrowseByCuisineScrollAmount);
    if (currentBrowseByCuisineScrollPosition >0){
        currentBrowseByCuisineScrollPosition = 0;
    }
    if (currentBrowseByCuisineScrollPosition<maxScrollBrowseByCuisine){
        currentBrowseByCuisineScrollPosition = maxScrollBrowseByCuisine;
    }
    sContBrowseByCuisine.style.left = currentBrowseByCuisineScrollPosition + 'px';
}
