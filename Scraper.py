import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re

# Setting up variables to use
years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
#Torvik Info Instantiation
info = {}
teams =[]
seeds = []
results = []
year = []
adjoef = []
adjdef = []
barthagf = []
efgf = []
efgdf = []
torf = []
tordf = []
orbf = []
drbf = []
ftrf = []
ftrdf = []
twopf = []
twopdf = []
threepf = []
threepdf = []
adjtf = []
wabf = []
#kenpom info instantiation
kpinfo = {}
kpnames = []
kpyear = []
kpseeds = []
adjemkp = []
adjokp = []
adjdkp = []
adjTkp = []
luckkp = []
adjemsoskp = []
adjososkp = []
adjdsoskp = []
adjemNCSOSkp = []

# Regex matching expressions for kenpom record and torvik web gobbledegook
record_match1 = r'\d\d-\d'
record_match2 = r'\d-\d\d'
record_match3 = r'\d\d-\d\d'
namepattern = r'\w*\W*\w*\W*\w*\W*\xa0\xa0\xa0\w*'


for j in years:
    # making the request and getting the content to scrape our data from
    ans = requests.get(f'https://barttorvik.com/trank.php?year={j}&sort=&top=0&conlimit=All#')
    soup = BeautifulSoup(ans.content, 'html.parser')
    # Finding Team names and parsing them so we have names, seeds, tournament results
    names = soup.find_all(class_='teamname')
    
    adjoe = soup.find_all('td',class_='1')
    for y in adjoe:
        if y.text == 'AdjOE':
            pass
        else:
            sp = y.text.split('.')
            adjoef.append(sp[0]+'.'+sp[1][0])

    adjde = soup.find_all(class_='2')
    for y in adjde:
        if y.text =='AdjDE':
            pass
        else:
            sp = y.text.split('.')
            adjdef.append(sp[0]+'.'+sp[1][0])
    
    barthag = soup.find_all(class_='3')
    for y in barthag:
        if y.text in ['Barthag', 'Rk']:
            pass
        else:
            barthagf.append(y.text[0:5])
    efg = soup.find_all(class_='7 mobileout')
    for y in efg:
        if y.text in ['Efg%', 'EFG%']:
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                efgf.append(sp[0]+'.'+sp[1][0])
            else:
                efgf.append(y.text[0:2])
    efgd = soup.find_all(class_='8 mobileout')
    for y in efgd:
        if y.text in ['EfgD%', 'EFGD%']:
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                efgdf.append(sp[0]+'.'+sp[1][0])
            else:
                efgdf.append(y.text[0:2])
    tor = soup.find_all(class_='11 mobileout')
    for y in tor:
        if y.text == 'TOR':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                torf.append(sp[0]+'.'+sp[1][0])
            else:
                torf.append(y.text[0:2])
    
    tord = soup.find_all(class_='12 mobileout')
    for y in tord:
        if y.text == 'TORD':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                tordf.append(sp[0]+'.'+sp[1][0])
            else:
                tordf.append(y.text[0:2])
    orb = soup.find_all(class_='13 mobileout')
    for y in orb:
        if y.text == 'ORB':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                orbf.append(sp[0]+'.'+sp[1][0])
            else:
                orbf.append(y.text[0:2])

    drb = soup.find_all(class_='14 mobileout')
    for y in drb:
        if y.text == 'DRB':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                drbf.append(sp[0]+'.'+sp[1][0])
            else:
                drbf.append(y.text[0:2])

    ftr = soup.find_all(class_='9 mobileout')
    for y in ftr:
        if y.text == 'FTR':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                ftrf.append(sp[0]+'.'+sp[1][0])
            else:
                ftrf.append(y.text[0:2])
    ftrd = soup.find_all(class_='10 mobileout')
    for y in ftrd:
        if y.text == 'FTRD':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                ftrdf.append(sp[0]+'.'+sp[1][0])
            else:
                ftrdf.append(y.text[0:2])
    twop = soup.find_all(class_='16 mobileout')
    for y in twop:
        if y.text == '2P%':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                twopf.append(sp[0]+'.'+sp[1][0])
            else:
                twopf.append(y.text[0:2])
    twopd = soup.find_all(class_='17 mobileout')
    for y in twopd:
        if y.text == '2P%D':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                twopdf.append(sp[0]+'.'+sp[1][0])
            else:
                twopdf.append(y.text[0:2])
    threep = soup.find_all(class_='18 mobileout')
    for y in threep:
        if y.text == '3P%':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                threepf.append(sp[0]+'.'+sp[1][0])
            else:
                threepf.append(y.text[0:2])
    threepd = soup.find_all(class_='19 mobileout')
    for y in threepd:
        if y.text == '3P%D':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                threepdf.append(sp[0]+'.'+sp[1][0])
            else:
                threepdf.append(y.text[0:2])

    adjt = soup.find_all(class_='26 mobileout')
    for y in adjt:
        if y.text == 'Adj T.':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
                adjtf.append(sp[0]+'.'+sp[1][0])
            else:
                adjtf.append(y.text[0:2])
    wab = soup.find_all(class_='34 mobileout')
    for y in wab:
        if y.text == 'WAB':
            pass
        else:
            sp = y.text.split('.')
            if len(sp) > 1:
               wabf.append(sp[0]+'.'+sp[1][0])
            else: 
                if y.text[0] =='-':
                    if len(y.text) == 6:
                        wabf.append(y.text[0:3])
                    elif len(y.text) == 5:
                        wabf.append(y.text[0:2])
                    elif len(y.text) == 4:
                        wabf.append(y.text[0:2])
                else:
                    wabf.append(y.text[0])

    for x in names:
        # To check if a team is a tournament team or not
        if re.match(namepattern,x.text):
            teaminfo = x.text.split()
            # Below is dealing with teams that have multiple word names vs single names
            if len(teaminfo) >= 5:
                if len(teaminfo) >= 6:
                    if teaminfo[len(teaminfo)-1] in ['R64','R32','R68']:
                        teams.append(teaminfo[0] + ' ' + teaminfo[1]+ ' ' + teaminfo[2])
                        seeds.append(teaminfo[3])
                    elif len(teaminfo) == 7 and teaminfo[len(teaminfo)-1] in ['Eight','Sixteen','Four']:
                        teams.append(teaminfo[0] + ' ' + teaminfo[1]+ ' ' + teaminfo[2])
                        seeds.append(teaminfo[3])
                    else:
                        teams.append(teaminfo[0] + ' ' + teaminfo[1])
                        seeds.append(teaminfo[2])
                else:
                    if teaminfo[len(teaminfo)-1] in ['R64','R32','R68']:
                        teams.append(teaminfo[0] + ' ' + teaminfo[1])
                        seeds.append(teaminfo[2])
                    else:
                        if len(teaminfo[1]) >= 3:
                            teams.append(teaminfo[0] + ' ' + teaminfo[1])
                            seeds.append(teaminfo[2])
                        else:
                            teams.append(teaminfo[0])
                            seeds.append(teaminfo[1])
            else:
                teams.append(teaminfo[0])
                seeds.append(teaminfo[1])
            
            # dealing with multiple word results vs single word results
            if teaminfo[len(teaminfo)-1] in ['Four', 'Eight', 'Sixteen']:
                results.append(teaminfo[len(teaminfo)-2] + ' ' + teaminfo[len(teaminfo)-1])
            else:
                results.append(teaminfo[len(teaminfo)-1])
        # Non tournament teams are much easier to deal with lol
        else:
            teaminfo = x.text.split()
            if len(teaminfo) >= 4:
                teams.append(teaminfo[0] + ' ' + teaminfo[1]+ ' ' + teaminfo[2]+ ' ' + teaminfo[3])
                seeds.append('17')
            elif len(teaminfo) >= 3:
                teams.append(teaminfo[0] + ' ' + teaminfo[1]+ ' ' + teaminfo[2])
                seeds.append('17')
            elif len(teaminfo) >= 2:
                teams.append(teaminfo[0] + ' ' + teaminfo[1])
                seeds.append('17')
            else:
                teams.append(teaminfo[0])
                seeds.append('17')
            results.append('NoTourney')
        year.append(j)
    

