import requests

#download the HTML document
#with an HTTP GET request
response = requests.get("https://bettereducation.com.au/Results/vce.aspx")

#print the HTML code
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_ = 'table table-striped table-bordered table-hover')
school_list = []
show_list = []

for school_data in table.find_all('tbody'):
    rows = school_data.find_all('tr')
    
print("Rank\t\t","School Name\t\t", "Percentile\t\t", "Median\t\t", "Location\t\t")   

for row in rows:
    rank = row.find_all('td')[1].text.replace("\n", "").replace("\r","")
    rank = rank.split(',')
    school_list.append(rank)
    
    school = row.find_all('td')[2].text.replace("\n", "").replace("\r","")
    school = school.split(',')[0]
    school_list.append(school)
   
        
    scores = row.find_all('td')[3].text.replace("\n", "").replace("\r","")
    scores = scores.strip()
    school_list.append(scores)
    
    median = row.find_all('td')[4].text.replace("\n", "").replace("\r","")
    school_list.append(median)
    
    locality = row.find_all('td')[6].text.replace("\n", "").replace("\r","")
    school_list.append(locality)
    
    show_list = school_list.copy()
    school_list.clear()
    print(show_list)
    
 
