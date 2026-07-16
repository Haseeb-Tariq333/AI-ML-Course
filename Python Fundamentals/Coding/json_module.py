import json

json_str = '{"name" : "Haseeb", "isTeacher" : true}'

py_obj = json.loads(json_str)

print(py_obj)

## mobinf from python object to json object ##
py_obj = {'name': 'Haseeb', 'isTeacher': True}

json_obj = json.dumps(py_obj)
print(json_obj)


## Reading from file ##
with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)
    
    
with open("data.json", "w") as f:
    py_obj = {'name': 'Haseeb', 'isTeacher': True, 'address': {'city': 'Rawalpindi', 'country': 'Pakistan'}}
    json.dump(py_obj, f, indent= 4, sort_keys=  True)
    