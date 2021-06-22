import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

def main_hire_lists():
  try:
    alba_url = "http://www.alba.co.kr"

    html_doc = requests.get(alba_url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    main_hire = soup.find(id="MainSuperBrand")
    main_hire_lists = main_hire.find_all(class_="impact")
    return main_hire_lists
  except:
    return None


def scrap_page(main_hire_lists):
  if main_hire_lists == None:
    return "Did not get alba_url..!!T.T\nTry Again!"
  else:
    for main_hire_list in main_hire_lists:
      company = main_hire_list.find(class_="company").get_text()
      company_hire_url = main_hire_list.find(class_="goodsBox-info").get("href")
      company_hire_doc = requests.get(company_hire_url).text
      company_hire_soup = BeautifulSoup(company_hire_doc,'html.parser')
      company_hire_table = company_hire_soup.find(id="NormalInfo")
      company_hire_rows = company_hire_table.find_all("tr", {'class': ''})[1:]
      
      company_hire_lists = []

      if (len(company_hire_rows) == 1):
        continue
      else:
        for company_hire_row in company_hire_rows:
          place = company_hire_row.find("td").text
          title = company_hire_row.find("td", class_="title").find("span", class_="company").text
          work_time = company_hire_row.find(class_="data").find("span").text
          pay = company_hire_row.find(class_="payIcon").text + company_hire_row.find(class_="number").text
          upload_date = company_hire_row.find(class_="regDate").text
          company_hire_lists.append([place, title, work_time, pay, upload_date])

        with open(f"{company}.csv", 'w') as f:
          writer = csv.writer(f)
          writer.writerow(["place","title","time","pay","date"])
          for company_hire_list in company_hire_lists:
            writer.writerow(company_hire_list)

scrap_page(main_hire_lists())