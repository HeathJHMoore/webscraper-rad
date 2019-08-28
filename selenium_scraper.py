from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import data
import secret
import pandas

# newestDateformat = datetime.strptime('2001-01-24', '%Y-%m-%d')

patientIdArrayLength = 1
aggregatePatientInfo = {
  "patientId" : [],
  "patientFirstSurgeryDate" : [],
  "firstOperationHeader" : [],
  "firstOperationNotes" : [],
  "postOpRadReport1Notes" : [],
  "postOpRadReport2Notes" : [],
  "postOpRadReport3Notes" : [],
  "patientNextSurgeryDate" : [],
  "nextOperationHeader" : [],
  "nextOperationNotes" : [],
  "preOpRadReport1Notes" : [],
  "preOpRadReport2Notes" : [],
  "preOpRadReport3Notes" :[]
}

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

def firstfilterRadiologyReports():
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

def secondfilterRadiologyReports():
  # Filter Radiology Reports for Individual Patient
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

    # adding patientId to data
    aggregatePatientInfo["patientId"].append(data.patientIdArray[i])

    time.sleep(5)
    patientRow = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[3]/div[1]/table/tbody/tr')
    patientRow.click()
    # we may actually not want to filter for reports since we need to do everything relative to all entries
    # filterRadiologyReports()
    # the below variable is storing the date of the patient's first operation
    firstSurgeryDate = data.firstSurgeryDateArray[i]
    print(firstSurgeryDate)
    # the below adds the first surgery date to the aggregate patient dataframe
    aggregatePatientInfo["patientFirstSurgeryDate"].append(firstSurgeryDate)
    # the below variable will store the header text and the index position
    firstSurgeryHeader = ''
    firstSurgeryDivIndex = 0
     # Get the dates of all report sections so that you can compare them properly
    reportHeaders = driver.find_elements_by_class_name('doc-content')
    time.sleep(2)
    reportHeadersLength = len(reportHeaders)
    time.sleep(2)
    for firstReportHeaderIterator in range(reportHeadersLength):
      allText = reportHeaders[firstReportHeaderIterator].text
      date = allText[0:10]
      reportType = allText[-16:]
      dateFormat = time.strptime(date, '%Y-%m-%d')
      if dateFormat == time.strptime(firstSurgeryDate, '%m-%d-%y') and reportType == 'OPERATIVE REPORT':
        firstSurgeryHeader = reportHeaders[firstReportHeaderIterator].text
        firstSurgeryDivIndex = firstReportHeaderIterator
        break
    reportContent = driver.find_elements_by_class_name('doc-content-div')
    firstSurgeryNotes = reportContent[firstSurgeryDivIndex].text

    # adding first surgery header and notes to data
    aggregatePatientInfo["firstOperationHeader"].append(firstSurgeryHeader)
    aggregatePatientInfo["firstOperationNotes"].append(firstSurgeryNotes)

    # start filtering radiology reports
    if i == 0:
      firstfilterRadiologyReports()
    else:
      secondfilterRadiologyReports()

    radiologyReportHeaders = driver.find_elements_by_class_name('doc-content')
    radiologyReportNotes = driver.find_elements_by_class_name('doc-content-div')
    radiologyReportHeadersListLength = len(radiologyReportHeaders)
    time.sleep(3)
    firstThreeRadiologyReports = []

    # this for loop finds the notes for the three radiology report after the first surgery date
    for radiologyReportHeaderIterator in range(radiologyReportHeadersListLength):
      radiologyReportText = radiologyReportHeaders[radiologyReportHeaderIterator].text
      radiolgyReportDate = radiologyReportText[0:10]
      radiolgyReportDateFormat = time.strptime(radiolgyReportDate, '%Y-%m-%d')
      if radiolgyReportDateFormat >= time.strptime(firstSurgeryDate, '%m-%d-%y'):
        if len(firstThreeRadiologyReports) < 3:
          class firstRadiologyReportInfo:
            reportHeader = radiologyReportText
            reportIndex = radiologyReportHeaderIterator
            reportNotes = radiologyReportNotes[radiologyReportHeaderIterator].text
          firstThreeRadiologyReports.append(firstRadiologyReportInfo)
        else:
          break
    
    for yo in firstThreeRadiologyReports:
      print(yo.reportNotes)

    # this code accounts for a patient having less than 3 radiology reports
    # it goes in and adds blank report to get a patients total up to 3 if need be
    firstRadReportsLength = len(firstThreeRadiologyReports)
    if (firstRadReportsLength < 3):
      numberToAdd = 3 - firstRadReportsLength
      for adds in range(numberToAdd):
        class blankRadiologyReportInfo:
           reportHeader = ''
           reportIndex = ''
           reportNotes = ''
        firstThreeRadiologyReports.append(blankRadiologyReportInfo)
    

    aggregatePatientInfo["postOpRadReport1Notes"].append(firstThreeRadiologyReports[0].reportNotes)
    aggregatePatientInfo["postOpRadReport2Notes"].append(firstThreeRadiologyReports[1].reportNotes)
    aggregatePatientInfo["postOpRadReport3Notes"].append(firstThreeRadiologyReports[2].reportNotes)
    

    
    # This begins the fining of the second surgery notes
    nextSurgeryDate = data.nextSurgeryDateArray[i]
    aggregatePatientInfo["patientNextSurgeryDate"].append(nextSurgeryDate)
    nextSurgeryDivIndex = 0
    nextSurgeryHeader = ''
    clearFilterButton = driver.find_element_by_xpath('//*[@id="sddiscover-1207851718"]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div')
    clearFilterButton.click()
    time.sleep(5)
    reportHeaders = driver.find_elements_by_class_name('doc-content')
    reportHeadersLength = len(reportHeaders)
    for secondReportHeaderIterator in range(reportHeadersLength):
      allText = reportHeaders[secondReportHeaderIterator].text
      date = allText[0:10]
      reportType = allText[-16:]
      dateFormat = time.strptime(date, '%Y-%m-%d')
      if dateFormat == time.strptime(nextSurgeryDate, '%m-%d-%y') and reportType == 'OPERATIVE REPORT':
        nextSurgeryHeader = reportHeaders[secondReportHeaderIterator].text
        nextSurgeryDivIndex = secondReportHeaderIterator
        break
    reportContent = driver.find_elements_by_class_name('doc-content-div')    
    nextSurgeryNotes = reportContent[nextSurgeryDivIndex].text


    aggregatePatientInfo["nextOperationHeader"].append(nextSurgeryHeader)
    aggregatePatientInfo["nextOperationNotes"].append(nextSurgeryNotes)



    secondfilterRadiologyReports()
    reversedRadiologyReportHeaders = driver.find_elements_by_class_name('doc-content')
    reversedRadiologyReportHeaders.reverse()
    reversedRadiologyReportNotes = driver.find_elements_by_class_name('doc-content-div')
    reversedRadiologyReportNotes.reverse()
    reversedRadiologyReportHeadersLength = len(reversedRadiologyReportHeaders)
    time.sleep(3)
    LastThreeRadiologyReports = []

    # this for loop finds the notes for the three radiology report after the first surgery date
    for reversedRadiologyReportHeaderIterator in range(reversedRadiologyReportHeadersLength):
      reveresdRadiologyReportText = reversedRadiologyReportHeaders[reversedRadiologyReportHeaderIterator].text
      reversedRadiolgyReportDate = reveresdRadiologyReportText[0:10]
      reversedRadiolgyReportDateFormat = time.strptime(reversedRadiolgyReportDate, '%Y-%m-%d')
      if reversedRadiolgyReportDateFormat <= time.strptime(nextSurgeryDate, '%m-%d-%y'):
        if len(LastThreeRadiologyReports) < 3:
          class lastRadiologyReportInfo:
            reversedReportHeader = reveresdRadiologyReportText
            reversedReportIndex = reversedRadiologyReportHeaderIterator
            reversedReportNotes = reversedRadiologyReportNotes[reversedRadiologyReportHeaderIterator].text
          LastThreeRadiologyReports.append(lastRadiologyReportInfo)
        else:
          break
  

    # this code accounts for a patient having less than 3 radiology reports
    # it goes in and adds blank report to get a patients total up to 3 if need be
    LastRadReportsLength = len(LastThreeRadiologyReports)
    if (LastRadReportsLength < 3):
      numberToAdd = 3 - LastRadReportsLength
      for adds in range(numberToAdd):
        class blankRadiologyReportInfo:
           reversedReportHeader = ''
           reversedReportIndex = ''
           reversedReportNotes = ''
        LastThreeRadiologyReports.append(blankRadiologyReportInfo)

    
    aggregatePatientInfo["preOpRadReport1Notes"].append(LastThreeRadiologyReports[0].reversedReportNotes)
    aggregatePatientInfo["preOpRadReport2Notes"].append(LastThreeRadiologyReports[1].reversedReportNotes)
    aggregatePatientInfo["preOpRadReport3Notes"].append(LastThreeRadiologyReports[2].reversedReportNotes)



iterativePatientResults()

df = pandas.DataFrame(aggregatePatientInfo)

df.to_excel("output3.xlsx")





 
