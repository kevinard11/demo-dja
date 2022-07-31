a = [1,2,3]
print(a) #[1, 2, 3]
b = ['A string',23,100.232,'o']
print(b) #['A string', 23, 100.232, 'o']
b[0] = 1
print(b[0]) #1

print('\n Length')
c = ['A string',23,100.232,'o']
print(len(c)) #4

print('\n Index and Slicing')
d = ['one','two','three',4,5]
print(d[0]) #one
print(d[1:]) #['two', 'three', 4, 5]
print(d[:3]) #['one', 'two', 'three']

print('\n Append')
e = ['new item']
print(e+e) #['new item', 'new item']
e.append('news item')
print(e) #['new item', 'news item']

print('\n Reassign')
f = ['one','two','three',4,5]
g = ['new item']
f = f+g
print(f) #['one', 'two', 'three', 4, 5, 'new item']

print('\n Multiply')
h = ['one','two','three',4,5]
print(h*2) #['one', 'two', 'three', 4, 5, 'one', 'two', 'three', 4, 5]

print('\n Basic methods')
i = [1, 2, 3, 'append me!']
print(i.pop()) #append me!
print(i) #[1, 2, 3]
print(i.pop(0)) #1
j = ['a','e','x','b','c']
j.reverse()
print(j) #['c', 'b', 'x', 'e', 'a']
j.sort()
print(j) #['a', 'b', 'c', 'e', 'x']

print('\n Nesting and Comprehension')
k_1=[1,2,3]
k_2=[4,5,6]
k_3=[7,8,9]
k = [k_1,k_2,k_3]
print(k) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(k[0]) #[1, 2, 3]
print(k[0][0]) #1
l = [row[0] for row in k]
print(l) #[1, 4, 7]

print("\n Comprehension")
m = [x for x in 'word']
print(m) #['w', 'o', 'r', 'd']
n = [x**2 for x in range(0,11)]
print(n) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
o = [x for x in range(11) if x % 2 == 0]
print(o) #[0, 2, 4, 6, 8, 10]
p = [0,10,20.1,34.5]
q = [((9/5)*temp + 32) for temp in p]
print(q) #[32.0, 50.0, 68.18, 94.1]
r = [ x**2 for x in [x**2 for x in range(11)]]
print(r) #[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]

