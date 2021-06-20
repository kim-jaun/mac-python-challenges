import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"


"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

#print(format_currency(5000, "KRW", locale="ko_KR"))





def trans_currency():
  result = requests.get(f"https://wise.com/gb/currency-converter/{incountry}-to-{outcountry}-rate?amount={money}")
  soup = BeautifulSoup(result.text, "html.parser")
  datalist = soup.find("h3", {"class": "cc__source-to-target"})





def search_table(tab_list):
  print("Where are you from? Choose a country by number")
  country = input("#: ")
  if country.isdecimal():
    country_code = int(country)
    if country_code <= len(tab_list):
      print(tab_list[country_code][2].upper())
    else:
      print("Choose a number form the list.")
      search_table(tab_list)
  else:
    print("That wasn't a number.")
    search_table(tab_list)


def table_code():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  datalist = soup.find("table", {"class": "table table-bordered downloads tablesorter"})
  tablelist = datalist.find_all('tr')
  table = []
  count = 0
  for i in tablelist:
    minilist =[]
    minilist.append(count)
    for k in i:
      if k != "\n":
        data = str(k.string)
        if data.isdecimal():
          minilist.append(int(data))
        else:
          minilist.append(data.capitalize())
    if type(minilist[4]) == type(0):
      table.append(minilist)
      count += 1
  return table


def firstwork():
  g_list = table_code()
  for i in g_list:
  print("#", i[0], i[1])
  return g_list


def startgame():
  print("Wellcom to CurrencyConvert PRO 2000 ")
  i_list = firstwork()
  search_table(i_list)

startgame()