from flask import Flask,render_template
import requests
import json

app = Flask(__name__)

@app.errorhandler(404)  
def page_not_found(error=None):
  return ('Error 404'), 404

@app.errorhandler(500)
def page_not_found_500(e):
    return render_template('404.html'), 404

@app.route('/api/pokemon/<int:id>')
def poke(id):
    if int(id)<152 and int(id)>0:
        #r=requests.get("https://pokeapi.co/api/v2/pokemon/"+str(id))
        with open ('pokedata.json') as r:
            data=json.load(r)
            #a=r.json()
            #data['id']=a['id']['id']
            #data['name']=a['id']['name']
            #data['sprite']=a['id']['sprite']
            d=data[str(id)]
            foo={}
            foo['pokemon']=d
            bar=json.dumps(foo)
            return bar
    else:
        return ("Error, invalid "), 404
        


if __name__ == '__main__':
    app.run(host='localhost' ,port=8006)