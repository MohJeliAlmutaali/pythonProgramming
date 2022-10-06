#This will not run on online IDE
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())
quotes = []

table = soup.find('div', attrs = {'id':'all_quotes'})

#row = soup.find('div', attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'})
#print(row)
for row in table.findAll('div',
                        attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
#    print(row)
    print(row.img['alt'])
    quote = {}

    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)



