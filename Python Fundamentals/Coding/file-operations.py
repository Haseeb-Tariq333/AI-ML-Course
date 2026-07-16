f = open("sample.txt", "r")
data = f.read()
line1 = f.readline()
print(data)
print(line1)
f.close()

## for  writing in a file ##
f = open("sample.txt", "w")
data = f.write("This is the new text which \n overrides the old text")
f.close()

## for appending data in file ##
f = open("sample.txt", "a")
data = f.write("This is the data which is \n appended to the file")
f.close()

## for creating a new file ##
# f = open("sample1.txt", "x")
# f.write("This is a new file \n this is a random text")
# f.close()

## read and write operation ##
f = open("sample.txt", "r+")
f.write("Hello hi")
f.read()
f.close()