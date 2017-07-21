#-*- coding: UTF-8 -*-
import bottle
from bottle import error,response,request
from db import verify

# <-- Para rodar em debug -->:
# Para rodar em e não ter problema de bloqueio nas requests da api descomente o CORS 
class EnableCors(object):
    name = 'enable_cors'
    api = 2
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


@app.route('/whois', method=['OPTIONS', 'GET'])
def whois():
    # -->> GET
    # -->> /whois?url='URL_ PROCURADA'
    # -->> Recebe a url procurada, chama a função que verifica se a url já está no banco e retorna as informações do dominio.
    return verify(request.params['url']info)


@error(404)
def error404(error):
    return 'Nothing here, sorry =('






# <-- Para rodar em debug -->:
app.install(EnableCors())
app.run(host='localhost', port=8081, debug=True)

#<-- Para rodar em prod (heroku) -->:
# app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
