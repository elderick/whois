#!/usr/bin/python
#-*- coding: UTF-8 -*-
import socket, sys, re
import unicodecsv
import time
 
#whois query generico que ira trazer o retorno
def perform_whois(server , query) :
    #Conexao com o socket
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((server , 43))
     
    #Enviando dados
    s.send(query + '\r\n')
     
    #Tratatamento da reposta
    msg = ''
    while len(msg) < 10000:
        chunk = s.recv(100)
        if(chunk == ''):
            break
        msg = msg + chunk
     
    #Retorna a resposta tratada
    return msg

# Funcao que trata a url afim de pegar o dominio e extensão 
def getWhoisData(dominio,whois):
    #remove http and www
    domain = domain.replace('http://','')
    domain = domain.replace('https://','')
    domain = domain.replace('www.','')
    domain = domain.replace('/','')
     
    #get the extension
    ext = domain[-3:]
    if "/" in ext: 
         ext = domain[-4:].replace("/","")
    #chama a funcao que faz o request no whois
    msg = genericWhois(whois,domain)

    #Return the reply
    return msg

# Function to perform the whois on a domain name
def get_whois_data(domain):
     
    #remove http and www
    domain  = re.findall(r"^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)", domain)[0]
    domain = domain.replace('http://','')
    domain = domain.replace('https://','')
    domain = domain.replace('www.','')
    domain = domain.replace('/','')
     
    #get the extension , .com , .org , .edu
    ext = domain[-3:]
    if "/" in ext: 
         ext = domain[-4:].replace("/","")
        
     
    #If top level domain .com .org .net
    if(ext == 'com' or ext == 'org' or ext == 'net' or ext == 'gov'):
        whois = 'whois.internic.net'
        msg = perform_whois(whois , domain)
        emails=[]
        consolemails=''
        #Now scan the reply for the whois server
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if  'e-mail' in words[0]:
                    emails.append(words[1])
        
        for email in emails:
            emailformatado=email.strip()
            consolemails = consolemails + "{0},".format(emailformatado)
        with open("emails.csv", "ab+") as f:
            writer = unicodecsv.writer(f, delimiter=';', quotechar='"', encoding='utf-8')
            writer.writerow([domain,consolemails])

    elif(ext == 'us'):
        whois = 'whois.nic.us'
        msg = perform_whois(whois , domain)
        emails=[]
        consolemails=''
        #Now scan the reply for the whois server
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if  'e-mail' in words[0]:
                    emails.append(words[1])
        
        for email in emails:
            emailformatado=email.strip()
            consolemails = consolemails + "{0},".format(emailformatado)
        with open("emails.csv", "ab+") as f:
            writer = unicodecsv.writer(f, delimiter=';', quotechar='"', encoding='utf-8')
            writer.writerow([domain,consolemails])

    elif(ext == '.br'):
        whois = 'whois.registro.br'
        msg = perform_whois(whois , domain)
        emails=[]
        consolemails=''
        #Now scan the reply for the whois server
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if  'e-mail' in words[0]:
                    emails.append(words[1])
        
        for email in emails:
            emailformatado=email.strip()
            consolemails = consolemails + "{0},".format(emailformatado)
        with open("emails.csv", "ab+") as f:
            writer = unicodecsv.writer(f, delimiter=';', quotechar='"', encoding='utf-8')
            writer.writerow([domain,consolemails])
    #Or Country level - contact whois.iana.org to find the whois server of a particular TLD
    else:
        #Break again like , co.uk to uk
        ext = domain.split('.')[-1]
         
        #This will tell the whois server for the particular country
        whois = 'whois.iana.org'
        msg = perform_whois(whois , ext)
         
        #Now search the reply for a whois server
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if 'whois.' in words[1] and 'Whois Server (port 43)' in words[0]:
                    whois = words[1].strip()
                    break;
     
    #Now contact the final whois server
    msg = perform_whois(whois , domain)
     
    #Return the reply
    return msg



# def parseData(domain,data):
#     data = str(data.replace('\n','\\n'))
#     regex = r"(?:e-mail:)(.*?)(?:.ncountry)"
#     emails = re.findall(r"(?:e-mail:)(.*?)(?:.ncountry)", data)
#     consolemails=''
#     for email in emails:
#         emailformatado=email.strip()
#         consolemails = consolemails + "{0},".format(emailformatado)
#     if consolemails != '':
#         consolemails = consolemails[:-1]
#         with open("emails.csv", "ab+") as f:
#             writer = unicodecsv.writer(f, delimiter=';', quotechar='"', encoding='utf-8')
#             writer.writerow([domain,consolemails])
#     else:
#          with open("erros.csv", "ab+") as f:
#             writer = unicodecsv.writer(f, delimiter=';', quotechar='"', encoding='utf-8')
#             writer.writerow([domain])
# end
# get the domain name from command line argument
# domain_name = sys.argv[1]
lista = []
with open("Sites.txt", "ab+") as f:
    content = lista.append(f.readlines())
wordslist = lista
for word in wordslist[0]:
    domain_name = word.replace('\r', '').replace('\n', '')
    get_whois_data(domain_name)
    time.sleep(5.3)