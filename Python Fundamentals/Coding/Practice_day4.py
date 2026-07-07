info = [
    ("Haseeb", "Math"),
    ("Alice", "AI"),
    ("Max", "DBMS"),
    ("Ahmed", "MSE"),
    ("Haseeb", "ADBMS"),
    ("Alice", "DBMS"),
    ("Max", "Math"),
    ("Ahmed", "AI")
]
courses = set()
for name, course in info:
    if course == "Math":
        print(name)
        
dict = {}
for name, course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
        
print(dict)