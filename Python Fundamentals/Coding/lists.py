marks = [100, 78, 56,23]
print(marks)
print(marks[0])
print(marks[3])
print(marks[0:3])  ## Slicing 
print(marks[:-1]) 
marks[0]= 34 ## Reassigning values 
print(marks)

## Methods 
marks.append(100)
marks.append(50)
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)

marks.insert(2, 100) ## insert(index, val)
print(marks)

## Loops ## 
for val in marks:
    print(val)