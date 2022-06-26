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
document.querySelector(".add-ingredients-to-shoppinglist-btn").addEventListener('submit',evt => {
    evt.preventDefault();
})