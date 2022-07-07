# YummyApp
YummyApp is a recipe management app that allows users to create recipes, search recipes, save recipes to personal collections, and generate a handy shopping list for selected recipes. 
I used to use gsheet for managing recipe collections. Not any more! I have enjoyed buidling and using the YummyApp along the way. Say goodbye to gsheet for recipe collections and Give my yummyapp a try! --I take feature request, build commonly requested features, and deploy them for  users!


## Table of Contents 📖
* [Tech Stack](#techstack)
* [Features](#features)
* [Set-Up](#setup)
* [Future Improvements](#futureimprovements)
* [Credits](#credits)
* [About Me](#aboutme)

## <a name="techstack"></a>Tech Stack :card_file_box:
* Backend: Python, Flask, SQL, PostgreSQL, SQLAlchemy
* Frontend UI Framework: HTML, Jinja2, CSS, Bootstrap 
* JS cornerstone: Javascript (AJAX method and JSON data format)
* Deploy: to be added ...
* Other: Beautiful Soup(used for data-scraping). See my [Giveme_Recipes](https://github.com/xena718/giveme_recipes) project for more information. 

## <a name="features"></a>Features :beers:
🎥 youtube link to be added... 


#### Homepage
* User can discover Featured recipes and most-saved recipes (by all users).
* Users can search recipes by any keyword (e.g. ingredient name, cuisine name, author name)
* Users can browse recipes by cuisine, by special diet, by course, and by ingredient name!
* Users can register or log-in for more features. 

### User Page
* A logged in user has their allergy profile pre-populated for them when they search for a product.
* If they are allergic to it, an offcanvas comes up showing the full list of ingredients and the offending ingredients.
![AllerApp User Page](/static/readmegifs/AllerAppUserPage.gif)

#### User Page - Safe & Unsafe Products
* Whenever a logged in user searches a product, it is immediately added to and displayed in the users safe and unsafe products list. This makes it easy for the user to see products they've already searched that they can or cant have.
![AllerApp Safe & Unsafe Products](/static/readmegifs/AllerAppSafeUnsafe.gif)

#### User Page - Favorited Products
* Clicking the "Add" button on any of the user's listed Safe Products will add the product to the user's favorite products list. 
* Hitting the Remove button on a product in the favorite list will remove it from the favorites list. 
![AllerApp Favorited Products](/static/readmegifs/AllerAppFavorited.gif)

## <a name="setup"></a>Set Up 🛠
To Be Added...

## <a name="futureimprovements"></a>Future Improvements :raised_hands:
* Remake this in React
* Add more options for ingredients to avoid
* Let the user manually input ingredients to avoid
* Set up a barcode scanner so that a user can quickly scan a product at a store to see if they can use it or not
* Passcode encryption for more security

## <a name="credits"></a>Credits :lollipop:
* All images and recipes in the demo are for demonstrative purposes only.
 * [NDTV Food](https://food.ndtv.com/)
 * [NYT Cooking](https://cooking.nytimes.com/)
 * [Allrecipes](https://www.allrecipes.com/)

## <a name="aboutme"></a>About Me :eyes: 
Hello! I'm Chengfeng, a software engineer and scientific researcher in Biotech. I created YummyApp in eight weeks(4-8 hrs per week) during my part-time full-stack engineer study at Hackbright. I'd love to connect with you on [Github](https://github.com/xena718?tab=repositories)!