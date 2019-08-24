import requests
from bs4 import BeautifulSoup
from csv import writer
from robobrowser import RoboBrowser
import time

# webpageResponse = requests.get('https://vumc.app.box.com/file/488726765019')

browser = RoboBrowser()
browser.open('https://sd.app.vumc.org/sd-discover/')
time.sleep(5)
# browser.open("https://starbrite.app.vumc.org/auth/?req_url=https%3A%2F%2Fstarbrite.app.vumc.org%2F")
# form = browser.get_form()
# form = browser.find('form')
# form['username'] = 'hatchjb2'
# form['password'] = 'vumcID$$'
# browser.submit_form(form)

body = browser.find('body')
output = browser.find(id='sddiscover-1207851718')
nextDiv = output.find(class_="v-app-loading")
# children = nextDiv.c
# newForm = browser.get_form()
# newForm['vunetid'] = 'hatchjb2'
# newForm['password'] = 'vumcID$$'
# browser.submit_form(newForm)

# output = browser.find('a', string='Synthetic Derivative (SD)')

# browser.open("https://starbrite.app.vumc.org/vdr/sdpage.html")


# soup = BeautifulSoup(webpageResponse.text, 'html.parser')

# workouts = soup.find_all('button')

# for child in output.children:
#   print(child)

print(body)

