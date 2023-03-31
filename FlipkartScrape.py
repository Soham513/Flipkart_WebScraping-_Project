import pandas as pd
import requests 
from bs4 import BeautifulSoup
#creating list to scrap 
Product_name= []
Prices = []
Description = []
Reviews = []





 #run through all 10 pager 
    #starting frm 2 coz we already have data of 1
url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"+str(1)
r = requests.get(url) #get us used to know the status code
    #print(r) #if response is 200 i.e we can get the html to scrap the data

        #pip install lxml
soup = BeautifulSoup(r.text,"lxml") # r.text -- gives text of the url  "lxml" -- is the file format
        #print(soup)
        #np will give the link of page 2 but when we click it will display the host page 
box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")#only particular section of the page


names = box.findAll("div",class_="_4rR01T") #findAll ("what to find","class")
for i in names:#will only print the names of phone
     name = i.text
     Product_name.append(name)
    #print(Product_name)
        
    #print(len(Product_name))#how many product

prices = box.findAll("div",class_="_30jeq3 _1_WHN1")
for i in prices:
        name = i.text
        Prices.append(name)
    #print(Prices)

desc = box.findAll( "ul",class_ = "_1xgFaf" )
for i in desc:
        name = i.text
        Description.append(name)
    #print(len(Description))
    #print(Description)
reviews =box.findAll("div",class_ = "_3LWZlK")
for i in reviews:
        name = i.text
        Reviews.append(name)
    #print(Reviews)
    
    #print(len(Reviews))
#Now creating a data frame to convert in a csv file
df = pd.DataFrame({'Product_name':Product_name,'Prices':Prices,'Description':Description,'Reviews':Reviews})#a dict is created
print(df)
df.to_csv("Flipkart_mobiles_under_50000.csv") #converted to csv file("location")






#while True: 
   # np = soup.find("a",class_ = "_1LKTO3").get("href") #.get -- get the link of this page
#print(np)
   # cnp = "https://www.flipkart.com"+np #will display from page 2
   # print(cnp)
   

