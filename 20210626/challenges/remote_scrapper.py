import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_job(html):
    link_id = html['data-id']
    datas = html.find_all('td')
    for data in datas:
      company = data.find("span", {"class":"companyLink"})
      if company != None:
        i = company.find("h3")
        if i != None:
          companys = i.text
      titles = data.find_all("a", {"class":"preventLink"})
      for i in titles:
        title = i.find("h2")
        if title != None:
          title = title.text
    return {
        'title': title,
        'company': companys,
        'apply_link': f"https://remoteok.io/remote-jobs/{link_id}"
    }


def extract_jobs(url):
    jobs = []
    print(f"Scrapping Remote")
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("tr", {"class": "verified"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://remoteok.io/remote-{word}-jobs"
    jobs = extract_jobs(url)
    return jobs

