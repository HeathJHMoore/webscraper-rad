from selenium import webdriver
from bs4 import BeautifulSoup
import time
import data
import secret


# Open the browser to the SD page
chrome_path = r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get('https://sd.app.vumc.org/sd-discover/')
time.sleep(8)


# Login to account
vunetid = driver.find_element_by_xpath('//*[@id="gwt-uid-3"]')
password = driver.find_element_by_xpath('//*[@id="gwt-uid-5"]')
first_submit_button = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[5]/div')
# Keep username and pass in secret file on local machine for security purposes
vunetid.send_keys(secret.username)
password.send_keys(secret.password)
first_submit_button.click()
time.sleep(8)


# Choose Recurrence Database
# recentDataSets = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div')
# recentDataSets.click()
# recurrence = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td[1]')
# recurrence.click()
# time.sleep(5)
# reviewSetResults = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div')
# reviewSetResults.click()
# time.sleep(10)



# Filter Radiology Reports for Individual Patient
# openFiltersButton = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div[1]/div')
# openFiltersButton.click()
# time.sleep(5)
# openFilterDropdownButton = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div')
# openFilterDropdownButton.click()
# time.sleep(2)
# radiologyReportsOption = driver.find_element_by_xpath('//*[@id="VAADIN_COMBOBOX_OPTIONLIST"]/div/div[2]/table/tbody/tr[11]')
# radiologyReportsOption.click()
# time.sleep(2)
# applyFilter = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div')
# applyFilter.click()
# time.sleep(5)


# Get all radiology reports in a list
# radiologyHeaders = driver.find_elements_by_class_name('doc-content')
# print(radiologyHeaders)




# list that will hold list of patient surgery dates
# patientSurgeryDateArray = [
#   '03-28-2019',
#   '05-01-2019',
#   '02-23-2018'
# ]

# Build out patient objects with for loop
# patientObjectArray = []
# for i in range(3):
#   class patientInfo:
#     patientId = patientIdArray[i],
#     firstSurgeryDate = patientSurgeryDateArray[i]
#   patientObjectArray.append(patientInfo)

# for i in range(3):
#   print(patientObjectArray[i].patientId)

