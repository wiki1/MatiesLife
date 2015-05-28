OK - its been a while, but the search function now works - here is a basic rundown:
=============================================================================================
>> go to the localhost/wikiApp/search page
>> enter a term or sentence for which to search( I should point out, that on this version, there is so far only one dummy article - called first article(its title))
>> Click the search button - one of two things will happen:
								- the first article list item will appear, if you included the words first or 									article within your search phrase
								- there will be no list items, since your search did not include those 									keywords, or the exact title of the article


additional notes:
================================================================================================
- In order to make this work, i had to modify some files:
								-views.py
								-urls.py

- I had to create a couple of templates located within the wikiapp/templates directory:

												-search.html
												-searc_results.html

I had no additional changes to the origional project - please let me know what you guys think, and if there are any issues.


Thanx
Hendrik
																			



