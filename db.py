from pymongo import MongoClient
from whois import genericWhois
import json
import re

def getWhois(url):
    connection = MongoClient("ds155651.mlab.com", 55651)
    db = connection["whois"]
    db.authenticate("whoisbot", "whoisbot10")
    domain  = re.findall(r"^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)", url)[0]
    ext = domain[-3:]
    if "." in ext:
        ext=ext.replace(".","")
    data = db.tld.find_one({"ext":str(ext)})
    if len(cursor) > 0:
        return data[u'host']
    
    json_docs = [json.dumps(doc, default=json_util.default) for doc in cursor]
    return json_docs


def verify(url):
    connection = MongoClient("ds155651.mlab.com", 55651)
    db = connection["whois"]
    db.authenticate("whoisbot", "whoisbot10")
    data = db.data.find_one({"url":str(url)})
    if len(cursor) > 0:
        return data[u'data']
    else:
        msg = genericWhois(getWhois(url),url)
        save(url,msg)
        return msg

def save(url,data):
    connection = MongoClient("ds155651.mlab.com", 55651)
    db = connection["whois"]
    db.authenticate("whoisbot", "whoisbot10")
    db.data.insert_one({'url':url,'data':data})
    connection.close()
