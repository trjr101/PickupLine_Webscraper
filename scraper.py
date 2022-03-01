#Web Scraping Script
#Author: Mihir Jetly

#Import our packages
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl
import pandas as pd


#Now, set the URL to scrape, and open it
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://bestlifeonline.com/pick-up-lines/"
req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
page = urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(page, "html.parser")

#We want to extract the elements we require from the page
OL_List = soup.find_all("ol")

lis = [li for ol in OL_List for li in ol.findAll('li')]

#Process it to get just the text out of our elements
for i in range(len(lis)):
    lis[i] = lis[i].get_text()

#Now we want to convert our list to a pandas dataframe to print to a csv file
df = pd.DataFrame(lis)
df.to_csv('pickup_lines.csv', index=False, header=False)
