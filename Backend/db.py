#-*- coding: UTF-8 -*-
from pymongo import MongoClient
from whois import genericWhois
import json
import re



#Função que verifica se os dados de whois já constam no banco, caso não constem eles são adicionados.
def verify(url):
    #conexao com o mongolab
    connection = MongoClient("ds155651.mlab.com", 55651)
    db = connection["whois"]
    db.authenticate("whoisbot", "whoisbot10")
    #select para encontrar se a url já foi inserida no banco
    data = db.data.find_one({"url":str(url)})
    #verifica se já esta no banco, caso contrario realiza a pesquisa
    if data is not None:
        return data[u'data']
    else:
        #chama a função que retorna o servidor de whois
        host = getWhois(url)
        #chama a função que retorna os dados do whois e arruma os problemas de encoding.
        msg = genericWhois(host,url).decode('latin-1')
        #chama a função que salva os dados buscados no banco
        save(url,msg)
        #retorna os dados pesquisados
        return msg

#Função que recebe a url e retorna o servidor de whois
def getWhois(url):
    #conexao com o mongolab
    connection = MongoClient("ds155651.mlab.com", 55651)
    db = connection["whois"]
    db.authenticate("whoisbot", "whoisbot10")
    #regex para extrair o dominio caso a url inserida esteja fora do padrão
    domain  = re.findall(r"^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)", url)[0]
    #Extracao da extensao para que localizar o servidor de whois 
    ext = domain[-3:]
    if "." in ext:
        ext=ext.replace(".","")
    #consulta na tabela de Tdl o servidor de whois
    data = db.tld.find_one({"ext":str(ext)})
    if len(data) > 0:
        return data[u'host']
    else:
        return ""

#função que salva os dados do whois no banco
def save(url,data):
    #conexao com o mongolab
    connection = MongoClient("ds155651.mlab.com", 55651)
    db = connection["whois"]
    db.authenticate("whoisbot", "whoisbot10")
    #insert no banco lidando com o problema de encode
    db.data.insert_one({'url':url,'data':data.encode('utf-8')})
    connection.close()