for j in years:
    ans = requests.get(f'https://kenpom.com/index.php?y={j}')
    soup = BeautifulSoup(ans.content, 'html.parser')
    teamskp = soup.find_all('td', class_ = 'next_left')
    td = soup.find_all('td')
    lefts = soup.find_all('td', class_ = 'td-left')

    for x in teamskp:
        if x.text[-1] in ['0','1','2','3','4','5','6','7','8','9']:
            if x.text[len(x.text)-2:len(x.text)] in ['10','11','12','13','14','15','16']:
                kpnames.append(x.text[0:len(x.text)-2].strip())
                kpseeds.append(x.text[len(x.text)-2:len(x.text)])
            else:
                kpnames.append(x.text[0:len(x.text)-1].strip())
                kpseeds.append(x.text[-1])
        else:
            kpnames.append(x.text.strip())
            kpseeds.append('17')
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

#kenpom dictionary to make pandas dataframe
kpnames = ['North Carolina St.' if x == 'N.C. State' else x for x in kpnames]
kpnames = ['Utah Valley' if x == 'Utah Valley St.' else x for x in kpnames]

# Below is a check for names that are in one set of rankings but not the other
# for p in kpnames:
#     if p in teams:
#         pass
#     else:
#         print(p)

kpinfo['Names'] = kpnames
kpinfo['Year'] = kpyear
kpinfo['Seed'] = kpseeds
kpinfo['AdjEM-KP'] = adjemkp
kpinfo['AdjO-KP'] = adjokp
kpinfo['AdjD-KP'] = adjdkp
kpinfo['AdjT-KP'] = adjTkp
kpinfo['Luck-KP'] = luckkp
kpinfo['AdjEM-SOS-KP'] = adjemsoskp
kpinfo['AdjO-SOS-KP'] = adjososkp
kpinfo['AdjD-SOS-KP'] = adjdsoskp
kpinfo['AdjEM-NCSOS-KP'] = adjemNCSOSkp

