# LAB - Class 16
## Project: capital-finder
### Author: Ibraheem Areeda


### Setup
- create .env environment 
- to install all requrments : `pip install -r requirements.txt`

**run the application**

by typing in the teminal `vercel dev` to start a local host 


**How to use this API** 

the url --> https://capital-finder-ibraheem-areeda.vercel.app/api/capital_finder?**query_as_country_or_capital**


The serverless function handles GET requests for capital and country information. If a country name is provided as a query parameter, the function responds with "The capital of X is Y", where X is the country name and Y is its capital. If a capital is provided, the response is "X is the capital of Y", where X is the capital name and Y is the corresponding country.

### examples

country --> https://capital-finder-ibraheem-areeda.vercel.app/api/capital_finder?country=cuba


capital --> https://capital-finder-ibraheem-areeda.vercel.app/api/capital_finder?capital=mosco

  
### Tests
When it comes to running tests, it was a manual testing by trying various countries and capitals and check for the end result

 
 

