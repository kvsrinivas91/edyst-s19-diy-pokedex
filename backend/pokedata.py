import requests
import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a') as fp:
        json.dump(data, fp)


for i in range(1,807,1):
    r=requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
    data={}
    a=r.json()
    data['id']=a['id']
    data['name']=a['name']
    data['sprite']=a['sprites']['front_default']
    foo={}
    foo[i]=data
    bar=json.dumps(foo)
    writeToJSONFile('./','pokedata',bar)
    print(bar)

