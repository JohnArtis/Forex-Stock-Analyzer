import urllib.request as rq
from urllib import *
def webParser(x):
    
    URL = "https://news.search.yahoo.com/"

    values = {x : "currencies"}
    data = parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    req = request.Request(URL, data)
    resp = request.urlopen(req)
    respData = resp.read()
    print(respData)

