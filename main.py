import os
import json

from src.modules import coreController
from src.modules import logController

jsonpath = './list.json'
urllist = []

with open(jsonpath, 'r') as j:
    data = json.load(j)

for k, v in data.items():
    name = k
    url = v
    urllist.append(name, url)
coreController(urllist)
