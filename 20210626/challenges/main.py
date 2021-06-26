"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""


from flask import Flask, render_template, request, redirect, send_file
from so_scrapper import get_jobs as so_jobs
from wwr_scrapper import get_jobs as wwr_jobs
from remote_scrapper import get_jobs as remote_jobs
from save import save_to_file as save_file



app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/term")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = wwr_jobs(word) + remote_jobs(word) + so_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template(
    "report.html", 
    searchingBy=word, 
    resultsNumber=len(jobs),
    jobs=jobs
    )

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_file(jobs)
    return send_file('jobs.csv')
  except:
    return redirect("/")


app.run(host="0.0.0.0")