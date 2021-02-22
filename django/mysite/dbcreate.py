import json
f=open('db.json','r')
k=json.loads(f.read())
print(k['database']['userdata'][0]['email'])

