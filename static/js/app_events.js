'use strict';

// ## the following chunk is to add and remove recipe to user's collection 
// by clicking heart and unheart button on the top right of recipe card##

// document.getElementsByClassName("save-remove-btn") also works
const saveRemoveBtns = document.querySelectorAll('.save-remove-btn')

for (const saveRemoveBtn of saveRemoveBtns) {

    saveRemoveBtn.addEventListener('click',evt =>{
    // console.log(btn)
    const addRemoveToServer ={recipeId: saveRemoveBtn.dataset.recipeId};
    console.log(addRemoveToServer);

    fetch('/save-remove',{
        method: 'POST',
        body: JSON.stringify(addRemoveToServer),
        headers: {
            'Content-Type': 'application/json',
            },
    })
    .then(response => response.text())
    .then(serverData => {
        // const icon = btn.children[0] # this works, but only when icon is the first child.
        const icon = saveRemoveBtn.querySelector("i")
        if (serverData === "just_saved"){
            icon.classList.replace("bi-heart", "bi-heart-fill")
        }else if (serverData === "removed_from_saved"){
            icon.classList.replace("bi-heart-fill", "bi-heart")
            console.log("just removed");
        }else if(serverData === "not_logged_in"){
            alert("please log in first to add ingredients to shopping list")

        }
    });
    // catch errors when server is down for example. 
    // recipe is deleted by user A while user b is trying to save the recipe.

    });

}

// ## the following chunk is to remove a recipe from user's collection at saved_recipe homepage. ##

const removeBtns = document.querySelectorAll(".remove-btn")
for (const removeBtn of removeBtns){
    removeBtn.addEventListener('click', evt =>{
    const removeToServer ={recipeId: removeBtn.dataset.recipeId};
    const allCurrentRecipeCardDivs = document.querySelectorAll(".recipe-card-div");
    document.querySelector("#saved-recipe-quantity").innerHTML=allCurrentRecipeCardDivs.length-1;

    fetch('/remove',{
        method: 'POST',
        body: JSON.stringify(removeToServer),
        headers: {
            'Content-Type': 'application/json',
            },
    })
    
    // removeBtn.closest(".recipe-card-div").remove();
    .then(response => response.text())
    .then(serverData => {
        const recipeCardDiv = removeBtn.closest(".recipe-card-div");
        // console.log(recipeCardDiv)
        if (serverData === "removed_from_saved"){
            recipeCardDiv.remove();
            console.log("just removed");
            // const allCurrentRecipeCardDivs = document.querySelectorAll(".saved-recipe-quantity");
            // document.querySelector("#saved-recipe-quantity").innerHTML=allCurrentRecipeCardDivs.length;
        }

    });

    });

}

// below is for removing recipe and update shopping list on shopping list page 
const removeRecipeSLBtns = document.querySelectorAll(".recipe-remove-btn-in-shoppinglist")
for (const removeRecipeSLBtn of removeRecipeSLBtns){
    removeRecipeSLBtn.addEventListener('click', evt =>{
    const infoToServer ={recipeId: removeRecipeSLBtn.dataset.recipeId};
    const allCurrentShoppingRecipes = document.querySelectorAll(".recipe-card-div");
    document.querySelector("#shopping-recipe-quantity").innerHTML=allCurrentShoppingRecipes.length-1;

    fetch('/remove-shopping-recipe',{
        method: 'POST',
        body: JSON.stringify(infoToServer),
        headers: {
            'Content-Type': 'application/json',
            },
    })
    
    .then(response => response.text())
    .then(serverData => {
        const shoppingRecipeCardDiv = removeRecipeSLBtn.closest(".recipe-card-div");
        // console.log(recipeCardDiv)
        if (serverData === "removed_from_shoppinglist"){
            shoppingRecipeCardDiv.remove();
            // shoppingRecipeCardDiv.style.display= "none";
            window.location.reload();

            console.log("just removed");
            // const allCurrentRecipeCardDivs = document.querySelectorAll(".saved-recipe-quantity");
            // document.querySelector("#saved-recipe-quantity").innerHTML=allCurrentRecipeCardDivs.length;
        }

    });

    });

}


// Carousel slide for recipe cards 

let currentScrollPosition = 0;
let scrollAmount = 800;

const sCont = document.querySelector(".recipes-cards-slide-container");
// const sCont = document.querySelector(".recipe-card-div-in-carousel");

const hScroll = document.querySelector(".recipe-card-horizontal-scroll");
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


