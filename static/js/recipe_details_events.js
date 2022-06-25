'use strict';

document.querySelector("#servings-size-form").addEventListener('submit',evt => {
    evt.preventDefault();
    const servingsSize = document.querySelector("#servings-size-adjust").value;
    const servingsSizeDefault = document.querySelector("#servings-size-adjust").defaultValue;
    if (servingsSize !== servingsSizeDefault){
        allIngredientCheckboxes = document.querySelector(".form-check-input")
        for ( const ingredientCheckbox of allIngredientCheckboxes){
            
        }
    }
    
});