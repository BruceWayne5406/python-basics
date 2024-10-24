import json
data='{"var1":"harsh","var2":"58"}'#right now "data" is in json format as it has double quotes

parsed=json.loads(data)# data has been parsed and can be used in python
print(parsed)

data2={"name":"harsh","cars":["aston martin","maybach","bugatti"],"fridge":("roti",540),
       "is bad":False
       
       }
jscomp=json.dumps(data2)
print(jscomp)#now data 2 has been coverted to javascript compatible object from python