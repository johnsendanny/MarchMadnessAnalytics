import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re

years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']

kpinfo = {}
names = []
kpyear = []
seeds = []
adjemkp = []
adjokp = []
adjdkp = []
adjTkp = []
luckkp = []
adjemsoskp = []
adjososkp = []
adjdsoskp = []
adjemNCSOSkp = []
record_match1 = r'\d\d-\d'
record_match2 = r'\d-\d\d'
record_match3 = r'\d\d-\d\d'

for j in years:
    ans = requests.get(f'https://kenpom.com/index.php?y={j}')
    soup = BeautifulSoup(ans.content, 'html.parser')
    teams = soup.find_all('td', class_ = 'next_left')
    td = soup.find_all('td')
    lefts = soup.find_all('td', class_ = 'td-left')

    for x in teams:
        if x.text[-1] in ['0','1','2','3','4','5','6','7','8','9']:
            if x.text[len(x.text)-2:len(x.text)] in ['10','11','12','13','14','15','16']:
                names.append(x.text[0:len(x.text)-2].strip())
                seeds.append(x.text[len(x.text)-2:len(x.text)])
            else:
                names.append(x.text[0:len(x.text)-1].strip())
                seeds.append(x.text[-1])
        else:
            names.append(x.text.strip())
            seeds.append('17')
        kpyear.append(j)

    prev_match = False
    for x in td:
        if prev_match:
            adjemkp.append(x.text)
            prev_match = False
        if re.match(record_match1,x.text) or re.match(record_match2,x.text) or re.match(record_match3,x.text):
            prev_match = True
            pass

    count = 0
    for x in lefts:
        if count % 8 == 0:
            adjokp.append(x.text)
        elif count % 8 == 1:
            adjdkp.append(x.text)
        elif count % 8 == 2:
            adjTkp.append(x.text)
        elif count % 8 == 3:
            luckkp.append(x.text)
        elif count % 8 == 4:
            adjemsoskp.append(x.text)
        elif count % 8 == 5:
            adjososkp.append(x.text)
        elif count % 8 == 6:
            adjdsoskp.append(x.text)
        elif count % 8 == 7:
            adjemNCSOSkp.append(x.text)
        count += 1

kpinfo['Names'] = names
kpinfo['Year'] = kpyear
kpinfo['Seed'] = seeds
kpinfo['AdjEM-KP'] = adjemkp
kpinfo['AdjO-KP'] = adjokp
kpinfo['AdjD-KP'] = adjdkp
kpinfo['AdjT-KP'] = adjTkp
kpinfo['Luck-KP'] = luckkp
kpinfo['AdjEM-SOS-KP'] = adjemsoskp
kpinfo['AdjO-SOS-KP'] = adjososkp
kpinfo['AdjD-SOS-KP'] = adjdsoskp
kpinfo['AdjEM-NCSOS-KP'] = adjemNCSOSkp

kpdata = pd.DataFrame(kpinfo)
print(kpdata)