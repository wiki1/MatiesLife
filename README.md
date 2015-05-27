# MatiesLife
our project
_________________________________________________________________________________________________________
____________________________________________________________________________________________

Hie all

I added a new login function that handles login with the users models and also handles user sessions.
Given this knowledge, the app can now efficiently handle logouts as well.

In terms of the post article app, theres a couple of fixes that are still required.

How it's supposed to work
_______________________

>The postingArticle page loads showing a user some textboxes where they can enter data into the textbox fields.

>Once page is loaded, the method that loads the page (the 'preliminary' method) loads some placeholder article and 
content objects and places them into the text boxes via the postArticles.html code. The file can be found in the 
postingArticles/templates folder.

>The user presses the save/submit button and the section that consists of a heading and a paragraph should be printed
at the bottom of the page. The textboxes are then wiped off their data and new data is loaded into them.

>The captured data is sent to a addItems module in the views.py that writes the POSTED data to objects which are then 
saved to the database.

>As heading and paragraph sections are being generated at the bottom of the page, a button is also generated that
allows users to edit the specific section its aligned with.
___________________________________________________________________________________________________________________

The program seems to be crashing because some of the values cannot take multiple heading and paragraph objects and
the variables that have been saved as sections of an article are not appearing at the bottom of the web page as 
expected.

please help!!!
