# Welcome to BeefinApp
BeefinApp is a fitness website designed to give trainees easy to use personalized workout templates to keep track of progress and BEEF UP!

## How to start?
1. download all content and use main.py to run the website on local host
2. Sign up to creat your username and password
3. You can use the homepage to add notes and reminders
4. To start a program and add data, go to Strength Program in the navigation bar and choose a week, day, and exercise to get a form of sets. the inputs you type in and submit will redirect you to a table with the database of the inputs you have submited over time. 

## Code Explained:
This is a flask website with html templates and a bit of java script.

- auth.py stores all the routes for the login and sign up pages
- views.py stores the routes for the home and program pages.
- models.py create the database classes [users, notes and workout data], all saved according to user. 
- each route is rendered with html file in the folder templates. 


