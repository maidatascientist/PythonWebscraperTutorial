# PythonWebscraperTutorial
Webscraping tutorial with Python

I am following the Python Webscraping tutorial at https://www.dataquest.io/blog/web-scraping-tutorial-python/

This tutorial uses Beautifulsoup to collect weather forecast data from the National Weather Services Site and then analyzes it using Pandas.

For this tutorial I used Visual Studio Code with Jupyter Notebook.

The first part of the tutorial is an introduction into HTML tags.

Tag Positions:
  1. child - tag inside another tag
  2. parent - tag that another tag is inside of
  3. sibling - tag nested inside parent of another tag
  
Common HTML Tags:
  1. a - link
  2. p - paragraph
  3. div - indicates a division or area of the page
  4. b - bolds text
  5. i - italicizes text
  6. table - creates table
  7. form - creates input form
  
Class and ID - gives HTML elements names which makes them easier to interact with.
  1. An element can have multiple classes and a class can be shared between elements
  2. An element can only have one id and an id can only be used once on a page.
  3. Classes and Id's are optional
  
Requests Library
  1. download simple website using requests.get method.
  
  
Parsing a page with BeautifulSoup


Finding all instances of a tag at once


Searching for tags by class and id


Using CSS Selectors


Downloading Weather Data


Exploring page structure with Chrome DevTools


Extracting Information from the Page


Extracting all the Information from the Page


Combining Data into a Pandas Dataframe




