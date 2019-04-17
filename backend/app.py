from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/api/pokemon/<id>')
def poke(id):
    r=requests.get("https://pokeapi.co/api/v2/pokemon/"+str(id))
    data={}
    a=r.json()
    data['id']=a['id']
    data['name']=a['name']
    data['sprite']=a['sprites']['front_default']
    foo={}
    foo['pokemon']=data
    bar=json.dumps(foo)
    return bar

if __name__ == '__main__':
    app.run(host='localhost' ,port=8006)