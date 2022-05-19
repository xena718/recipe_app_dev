'use strict';

document.querySelector('#add-to-saved-form').addEventListener('submit',evt =>{
    evt.preventDefault();
}

// document.querySelector('#add-to-saved-form').addEventListener('submit',evt =>{
//     evt.preventDefault();

//     const forminput = {
//         recipe_instance: document.querySelector('#add-to-saved-input')
//     };
    
//     fetch('/add-to-saved',{
//         method: 'POST',
//         body: JSON.stringify(forminput),
//         headers: {
//             'Content-Type': 'application/json',
//           },
//     })
//     .then(response => response.json())
//     .then(responseJSON => {
//         // I want  to change the submit button to a different color 
//     });

// });


