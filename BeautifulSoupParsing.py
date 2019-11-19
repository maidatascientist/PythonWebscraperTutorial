# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\\..\AppData\Local\Temp'))
	print(os.getcwd())
except:
	pass

# %%
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page


# %%
page.status_code


# %%
page.content


# %%
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


# %%
print(soup.prettify())


# %%
list(soup.children)


# %%
[type(item) for item in list(soup.children)]


# %%
html = list(soup.children)[2]


# %%
list(html.children)


# %%
body = list(html.children)[3]


# %%
list(body.children)


# %%
p = list(body.children)[1]


# %%
p.get_text()


# %%
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p')


# %%
soup.find_all('p')[0].get_text()


# %%
soup.find('p')


# %%


