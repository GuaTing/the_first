#coding:utf-8
import sys
import json
import collections
import os
from pymongo import MongoClient
conn = MongoClient('192.168.235.55', 27017)
db = conn['admin']
db.authenticate("admin","123456")
db = conn['team_behind_sc']
table = db['Film_company']
dict0 = collections.OrderedDict()
ids = []
def get_message(f):
    with open("./film2012/"+f, "r")as f:
        lines = f.readlines()
        id = lines[0].split("`")[1]
        # print(id)
    for line in lines:
        movie_key = line.replace("\n","").replace("\"","\'").split("`")[0]
        movie_value = line.replace("\n","").replace("\"","\'").split("`")[1]
        dict0[movie_key] = movie_value
        print(json.dumps(dict0,ensure_ascii=False,indent=1))
    if id in ids:
        return
    else:
        ids.append(id)
        table.insert(dict0)
path = "./film2012"
files = os.listdir(path)
for f in files:
    get_message(f)