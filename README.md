# YummyApp
YummyApp is a recipe management app that allows users to create recipes, search recipes, save recipes to personal collections, and generate a handy shopping list for selected recipes. 
I used to use gsheet for managing recipe collections. Not any more! I have enjoyed building and using the YummyApp along the way. Say goodbye to gsheet for recipe collections and Give my yummyapp a try! --I take feature request, build commonly requested features, and deploy them for  users!


## Table of Contents 📖
* [Tech Stack](#techstack)
* [Features](#features)
* [Set-Up](#setup)
* [Future Improvements](#futureimprovements)
* [Credits](#credits)
* [About Me](#aboutme)

## <a name="techstack"></a>Tech Stack :card_file_box:
* Languages: Python, Javascript(AJAX, JSON), HTML, CSS, SQL
* Frameworks/Libraries: Flask, Bootstrap, Jinja, BeautifulSoup
* Database & Industry Tools: PostgreSQL, Git, Github, Command Line
* Tools/Software: Docker, Visual Studio Code, Microsoft Office

## <a name="features"></a>Features :beers:
🎥 [Yummy APP Demo Youtube Link](https://www.youtube.com/watch?v=hWVR_YX7PN8)


#### Homepage
* User can discover Featured recipes and most-saved recipes (by all users).
* Users can search recipes by any keyword (e.g. ingredient name, cuisine name, author name)
* Users can browse recipes by cuisine, by special diet, by course, and by ingredient name!
* Users can register and log-in for more features below (save a recipe, add a recipe, generate shopping list for recipes added to shopping cart). 
* Carousel card slides were implemented for convenient browsing. 

#### Save and Unsave Recipes 
* On top right corner of each recipe card, there is a heart-shaped save/remove button. After user logs in, all recipe cards in homepage or search returned page or browse-by returned page will have a filled heart button (already saved by user) or unfilled heart button (not saved by user yet) on top right of recipe card. Click the save/remove button (toggle between two save/remove) to save a recipe to users' recipe collection or remove it from users' recipe collection.
* At Saved page, it displays # of recipes a logged in user have saved and all saved-recipe cards with a remove button on the top right of each recipe card. 

#### Recipe Detail Page
* Users can adjust serving size. Quantity of each ingredient on page will be adjusted to the updated serving size. 
* logged in user can add all ingredients to shopping list. 

#### Shopping List Page
* logged-in users can see recipes that they have added to shopping cart. Each recipe card displays the shopping servings of the recipe. 
* A shopping list is generated for all recipes in cart. Shopping serving size of each recipe is used to generate shopping list. The quantity of the same ingredient from all recipes in card will be summed together if same unit is used or bundled together to the same line in shoppling list. 
* Users can click the ingredient to show/hide its associated recipes! 
* Users can text shopping list to cell phone!

#### Add a Recipe and User Profile
* Logged in users can add recipes by navigating to Add Recipe page.
* User profile page display logged in user's saved recipes and added/created recipes.


## <a name="setup"></a>Set Up 🛠
* This is a placeholder for setup of deployed app. ##to updated##.

## <a name="futureimprovements"></a>Future Improvements :raised_hands:
* Implement natural language processing (NLP) to categorize ingredients in shopping list.
* Use nutrition API to calculate and show nutrition information for each recipe. 
* Add more advanced searching algorithm and add more searching options.
* Based on users’ search history, suggest recipes that users may like.
* Allow users to add or remove ingredients in shopping list.
* Add unit conversion for ingredients in recipe detail page and shopping list page.
* Passcode encryption for more security.
* Remake this in React!



## <a name="credits"></a>Credits :lollipop:
* All images and recipes in the demo were scraped from the following sources for demonstrative purposes only. 
 * [NDTV Food](https://food.ndtv.com/)
 * [NYT Cooking](https://cooking.nytimes.com/)
* Thanks to HackBright Academy, instructors, TAs, alumni, outcomes team, and mentor for their support!

## <a name="aboutme"></a>About Me :eyes: 
Hello! I'm Chengfeng, a software engineer and scientific researcher in Biotech. I created YummyApp in eight weeks(4-8 hrs per week) during my part-time software engineering study (focused on full-stack web development) at Hackbright Academy. Check out my other projects on my [Github](https://github.com/xena718?tab=repositories)! I'd love to connect with you on [Linkedin](https://www.linkedin.com/in/chengfengren/)!