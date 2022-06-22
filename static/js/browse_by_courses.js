let currentBrowseByCourseScrollPosition = 0;
let BrowseByCourseScrollAmount = 800;

const sContBrowseByCourse = document.querySelector(".Courses-container");
const hScrollBrowseByCourse = document.querySelector(".browse-by-courses-horizontal-scroll");
let maxScrollBrowseByCourse = -sContBrowseByCourse.offsetWidth+ hScrollBrowseByCourse.offsetWidth; 
function browseByCourseScrollHonrizontally(val){
    currentBrowseByCourseScrollPosition += (val*BrowseByCourseScrollAmount);
    if (currentBrowseByCourseScrollPosition >0){
        currentBrowseByCourseScrollPosition = 0;
    }
    if (currentBrowseByCourseScrollPosition<maxScrollBrowseByCourse){
        currentBrowseByCourseScrollPosition = maxScrollBrowseByCourse;
    }
    sContBrowseByCourse.style.left = currentBrowseByCourseScrollPosition + 'px';
}
