import os
import requests
from bs4 import BeautifulSoup

os.system("clear")



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
    print("That wasn't a number.")
    return finding()



def find_table():
  url = "https://www.iban.com/currency-codes"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  tablesorter = soup.find("table", {"class":"table table-bordered downloads tablesorter"})
  tables = tablesorter.find_all("tr")
  tablelist = []
  count = 0
  for table in tables[1:]:
    minilist = []
    minilist.append(count)
    for minitable in table:
      if minitable != "/n":
        data = str(minitable.string)
        if data.isdecimal():
        minilist.append(int(data))
        else:
        minilist.append(data[0] + data[1:].lower())
    if type(minilist[4]) == type(0):
    tablelist.append(minilist)
    count += 1
  return tablelist

def firstwork():
  tablelist = find_table()
  for i in tablelist:
    print("#", i[0], i[1])
    return tablelist

def startgame():
  print("Hello! Please choose select a country by number:")
  tablelist = firstwork()
  finding(tablelist)
