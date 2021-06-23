import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
newurl = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popularurl = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")
DataBagenew = []
innew = []
DataBagePopular = []
inpopular = []
DataBagecom = []


def populardataget():
    popular = requests.get(popularurl)
    populardic = popular.json()
    for i in populardic['hits']:
        if i['num_comments'] != 0 and i['title'] != None:
            if i['objectID'] not in inpopular:
                inpopular.append(i['objectID'])
                DataBagePopular.append(i)
    return DataBagePopular


def newdataget():
    new = requests.get(newurl)
    populardic = new.json()
    for i in populardic['hits']:
        if i['title'] != None:
            if i['objectID'] not in innew:
                innew.append(i['objectID'])
                DataBagenew.append(i)
    return DataBagenew


@app.route("/")
def home():
    order_by = request.args.get('order_by')
    print(order_by)
    if order_by == "new":
        if DataBagenew:
            DataBage = DataBagenew
        else:
            DataBage = newdataget()
        return render_template("index.html", data=DataBage, order=order_by)
    elif order_by == "popular":
        if DataBagePopular:
            DataBage = DataBagePopular
        else:
            DataBage = populardataget()
        return render_template("index.html", data=DataBage, order=order_by)
    else:
        if DataBagePopular:
            DataBage = DataBagePopular
        else:
            DataBage = populardataget()
        return render_template("index.html", data=DataBage, order=order_by)


@app.route("/<number>")
def comment(number):
    com = requests.get(f"{base_url}/items/{number}")
    comdic = com.json()
    return render_template("detail.html", data = comdic)

def startgame():
  app.run(host="0.0.0.0")

startgame()