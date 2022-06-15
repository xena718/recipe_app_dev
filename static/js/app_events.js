'use strict';
// document.getElementsByClassName("save-remove-btn") also works
const btns = document.querySelectorAll('.save-remove-btn')

for (const btn of btns) {

    btn.addEventListener('click',evt =>{
    console.log(btn)
    const dataToServer ={recipeId: btn.dataset.recipeId};
    console.log(dataToServer);

    fetch('/save-remove',{
        method: 'POST',
        body: JSON.stringify(dataToServer),
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


