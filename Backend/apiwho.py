#-*- coding: UTF-8 -*-
import bottle
from bottle import error,response,request
from db import verify
import os

# Para rodar em e nao ter problema de bloqueio nas requests da api setamos o CORS.
class EnableCors(object):
    name = 'enable_cors'
    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Access-Control-Allow-Headers, Authorization,Access-Control-Allow-Credentials X-Requested-With,Access-Control-Allow-Origin'

            if bottle.request.method != 'OPTIONS':
                return fn(*args, **kwargs)

        return _enable_cors

app = bottle.app()

# -->> GET
# -->> /whois?url='URL_ PROCURADA'
# -->> Recebe a url procurada, chama a função que verifica se a url já está no banco e retorna as informações do dominio.
@app.route('/whois', method=['OPTIONS', 'GET'])
def whois():
    try:
        #Extrai o parametro "Url" do request e chama função que vai retornar os dados da url.
        msg = verify(request.params['url'])
        return msg
    except:
        #Em caso de problemas retorna uma mensagem generica de erro.
       return "Serviço Indisponivel para esta url, por favor tente mais tarde"
    

#Tratamento de erro
@error(404)
def error404(error):
    return 'Nothing here, sorry =('






#instancia o CORS na api.
app.install(EnableCors())

# <-- Para rodar em debug -->:
app.run(host='localhost', port=8081, debug=True)

#<-- Para rodar em prod (heroku) -->:
# app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
