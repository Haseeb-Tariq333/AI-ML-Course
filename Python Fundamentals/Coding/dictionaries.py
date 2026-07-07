info = {
    "name" : "Haseeb Tariq",
    "age" : 19,
    "cgpa" : 3.25,
    "subjects" : ["AI", "DBMS", "OOP"]  
}

print(info)
print(type(info))
info["cgpa"]=3.5
print(info["cgpa"])
print(info.keys()) ## returns keys
print(info.values())  ## returns values
print(info.items()) ## returns (key,val) pairs
print(info.get("cgpa"))
info.update({
    "city" : "Islamabad"
})
print(info)