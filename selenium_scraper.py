from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import data
import secret

# newestDateformat = datetime.strptime('2001-01-24', '%Y-%m-%d')

patientIdArrayLength = 1

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
recentDataSets = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div')
recentDataSets.click()
time.sleep(3)
recurrence = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td[1]')
recurrence.click()
time.sleep(5)
reviewSetResults = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/div')
reviewSetResults.click()
time.sleep(10)

def filterRadiologyReports():
  # Filter Radiology Reports for Individual Patient
  openFiltersButton = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div[1]/div')
  openFiltersButton.click()
  time.sleep(5)
  openFilterDropdownButton = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div')
  openFilterDropdownButton.click()
  time.sleep(2)
  radiologyReportsOption = driver.find_element_by_xpath('//*[@id="VAADIN_COMBOBOX_OPTIONLIST"]/div/div[2]/table/tbody/tr[11]')
  radiologyReportsOption.click()
  time.sleep(2)
  applyFilter = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div')
  applyFilter.click()
  time.sleep(5)

def iterativePatientResults():
  #Filter by PatientId
  for i in range(patientIdArrayLength): 
    searchPatient = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/input')
    searchPatient.send_keys(data.patientIdArray[i])
    time.sleep(5)
    patientRow = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[3]/div[1]/table/tbody/tr')
    patientRow.click()
    # we may actually not want to filter for reports since we need to do everything relative to all entries
    # filterRadiologyReports()
    # Get the dates of all report sections so that you can compare them properly
    reportHeaders = driver.find_elements_by_class_name('doc-content')
    reportHeadersLength = len(reportHeaders)
    # the below variable is storing the date of the patient's first operation
    firstSurgeryDate = data.firstSurgeryDateArray[i]
    # the below variable will store the header text and the index position
    # firstSurgeryDivSection = ''
    firstSurgeryDivIndex = 0
    for i in range(reportHeadersLength):
      allText = reportHeaders[i].text
      date = allText[0:10]
      reportType = allText[-16:]
      print(reportType)
      dateFormat = time.strptime(date, '%Y-%m-%d')
      if dateFormat == time.strptime(firstSurgeryDate, '%m-%d-%y') and reportType == 'OPERATIVE REPORT':
        firstSurgeryDivSection = reportHeaders[i]
        firstSurgeryDivIndex = i
        break
    reportContent = driver.find_elements_by_class_name('doc-content-div')
    firstSurgeryNotes = reportContent[firstSurgeryDivIndex]
    print(firstSurgeryNotes.text)


iterativePatientResults()





 
