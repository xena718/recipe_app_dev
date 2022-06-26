'use strict';

document.querySelector("#servings-size-form").addEventListener('submit',evt => {
    evt.preventDefault();
    const servingsSize = Number(document.querySelector("#servings-size-input").value);
    const servingsSizeDefault = Number(document.querySelector("#servings-size-input").defaultValue);

    if (servingsSize !== servingsSizeDefault){
        const allIngredientCheckBoxes = document.querySelectorAll(".form-check-input");
        // const ingredient = document.querySelector(".form-check-input").defaultValue;
        // ingredient is a string...
        for ( const ingredientCheckBox of allIngredientCheckBoxes){
            const checkBoxLabel = ingredientCheckBox.nextElementSibling;
            const ingredientQuantity = checkBoxLabel.querySelector(".ingredient-quantity");
            if (ingredientQuantity.innerText !==""){
                // updatedQuantity = servingsSize/servingsSizeDefault*Number(ingredientQuantity.innerText)
                // quantityFraction = fc(updatedQuantity).toFraction()
                // ingredientQuantity.innerText = `${quantityFraction}`
                const updatedQuantity = servingsSize/servingsSizeDefault*eval(ingredientQuantity.innerText);
                if (Number.isInteger(updatedQuantity)){
                    ingredientQuantity.innerText = `${updatedQuantity}`
                } else{
                    ingredientQuantity.innerText = `${updatedQuantity.toFixed(1)}`;
                }
            }
        }
    }
    
});


// below are for handling adding ingredients to shopping list.
const addAllToShoppingListForm = document.querySelector("#add-to-shoppinglist-form");
addAllToShoppingListForm.addEventListener('submit',evt => {
    evt.preventDefault();
    // check if user logged in or not. Need to be in the server side.
    const addAllToShoppingListBtn = addAllToShoppingListForm.querySelector(".add-ingredients-to-shoppinglist-btn")
    const recipeIDToServer ={recipeID: addAllToShoppingListBtn.dataset.recipeId};
    console.log(recipeIDToServer);
    fetch('/add-to-shoppinglist',{
        method: 'POST',
        body: JSON.stringify(recipeIDToServer),
        headers: {
            'Content-Type': 'application/json',
            },
    })
    .then(response => response.text())
    .then(serverData => {
        if (serverData === "added_shopping_recipe_entry"){
            addAllToShoppingListBtn.value = "Added All Ingredients to Shopping List";

        }
    });
    // catch errors when server is down for example. 
    // recipe is deleted by user A while user b is trying to save the recipe.

});