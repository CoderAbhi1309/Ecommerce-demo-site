from django.conf import settings
import json
import re

DB = settings.DB

def writeDB(obj,loc,filename=DB):
    with open(filename, 'r') as dbjson : 
        datadict= json.loads(dbjson.read()) 
        dbjson.close()
        temp=datadict['database'][loc]
        temp.append(obj)
    
    with open(filename, 'w') as jsondb:
        json.dump(datadict, jsondb )
        jsondb.close()


def readDB(loc,filename=DB):
    with open(filename,'r') as dbjson:
        datadict=json.loads(dbjson.read())
        dbjson.close()
        temp=datadict['database'][loc]
        return temp

def findDB(userobj,filename=DB):
    with open(filename,'r') as dbd:
        dbdict=json.loads(dbd.read())
        dbd.close()
        j=0
        for i in range(len(dbdict['database']['userdata'])):
            if userobj['email']==dbdict['database']['userdata'][i]['email'] and userobj['pswd']==dbdict['database']['userdata'][i]['pswd']:
                return True 
            j+=1
        if j== len(dbdict['database']['userdata']):return False
            
             

        
    
    


