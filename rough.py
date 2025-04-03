from bs4 import BeautifulSoup
import requests
import json


resp = requests.get("https://www.tutorialspoint.com/")



html_doc = BeautifulSoup(resp.content, 'html.parser')

anchor_list = html_doc.find_all('a')
count = 0
data = {}

for link in anchor_list:
    ref = link.get('href')
    if "https" in ref:
        count += 1
        data[f"link:{count}"] = ref 

print(json.dumps(data,indent=2))
        # print(ref)
