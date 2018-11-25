from xgoogle.search import GoogleSearch, GoogleNewsSearch
import json
import html2text
import requests
from textblob import TextBlob
from tinydb import TinyDB, Query

# disable the ssl not verified warnings
requests.packages.urllib3.disable_warnings()

db = TinyDB('results.json')

search_terms = "Michael Jackson"
gs = GoogleNewsSearch(search_terms)
gs.results_per_page = 25
results = gs.get_results()
cnt = 0
for res in results:
    print(res.title.encode('utf8'))
    title = res.title
    url = res.url
    resp = requests.get(url,verify=False)
    encoding = resp.encoding
    if not encoding: encoding = "utf-8"
    print(encoding)
    text = html2text.html2text(resp.text)
    blob = TextBlob(text)
    print(blob.sentiment)
    db.insert({'q': search_terms,'title': title, 'rank': cnt+1, 'sentiment': blob.sentiment})
    cnt += 1
