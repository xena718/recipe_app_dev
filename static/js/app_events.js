'use strict';

// ## the following chunk is to add and remove recipe to user's collection 
// by clicking heart and unheart button on the top right of recipe card##

// document.getElementsByClassName("save-remove-btn") also works
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

    });

}

// ## the following chunk is remove a recipe from user's collection at saved_recipe homepage. ##

const removeBtns = document.querySelectorAll(".remove-btn")
for (const removeBtn of removeBtns){
    removeBtn.addEventListener('click', evt =>{
    const removeToServer ={recipeId: removeBtn.dataset.recipeId};

    fetch('/remove',{
        method: 'POST',
        body: JSON.stringify(removeToServer),
        headers: {
            'Content-Type': 'application/json',
            },
    })
    // the following code needs update.
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

    });

}
