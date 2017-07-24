# Whois
You can try all the features here: https://elderick.github.io/whois/

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

Debbug request example: (**Dont Forget to run api in debug**)
`https://whoisappp.herokuapp.com/whois?url=google.com`
