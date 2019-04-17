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

#https://gist.github.com/keithweaver/ae3c96086d1c439a49896094b5a59ed0 I reffered this link to do this program.