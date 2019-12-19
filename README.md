# webscraper-rad

## About This Project
This python project was my first attempt at building a Selenium web scraper. A team of radiology researchers at Vanderbilt University asked me to build this webscraper to automate data aggregation that was being done manually through a web based database. The webscraper works by logging into the web based database and programmatically searching through a list of patients to capture clinical information from their charts and medical records. I stored this aggregated clinical information  in a Pandas dataframe and exported the information into Excel for easy distrubution to the researchers.

### Technologies Used
* Python

## Future Improvements
Given that this was my first python project, I made some decisions that, in hindsight, I would now avoid. 

Firstly, I relied heavily on the time.sleep() function to handle asynchronous requests in my program. As a more experienced python programmer, I would now use "try except" blocks for asynchronous processes since "try except" blocks allow for more sophisticaed error handling. Without this error/exception handling in my code, my program will sometimes crash if an asynchronous process does not complete in the time alloted in the time.sleep() function following it. 

Secondly, I would make more efforts to break my code into smaller functions, each with a single purpose (The S in the SOLID Principle). Currently, my code is only divided into a few, very heavy functions. In a code refactor, I would certainly break up these large functions into several smaller functions.
