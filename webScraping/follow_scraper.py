from urllib.request import urlopen
from bs4 import BeautifulSoup

# re imports regular expression operations, and is used in compile below
import re

site_links = []


def internal_links(link_url):
    html = urlopen('https://treehouse-projects.github.io/horse-land/{}'
                   .format(link_url))
    soup = BeautifulSoup(html, 'html.parser')

    # re.compile compiles a reg.ex into a reg.ex object, which can be reused
    #   for multiple uses of the function defined.
    return soup.find('a', href=re.compile('(.html)$'))


if __name__ == '__main__':
    urls = internal_links('index.html')
    while len(urls) > 0:
        page = urls.attrs['href']
        if page not in site_links:
            site_links.append(page)

            print(page)
            print('\n============\n')
            urls = internal_links(page)

        else:
            break
