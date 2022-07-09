
'use strict';

// to remove repeated recipe name under an ingredient in shopping list page

// const ingredientRecipesDivs = document.querySelectorAll(".ingredient-associated-recipes-div");
// for (const ingredientRecipesDiv of ingredientRecipesDivs){
//     // console.log(ingredientRecipesDiv.childElementCount);
//     while (ingredientRecipesDiv.childElementCount >=2 ){
        
//         ingredientRecipesDiv.querySelector("a").remove();
//     }
// };


// to remove comma at the end of the ingredient quantity span
const allIngredientQuantitySpans = document.querySelectorAll(".ingredient-quantities-span");
for ( const ingredientQuantitySpan of allIngredientQuantitySpans){
    const currentText = ingredientQuantitySpan.innerText;
    ingredientQuantitySpan.innerText = currentText.slice(0,-1);
    console.log(ingredientQuantitySpan.innerText.length);
    // what learned here: .innerHTML is a much longer string than .innerText. innerHTML doesn't work for cases here.


}