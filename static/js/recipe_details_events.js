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


// below are example code

const btns = document.querySelectorAll('.save-remove-btn')

for (const btn of btns) {

    btn.addEventListener('click',evt =>{
    // console.log(btn)
    const addRemoveToServer ={recipeId: btn.dataset.recipeId};
    // console.log(dataToServer);

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
        const icon = btn.querySelector("i")
        if (serverData === "just_saved"){
            icon.classList.replace("bi-heart", "bi-heart-fill")
        }else if (serverData === "removed_from_saved"){
            icon.classList.replace("bi-heart-fill", "bi-heart")
        }
    });
    // catch errors when server is down for example. 
    // recipe is deleted by user A while user b is trying to save the recipe.

    });

}