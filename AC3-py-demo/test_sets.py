a = set()
print(a) #set()
b = [1,1,2,2,3,4,5,6,1,1]
print(b) #[1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
print(set(b)) #{1, 2, 3, 4, 5, 6}
c = set()
c.add(1)
print(c) #{1}
c.add(2)
print(c) #{1, 2}
c.add(1)
print(c) #{1, 2}