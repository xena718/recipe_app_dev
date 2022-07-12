
'use strict';

// to remove repeated recipe name under an ingredient in shopping list page

// const ingredientRecipesDivs = document.querySelectorAll(".ingredient-associated-recipes-div");
// for (const ingredientRecipesDiv of ingredientRecipesDivs){
//     // console.log(ingredientRecipesDiv.childElementCount);
//     while (ingredientRecipesDiv.childElementCount >=2 ){
        
//         ingredientRecipesDiv.querySelector("a").remove();
//     }
// };


// below is for removing recipe and update shopping list on shopping list page 
const removeRecipeSLBtns = document.querySelectorAll(".recipe-remove-btn-in-shoppinglist")
for (const removeRecipeSLBtn of removeRecipeSLBtns){
    removeRecipeSLBtn.addEventListener('click', evt =>{
    const infoToServer ={recipeId: removeRecipeSLBtn.dataset.recipeId};
    const allCurrentShoppingRecipes = document.querySelectorAll(".shopping-recipe-card-div");
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
        const shoppingRecipeCardDiv = removeRecipeSLBtn.closest(".shopping-recipe-card-div");
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

// to remove comma at the end of the ingredient quantity span
const allIngredientQuantitySpans = document.querySelectorAll(".ingredient-quantities-span");
for ( const ingredientQuantitySpan of allIngredientQuantitySpans){
    const currentText = ingredientQuantitySpan.innerText;
    ingredientQuantitySpan.innerText = currentText.slice(0,-1);
    // console.log(ingredientQuantitySpan.innerText.length);
    // what learned here: .innerHTML is a much longer string than .innerText. innerHTML doesn't work for cases here.
}

// for text shopping list to user

const textShoppingListBts = document.querySelector(".text-shoppinglist-btn")

textShoppingListBts.addEventListener('click',evt =>{
    const ingredientsDivs = document.querySelectorAll(".ingredient-item");
    const shoppingListToServer ={"ingredients":[]};

    for (const ingredientDiv of ingredientsDivs){
        // console.log(ingredientDiv.innerText);
        shoppingListToServer.ingredients.push(ingredientDiv.innerText);
    }
    // console.log(shoppingListToServer);
    // const catergoryDivs = document.querySelectorAll(".ingredient-category-name-span");
    // for (const catergoryDiv of catergoryDivs){
    //     // console.log(catergoryDiv.innerText);
    //     // const ingredientsDivs = catergoryDiv.closest(".ingredient-items");
    //     // for(const ingredientDiv of ingredientsDivs){
    //     // console.log(ingredientDiv.innerText);

    //     // }

    // }


    fetch('/text-shoppinglist-to-user',{
        method: 'POST',
        body: JSON.stringify(shoppingListToServer),
        headers: {
            'Content-Type': 'application/json',
            },
    })
    .then(response => response.text())
    .then(serverData => {
        // const icon = btn.children[0] # this works, but only when icon is the first child.
        if (serverData === "text_sent"){
            document.querySelector(".text-shoppinglist-btn").innerText ="Just Sent!";
        }
    });

})


// Carousel slide for shopping recipe cards 

// let currentScrollPosition = 0;
// let scrollAmount = 800;

// const sCont = document.querySelector(".recipes-cards-slide-container");
// // const sCont = document.querySelector(".recipe-card-div-in-carousel");

// const hScroll = document.querySelector(".shopping-recipe-card-horizontal-scroll");
// let maxScroll = -sCont.offsetWidth+ hScroll.offsetWidth; 

// function scrollHonrizontally(val){
//     currentScrollPosition += (val*scrollAmount);
//     if (currentScrollPosition >0){
//         currentScrollPosition = 0;
//     }
//     if (currentScrollPosition<maxScroll){
//         currentScrollPosition = maxScroll;
//     }
//     sCont.style.left = currentScrollPosition + 'px';
// }

