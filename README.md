# Whois
You can try all the features here: https://elderick.github.io/whois/
-Please be patient on the first query, we need to wakeup some heroku dinos and put they to work(they are soo lazy!).

- database hosting: https://mlab.com/
- api hosting:https://www.heroku.com/


## How to run api in debug:
- Install python https://www.python.org/ (make sure to install version **2.7**)
- Open the folder Backend.
- Install requeriments.
`pip install -r requirements.txt`
- Run api
`python whois.py`

## How to run Http in debug:
- Install python https://www.python.org/ (make sure to install version **2.7**)
- In the main folder type:
`python -m SimpleHTTPServer 8000`
- Go to:
`http://localhost:8000` 
 

## Routes
| ROUTE         |  METHOD       | ACTION                     |
| ------------- |:-------------:| --------------------------:|
| /whois        |     GET       | Get domain info from a url |

Request example:
`https://whoisappp.herokuapp.com/whois?url=google.com`

Debug request example: (**Dont Forget to run api in debug**)
`http://localhost:8081/whois?url=terra.com.br`


## TODO:
- Remove subdomains from the domain field
- Improve "De/Para"
