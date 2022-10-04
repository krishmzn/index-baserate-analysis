from html.parser import HTMLParser
from platform import processor
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

month = []
base_rate = []

#getting the url
req = requests.get("https://www.nicasiabank.com/investor-relation/interest-base-rate").text

soup = BeautifulSoup(req, 'html.parser')

#month
mon = soup.select("tr > td:nth-of-type(1)")# first element of tr
for i in range(len(mon)):
  month.append(mon[i].text)

#base_rate
bsr = soup.select("tr > td:nth-of-type(2)")# second element
for i in range(len(bsr)):
  base_rate.append(bsr[i].text)
  
  
df = {'Date':month, 'Base Rate':bsr}
dataset = pd.DataFrame.from_dict(df, orient = 'index')
dataset = dataset.transpose()
print(dataset)

directory = os.path.dirname(os.path.realpath(__file__))
FILE_NAME = "scrapedfile.csv"
PATH_TO_CSV_FILE = os.path.join(directory, FILE_NAME)
dataset.to_csv(PATH_TO_CSV_FILE, index = False)