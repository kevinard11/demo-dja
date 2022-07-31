from random import randint, shuffle


print(" Range")
print(list(range(0,12))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list(range(0,11,2))) #[0, 2, 4, 6, 8, 10]

print('\n Enumerate')
a = 'abcde'
print(list(enumerate(a))) #[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
for i,letter in enumerate(a):
    print("At index {} the letter is {}".format(i,letter))
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

print('\n Zip')
b = [1,2,3,4,5]
c = ['a','b','c','d','e']
print(list(zip(b,c))) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
for item1, item2 in zip(b,c):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))
# For this tuple, first item was 1 and second item was a
# For this tuple, first item was 2 and second item was b
# For this tuple, first item was 3 and second item was c
# For this tuple, first item was 4 and second item was d
# For this tuple, first item was 5 and second item was e

print("\n in and not in")
d = 'x' 
e = ['x','y','z']
print(d in e) #True
print(d not in e) #False
f = '1'
print(f in e) #False
print(f not in e) #True

print("\n min and max")
g = [10,10,30,40,100]
print(min(g)) #10
print(max(g)) #100

print("\n random")
h = [10,10,30,40,100]
shuffle(h)
print(h) #[30, 40, 10, 10, 100] (shuffle the value in the list)
print(randint(0,100)) #65 (random number between 0 to 100 (0 and 100 include))

print("\n input")
i = input('Enter Something into this box: ')
print(i) #test (any string that typed)


