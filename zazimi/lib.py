import requests


def try_me():
    url = 'http://wttr.in/'
    r = requests.get(url)
    r.json()
