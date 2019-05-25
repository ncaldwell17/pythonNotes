from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')
# un-comment any of the functions below to see what they do

# Get all the hyperlinks on a page:
for link in soup.find_all('a'):
    print(link.get('href'))

# New Commands:
# * name = looks for tags with certain names, like title or <div>
# * attrs = allows for the searching of a specific css class
# * recursive = if set to false, it will only look at the direct children of the tag
# * string = allows for the searching of strings instead of tags
# * **kwargs = allows for searching of other items, like a CSS ID
# * limit = limits the search to a specified parameter

"""
for button in soup.find(attrs={'class': 'button button--primary'}):
    print(button)
"""
# vs.
"""
for button in soup.find(class_='button button--primary'):
    print(button)
"""

# find allows you to find the first instance of a web element
# the find syntax is soup.find('element_name', {'subset_type':'name'})
"""
div = soup.find('div', {'class': 'featured'})
print(div)
"""

# chaining child elements of elements - just add the name as a point at the end
"""
featured_header = soup.find('div', {'class', 'featured'}).h2
print(featured_header.get_text())
"""
# .get_text on the end of a variable gets rid of the tags (e.g. <h1>, <class>)
# MAKE SURE that you only use .get_text() at the end of a program, otherwise
#   it'll mess things up because it strips the tags, preventing the scraper
#   from reading the information going forward.

# find_all just returns every div that meets the categories I defined
"""
divs = soup.find_all('div', {'class': 'featured'})
for div in divs:
    print(div)
"""