# Torvik output dictionary to make pandas dataframe
info['TeamNames'] = teams
info['Year'] = year
info['Seed'] = seeds
info['Results'] = results
info['ADJOE'] = adjoef
info['ADJDE'] = adjdef
info['Barthag'] = barthagf
info['efg%'] = efgf
info['efgd%'] = efgdf
info['tor'] = torf
info['tord'] = tordf
info['orb'] = orbf
info['drb'] = drbf
info['ftr'] = ftrf
info['ftrd'] = ftrdf
info['2p%'] = twopf
info['2pd%'] = twopdf
info['3p%'] = threepf
info['3pd%'] = threepdf
info['adjt'] = adjtf
info['wab'] = wabf

kpdata = pd.DataFrame(kpinfo)
TorvikData = pd.DataFrame(info)

TorvikData.to_csv('Torvik.csv')
kpdata.to_csv('KenPom.csv')

kpdata['nameyear'] = kpdata['Names'] + kpdata['Year']
TorvikData['nameyear'] = TorvikData['TeamNames'] + TorvikData['Year']

bothData = pd.merge(TorvikData,kpdata,on=['nameyear'])
del bothData['nameyear']
del bothData['Names']
del bothData['Year_y']
del bothData['Seed_y']
bothData.rename(columns = {'Year_x':'Year','Seed_x':'Seed'},inplace= True)
bothData.to_csv('CBB_Data08-19.csv')