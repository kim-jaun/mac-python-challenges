import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""
subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]
app = Flask("DayEleven")


@app.route('/')
def home():
  return render_template("home.html", subreddits=subreddits)

@app.route('/read')
def read():
  results = []
  word = request.args
  for i in word:
    item = i
    url = f"https://www.reddit.com/r/{item}/top/?t=month"
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rending = soup.find_all("div", {"class":"_1oQyIsiPHYt6nx7VOmd1sz"})
    for card in rending:
      a = {}
      links = card.find_all("a", {"class":"SQnoC3ObvgnGjWt90zD9Z"})
      titles = card.find_all("h3", {"class":"_eYtD2XCVieq6emjKBH3m"})
      upvotes = card.find_all("div", {"class":"_1rZYMD_4xY3gRcSS3p8ODO"})
      for link in links:
        a['link'] = link['href']
      for title in titles:
        a['title'] = title.text
      for upvote in upvotes:
        a['upvote'] = upvote.text
      results.append(a)
  return render_template("read.html", word=word, item=item, results=results)

app.run(host="0.0.0.0")
