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


// below are for handling the form of adding ingredients to shopping list.
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
        }else if(serverData === "not_logged_in"){
            alert('please log in first to add ingredients to shopping list');

        }
    });
});

// below are for handling the button of adding ingredients to shopping list.
// below not working
// const addToShoppingListBtn = document.querySelector(".add-to-shoppinglist-btn");
// addToShoppingListBtn.addEventListener('click',evt => {
//     // check if user logged in or not. Need to be in the server side.
//     const recipeIdToServer ={recipeID: addToShoppingListBtn.dataset.recipeId};
//     // console.log(recipeIdToServer);
//     fetch('/add-to-shoppinglist',{
//         method: 'POST',
//         body: JSON.stringify(recipeIdToServer),
//         headers: {
//             'Content-Type': 'application/json',
//             },
//     })
//     .then(response => response.text())
//     .then(serverData => {
//         if (serverData === "added_shopping_recipe_entry"){
//             addToShoppingListBtn.querySelector("#add-to-shoppinglist-text").innerText = "Added All Ingredients to Shopping List";
//             addToShoppingListBtn.querySelector("i").classList.replace("bi bi-cart", "bi bi-cart-check")

//         }
//     });
// });