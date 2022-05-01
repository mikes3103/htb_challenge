# htb_challenge
My approach to the hasToBe coding challenge :)


## CHALLENGE 1

Clone the repository into a folder

### MAIN-APP
Just run the application by navigating to the main folder and typing the 'flask run' command
(having python 3 installed is mandatory !!!)
Then open up your browser and type in 'localhost:5000' - there you can test the API '/route'

### TESTING
Simply run the command 'pytest test.py'


## CHALLENGE 2
Suggest improvements to the API design:

Since it is my first time working with Flask, there are for sure many possible improvements.
I broke it down to three main things and one thing regarding the UI.

- I am sure that there would be a better way to handle a missing component than the try/except block that I used.
Since a try/except tends to mute every error that occurs and therefore maybe also hides othere errors that can cause problems later on.

- I am also sure that there would be a better way to return the results. My "output()" method seems a bit too static

- There should definitely be another way of converting the datetime because there are sooo many different possible formats of a datetime.

Regarding the UI, I am not quite sure if every browser supports the input type 'type="datetime-local"'
