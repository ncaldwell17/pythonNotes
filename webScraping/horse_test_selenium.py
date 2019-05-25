from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get('https://treehouse-projects.github.io/horse-land/index.html')

time.sleep(5)

page_html = driver.page_source

soup = BeautifulSoup(page_html, 'html.parser')

print(soup.prettify())

driver.close()