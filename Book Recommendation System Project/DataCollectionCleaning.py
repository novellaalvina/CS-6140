# web scraping from project gutenberg website
import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://www.gutenberg.org/ebooks/search/?sort_order=downloads"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

links = []
for line in soup.findAll('a', {'class': 'link'}):
    links.append(line.get('href'))

links = links[2:]

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

book = {}
for link in links:
    ebook_no = link.replace('/ebooks/', '')
    url2 = 'https://www.gutenberg.org/ebooks/'+ str(ebook_no)
    # print(url2)
    r = requests.get(url2)
    soup2 = BeautifulSoup(r.text, features="html.parser")

    detail = {}

    detail['title'] = soup2.find(itemprop = 'headline').get_text().strip('\n')
    detail['author'] = soup2.find(itemprop = 'creator').get_text().strip('\n')

    langs = []
    for lang in soup2.find(itemprop = 'inLanguage').findAll('td'):
        langs.append(lang.get_text())
    detail['language'] = langs

    subjs = []
    for subj in soup2.findAll('a', {'class':'block'}):
        subjs.append(subj.get_text('href').strip('\n'))
    detail['subject'] = subjs

    date = soup2.find(itemprop = 'datePublished').get_text().replace(',', '').split()
    month = months[date[0]]
    day = int(date[1])
    year = int(date[2])
    date_format = str(year) + '-' +str(month) + '-' + str(day)
    detail['released date'] = date_format

    # detail['released date'] = datetime.strptime(soup2.find(itemprop = 'datePublished').get_text().strip('\n'), '%d %b %Y')

    detail['download number'] = int(soup2.find(itemprop = "interactionCount").get_text().strip('downloads in the last 30 days.'))

    book[ebook_no] = detail

for ebook, detail in book.items():
    print("ebook", ebook, "detail", detail)

    just need paramater self. no need other parameter
    needs to double the self.number, so self.number needs to be multiplied back so the instance variable number in the class is changed. Like self.number = self.number * 2 
    syntax for multiplication in python is *
    incorrect syntax

