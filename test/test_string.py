a = 'hello'
print(a) #hello
a = "hello"
print(a) #hello
a = "hell'o"
print(a) #hell'o
a = "hell\no"
print(a) #hell 
         #o

print("\n Length and Indexing")
b = 'hello'
print(len(b)) #5
print(b[0]) #h
print(b[1]) #e
print(b[-1]) #o
print(b[0:]) #hello
print(b[1:]) #ello
print(b[1::]) #ello
print(b[:4:]) #hell
print(b[::-1]) #olleh
print(b[:2:-1]) #ol
print(b[::-1][1:4]) #ell


print("\n Concat")
c = 'hello'
d = 'world'
print(c+' '+d) #hello world

print("\n Multiply")
e = 'hello'
print(e*10) #hellohellohellohellohellohellohellohellohellohello

print("\n Upper Lower Split")
f = 'heLLo wOrld'
print(f.upper()) #HELLO WORLD
print(f.lower()) #hello world
print(f.split()) #['heLLo', 'wOrld']
print(f.split('w')) #['heLLo ', 'Orld']
print(type(f.split())) #<class 'list'>

print("\n Format and conversion string")
g = 'hello'
h = 'world'
print(g + ' {}'.format(h)) #hello world
print(g +' %s' %h) #hello world
print(g +' %s %s' %(h,g)) #hello world hello
print(g +' %r' %h) #hello 'world'
print(g +' %r' %('\t'+h)) #hello '\tworld'

print('\n Conversion number and padding')
i = 3.75
print('%s' %i) #3.75
print('%d' %i) #3
j = 13.144
print('%5.2f' %(13.144)) #13.14
print('%1.0f' %(13.144)) #13
print('%1.5f' %(13.144)) #13.14400
print('%10.2f' %(13.144)) #     13.14
print('%25.2f' %(13.144)) #                    13.14

print('\n Multiple Format')
k = 'hi'
l = 3.1415
m = 'bye!'
print('First: %s, Second: %5.2f, Third: %r' %(k,l,m)) #First: hi, Second:  3.14, Third: 'bye!'
print('The {2} {1} {0}'.format(k,l,m)) #The bye! 3.1415 hi
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=k,b=l,c=m)) #First Object: hi, Second Object: 3.1415, Third Object: bye!
print('A {p} saved is a {p} earned.'.format(p=k)) #A hi saved is a hi earned.

print('\n Padding, Allignment, Precision')
print('{0:8} | {1:9}'.format('Fruit', 'Quantity')) #Fruit    | Quantity
print('{0:8} | {1:9}'.format('Apples', 3.)) #Apples   |       3.0
print('{1:8} | {0:9}'.format('Oranges', 10)) #      10 | Oranges
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right')) #Left     |  Center  |    Right
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33)) #11       |    22    |       33
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right')) #Left==== | -Center- | ...Right
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33)) #11====== | ---22--- | ......33
print('This is my ten-character, two-decimal number:%10.2f' %13.579) #This is my ten-character, two-decimal number:     13.58
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579)) #This is my ten-character, two-decimal number:     13.58

print('\n Format with f strings')
n = 'Fred'
print(f"He said his name is {n}.") #He said his name is Fred.
print(f"He said his name is {n!r}") #He said his name is 'Fred'
o = 23.45678
print("{0:10.4f}".format(o)) #   23.4568
print(f"{o:{10}.{6}}") #   23.4568
p = 23.45
print("{0:10.4f}".format(p)) #   23.4500
print(f"{p:{10}.{6}}") #     23.45
print("{0:10.4f}".format(p)) #   23.4500
print(f"{p:10.4f}") #   23.4500