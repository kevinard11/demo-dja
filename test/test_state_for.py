print("\n List, if-else")
a = [1,2,3]
for num in a:
    print(num) 
#1 \n2 \n3
b = [1,2,3,4,5]
for num in b:
    if num%2 == 0:
        print(num)
    else:
        print('{} = Odd number'.format(num))
#1 = Odd Number \n2 \n3 = Odd Number \n4 \n5 = Odd Number

print("\n String")
c = 'He llo'
for num in c:
    print(num)
#H \ne \n \nl \nl \no

print("\n Tuples")
d = (1,2,3)
for num in d:
    print(num)
#1 \n2 \n3

print("\n Tuples in List")
e = [(2,4),(6,8),(10,12)]
for num in e:
    print(num)
#(2,4) \n(6,8) \n(10,12)
for (num1,num2) in e:
    print(num1)
#2 \n6 \n10

print("\n Dictionaries")
f = {'k1':1,'k2':2,'k3':3}
for item in f:
    print(item)
#k1 \nk2 \nk3
for k,v in f:
    print(v)
#1 \n2 \n3
