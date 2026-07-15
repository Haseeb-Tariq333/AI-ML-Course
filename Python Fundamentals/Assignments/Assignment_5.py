       ######################
       ##### Question:1 #####
       ######################
  
  
       
with open("names.txt", "w") as f:
    f.write("Haseeb Tariq \nHabib Tariq \nUsman Haider \nSoman Khan \nSaad Saleem")
with open("names.txt", "r") as f:
    data = f.read()
    print(data)
    
 
    
       ######################
       ##### Question:2 #####
       ######################
       
       
       
with open("log.txt", "a") as f:
    f.write("Program run successfully")
with open("log.txt", "r") as f:
    data = f.read()
    print(data)
    
    
    
       ######################
       ##### Question:3 #####
       ######################   
       
       
       
list = [5,10,15,20,25]
new_list = [val for val in list if val > 15]
print(new_list)



       ######################
       ##### Question:4 #####
       ######################  
       
       
       
import json  
dict = {
    "Islamabad" : 200,
    "Lahore" : 100,
    "Multan" : 90
    }

with open("cities.json", "w") as f:
    json.dump(dict, f, indent=4)
with open("cities.json", "r") as f:
    py_object = json.load(f)
    for city, population in py_object.items():
        print(f"{city} : {population}")
with open("cities.json", "w") as f:
    a = input("Enter the new city name : ")
    b = int(input("Enter the population of this city"))
    py_object[a] = b
    json.dump(py_object, f, indent=4)
            
    
    
    
    
    
    
       ######################
       ##### Question:5 #####
       ###################### 
       
       
       
try:
    with open("data.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
