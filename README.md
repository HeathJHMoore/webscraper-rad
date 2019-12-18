# webscraper-rad

## About This Project
This python project was my first attempt at building a Selenium web scraper. A team of radiology researchers at Vanderbilt University asked me to build this webscraper to automate data aggregation that was being done manually through a web based database. The webscraper works by logging into the web based database and programmatically searching through a list of patients to capture clinical information from their charts and medical records. I stored this aggregated clinical information  in a Pandas dataframe and exported the information into Excel for easy distrubution to the researchers.

## Future Improvements
Given that this was my first python project, I made some decisions that, in hindsight, I would now avoid. 

Firstly, I relied heavily on the time.sleep() function to handle asynchronous problems in my program. As a more experienced python programmer now, I would instead use "try except" blocks for this problem. 
