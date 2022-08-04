import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest



#coluns
job_title=[]
company_name=[]
location=[]
date_posted=[]
job_type=[]
career_level=[]
year_of_exper=[]
skills=[]

#request
result=requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
#content of the request
src=result.content

#parsing in lxml
soup=BeautifulSoup(src,"lxml")

#geting all job titles
job_titles=soup.find_all("h2",{"class":"css-m604qf"})
#geting all companies name
company_names=soup.find_all("a",{"class":"css-17s97q8"})
#locations
locations_names=soup.find_all("span",{"class":"css-5wys0k"})
#date of publishment
date=soup.find_all("div",{"class":"css-4c4ojb"})
#job type
jobtype=soup.find_all("span",{"class":"css-1ve4b75 eoyjyou0"})
level=soup.find_all("a",{"class":"css--o171kl" , "href":"/a/Experienced-Jobs-in-Egypt"})
exp_year=soup.find_all("span")
job_skills=soup.find_all("div",{"class":"css-y4udm8"})





#reading informations
for i in range (len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    location.append(locations_names[i].text)
    job_type.append(jobtype[i].text)
    #skills needed for a well known job
    for j in range (len(job_skills)):
        skills.append(job_skills[i].text)





#writting in a csv file
file_list = [job_title, company_name, location, job_type, skills]
exported = zip_longest(*file_list)
with open(r"C:\Users\hhss\Documents\JOBSTEXT.csv" , "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job_title", "company_name", "location", "job_type", "skills"])
    wr.writerows(exported)