import requests
import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

foo={}

for i in range(1,808,1):
    r=requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
    a=r.json()
    data={}
    data['id']=a['id']
    data['name']=a['name']
    data['sprite']=a['sprites']['front_default']
    foo[i]=data

writeToJSONFile('./','pokedata',foo)

#https://gist.github.com/keithweaver/ae3c96086d1c439a49896094b5a59ed0 I reffered this link to do this program.