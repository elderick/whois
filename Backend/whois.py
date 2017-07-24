import socket
import re
#Chamada generica que ira trazer o dados do whois
def genericWhois(server,query):
    #Conexao com o socket
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((str(server), 43))
    #Enviando dados
    s.send(query + '\r\n')
     
    #Tratatamento da reposta
    msg = ''
    host = ''
    owner=''
    while len(msg) < 10000:
        chunk = s.recv(100)
        if(chunk == ''):
            break
        msg = msg + chunk
    
        #Now scan the reply for the whois server
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if 'nserver' in words[0] and host == '':
                    if len(re.findall(r"\.(.*?)(?:\.a*)", words[1].strip())) >= 1:
                        host = re.findall(r"\.(.*?)(?:\.a*)", words[1].strip())[0]
                        break
                if 'Name Server' in words[0] and host == '':
                    if len(re.findall(r"\.(.*?)(?:\.a*)",words[1].strip())) >= 1:
                        host = re.findall(r"\.(.*?)(?:\.a*)", words[1].strip())[0]
                        break
                    if len(re.findall(r"(?:\.)[a-zA-Z]*",words[1].strip())) >= 1:
                        host = re.findall(r"(?:\.)[a-zA-Z]*", words[1].strip())[0].replace('.','')
                        break
             
    # Retorna a resposta tratada
    return [msg,host,owner]

# a =  genericWhois('whois.registro.br','stackoverflow.com')
# print a