import requests
from bs4 import BeautifulSoup


def extract_job(html):
    datas = html.find_all('a')
    for data in datas:
      title = data.find("span", {"class": "title"})
      if title != None:
        title = title.text
      company = data.find("span", {"class": "company"})
      if company != None:
        company = company.text
      link = data['href']
    return {
        'title': title,
        'company': company,
        'apply_link': f"https://weworkremotely.com{link}"
    }


def extract_jobs(url):
    jobs = []
    print(f"Scrapping WWR")
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("li", {"class": "feature"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word}"
    jobs = extract_jobs(url)
    return jobs

