def add_num(num1,num2):
    return num1+num2
a = add_num(2,1)
print(a) #3

print("\n Map")
def square(num):
    return num**2
my_nums = [1,2,3,4,5]
b = list(map(square,my_nums))
print(b) #[1, 4, 9, 16, 25]

print("\n Filter")
def odd(num):
    return num%2 == 0
my_nums = [1,2,3,4,5]
c = list(filter(odd,my_nums))
print(c) #[2, 4]

print("\n Lambda")
d = lambda num,nums: num*nums
print(d(2,3)) #6
e = list(map(lambda num: num ** 2, my_nums))
print(e) #[1, 4, 9, 16, 25]
f = list(filter(lambda num: num%2 == 0, my_nums))
print(f) #[2, 4]


x = 25

def printer(x):
    x = 50
    return x

printer(x)
print(x)



