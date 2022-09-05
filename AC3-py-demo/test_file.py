print(" Create file")
a = open('test.txt','w') #open file (w) create new or overwrite(delete the previous) file only write can't read

print("\n Write to file")
print(a.write('This is a new line')) #write to file; output the number of word that write
#print(a.read()) #fail; because a is not readable only wirteable
a.close() #close before work with another file

print("\n Open file")
b = open('test.txt', 'r+') #open file (r+) readable and writeable
print(b.read()) #read all line in the file
print(b.read()) #fail to read because the file already read until the last line
print(b.seek(0)) #set the line into first line again
print(b.read()) #read all line in the file again
print(b.seek(0)) #set the line into first line again
print(b.readlines()) #read the file line by line; output list line by line
b.close() #close before work with another file

print("\n Append")
c = open('test.txt','a+') #open file (a+,a) not overwrite file; readable
print(c.write('\nThis is text being appended to test.txt'))  #write to file; output the number of word that write
print(c.write('\nAnd another line here.'))  #write to file; output the number of word that write
print(c.read()) #fail to read because the file already write from the last line
print(c.seek(0)) #set the line into first line again
print(c.read())  #read all line in the file 
print(c.close()) #close before work with another file

print("\n Iterate")
for line in open('test.txt'):
    print(line)
