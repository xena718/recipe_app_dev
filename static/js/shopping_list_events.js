
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
