import os
import requests
from bs4 import BeautifulSoup

def finding(biglist):
  country = input("#: ")
  if country.isdecimal():
      number = int(country)
      if number <= len(biglist):
        print("You chose", biglist[number][1])
        print("The currency code is", biglist[number][3].upper())
      else:
        print("Choose a number from the list.")
        return finding()
  else:
    print("That wasn\'t a number.")
    return finding


def findurlcode():
  indeed_result = requests.get('https://www.iban.com/currency-codes')
  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
  datalist = indeed_soup.find("table", {"class": "table table-bordered downloads tablesorter"})
  pages = datalist.find_all('tr')
  biglist = []
  count = 0
  for i in pages[1:]:
    minilist = []
    minilist.append(count)
    for k in i:
      if k != "\n":
        data = str(k,string)
        if data.indecimal():
          minilist.append(int(data))
        else:
          minilist.append(data[0] + data[1:].lower())
    if type(minilist[4]) == type(0):
      biglist.append(minilist)
      count += 1
  return biglist


def firstwork():
  boglist = findurlcode()
  for i in biglist:
    print("#", i[0], i[1])
  return biglist


def startgame():
  print("Hello! Please choose select a country by number:")
  biglist = firstwork()
  finding(biglist)
