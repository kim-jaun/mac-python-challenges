import requests
import os
import sys

print("Welcome to IsItDown.py!")
print("Please write a URL or URLs you want to check. (separated by comma)")

ur = input()
u = ur.lower()
urls = u.split(',')


def req_url():
  try:
    reurl = requests.get(url)
    if reurl.status_code == requests.codes.ok:
      print(f"{url} is up!")
  except:
    print(f"{url} is down!")


for url in urls:
  url = url.strip()
  if "http://" in url and "." in url:
    req_url()
  elif "." in url:
    url = "http://" + url
    req_url()
  else:
    print(f"{url} is not a valid URL")


def restart_over():
  sta_over = input("Do you want to start over? y/n ")
  start_over = sta_over.lower()
  if start_over == "y":
    os.system('clear')
    os.execl(sys.executable, sys.executable, *sys.argv)
  elif start_over == "n":
    sys.exit
  else:
    print("That's not a vaild answer")
    restart_over()



restart_over()