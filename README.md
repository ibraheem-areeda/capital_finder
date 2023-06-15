# LAB - Class 16
## Project: capital-finder
### Author: Ibraheem Areeda


### Setup
- create .env environment 
- to install all requrments : `pip install -r requirements.txt`

**run the application**

by typing in the teminal `vercel dev` to start a local host 


**How to use this API** 


to use capital_finder API :
 1. get_citations_needed_count
 get_citations_needed_count(url), takes a URL as input and retrieves the webpage content using the requests library. It then uses the BeautifulSoup library to parse the HTML content of the webpage. The function searches for all occurrences of the text "citation needed" wrapped in a <span> tag and counts the number of such occurrences. Finally, it returns the count of citations needed.
 
 
 ex:     

 
input --> url = "https://en.wikipedia.org/wiki/Numerical_control"
 
 
output -> 2
 

 
 2. get_citations_needed_report
  get_citations_needed_report(url), performs a similar process as the first function. It retrieves the webpage content and parses it using BeautifulSoup. It searches for all occurrences of the text "citation needed" wrapped in a <span> tag. For each occurrence, it appends the parent elements' text (four levels up from the <span> tag) to a string. The function then returns the accumulated string, which represents a report of all the sections or sentences that require citations in the webpage. The report is formatted with line breaks between each section or sentence.
   
 
 ex:     

 
input --> url = "https://en.wikipedia.org/wiki/Numerical_control"
 
 
output -> "
The high backlash mechanism itself is not necessarily relied on to be repeatedly precise for the cutting process, but some other reference object or precision surface may be used to zero the mechanism, by tightly applying pressure against the reference and setting that as the zero references for all following CNC-encoded motions. This is similar to the manual machine tool method of clamping a micrometer onto a reference beam and adjusting the Vernier dial to zero using that object as the reference.[citation needed]

[Code Miscellaneous Functions (M-Code)][citation needed]. M-codes are miscellaneous machine commands that do not command axis motion. The format for an M-code is the letter M followed by two to three digits; for example:
"

  
### Tests
When it comes to running tests, it was a manual testing by trying various countries and capitals and check for the end result

 
 

