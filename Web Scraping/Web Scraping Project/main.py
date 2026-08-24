from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.goodfirms.co/companies/web-development-agency")

soup = BeautifulSoup(html_text.text, 'lxml')
jobs = soup.find_all('li', class_ = 'firm-wrapper')

for job in jobs:
    company_name= job.find('h3', class_ = 'firm-name')
    if company_name:
        print(f"Company Name = {company_name.text}")
    else:
        print("Company Name = None")
        
    company_location = job.find('div', class_ ='firm-location custom_tooltip')
    if company_location:
        print(f"Company Location = {company_location.text}")
    else:
        print("Company Location = None")
        
    company_description = job.find('p', class_ = 'firm-short-description')
    if company_description:
       print(f"Company Description = {company_description.text}")
    else:
        print("Company Description = None")
    
    company_website = job.find('a', class_ = 'visit-website web-url list-blue-link js-no-modal-overlay')    
    if company_website:
        print(f"Company Website = {company_website['href']}")
    else:
        print("Company Website = None")
    print("\n")