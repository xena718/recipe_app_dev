// below chunk for handling add ingredient
const addIngredientBtn = document.querySelector("#add-ingredient-button");
addIngredientBtn.addEventListener("click",evt =>{
    const ingredientDivs = document.querySelectorAll(".ingredient-quantity-unit-name-category-div");
    const lastIngredientDiv = ingredientDivs[ingredientDivs.length-1];
    const duplicate = lastIngredientDiv.cloneNode(true);
    duplicate.querySelector('input[name="ingredient-quantity"]').value ="";
    // console.log(duplicate.querySelector('input[name="ingredient-quantity"]').value);
    lastIngredientDiv.insertAdjacentElement('afterend', duplicate);

})

// below chunk for handling add cooking direciton
const addDirectionBtn = document.querySelector("#add-cooking-step-button");
addDirectionBtn.addEventListener("click",evt =>{
    let directionDivs = document.querySelectorAll('.step-number-direction-div');
    let lastDirectionDiv = directionDivs[directionDivs.length-1];
    let stepNumberOfLastDirectionDiv = Number(lastDirectionDiv.querySelector(".step-number").innerText);
    const duplicateDiv = lastDirectionDiv.cloneNode(true);
    duplicateDiv.querySelector(".step-number").innerText = stepNumberOfLastDirectionDiv+1;
    duplicateDiv.querySelector('textarea[name="step-guidance"]').value ="";
    duplicateDiv.querySelector('textarea[name="step-guidance"]').placeholder ="Add another step";

    lastDirectionDiv.insertAdjacentElement('afterend', duplicateDiv);
})

// below chunk for removing ingredient
const ingredientsDiv = document.querySelector(".ingredients-div");
ingredientsDiv.addEventListener("click", event=>{
    // console.log(event.currentTarget);
    const removeBtns = event.currentTarget.querySelectorAll(".ingredient-remove-btn");
    for (const removeBtn of removeBtns){
        // console.log(removeBtn);
        removeBtn.addEventListener("click", evt=>{
        const allRemoveBtns =document.querySelectorAll(".ingredient-remove-btn");
        if (allRemoveBtns.length>1){
            removeBtn.closest(".ingredient-quantity-unit-name-category-div").remove();
        }

        })
    }

});



// below chunk for handling removing cooking direction

const directionsDiv = document.querySelector(".directions-div");
directionsDiv.addEventListener("click", event=>{
    console.log("first");
    // console.log(event.currentTarget);
    // const removeDirectionBtns = event.currentTarget.querySelectorAll(".direction-remove-btn");
    const removeDirectionBtns = event.currentTarget.querySelectorAll(".direction-remove-btn");
    for (const removeDirectionBtn of removeDirectionBtns){
        console.log("second");

        removeDirectionBtn.addEventListener("click", evt=>{
        console.log("third");

        const allRemoveDirectionBtns = document.querySelectorAll(".direction-remove-btn");
        if(allRemoveDirectionBtns.length>1){
            console.log(removeDirectionBtn.closest(".step-number-direction-div"));
            removeDirectionBtn.closest(".step-number-direction-div").remove();
            const stepSpans = document.querySelectorAll(".step-number");  
            let j=1;
            for (const stepSpan of stepSpans) {
                if (j<=stepSpans.length){
                    stepSpan.innerText=j;
                    j=j+1;
                }
            }
        }

        })
    }
});