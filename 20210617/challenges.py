import requests
import os
import sys

print("Welcome to IsItDown.py!")
print("Please write a URL or URLs you want to check. (separated by comma)")

try:
  urls = input()
  urls = urls.split(',')

  for url in urls:
    url = url.strip()
    if "http://" in url:
      reurl = requests.get(url)
      if reurl.status_code == requests.codes.ok:
        print(f"{url} is up!")
      else :
        print(f"{url} is down!")
    else:
      url = "http://" + url
      reurl = requests.get(url)
      if reurl.status_code == requests.codes.ok:
        print(f"{url} is up!")
      else :
        print(f"{url} is down!")

except:
  print(f"{url} is not a valid URL")

def restart_over():
  start_over = input("Do you want to start over? y/n ")
  if start_over == "y":
    os.system('clear')
    os.execl(sys.executable, sys.executable, *sys.argv)
  elif start_over == "n":
    sys.exit
  else:
    print("That's not a vaild answer")
    restart_over()



restart_over()
  