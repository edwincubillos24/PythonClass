a=2
def funcion1():
    b=3
    c=a+b
    return c
print(funcion1())

a = 0.1 + 0.2
print(a == 0.3)
print(0.1 + 0.2 == 0.3)

print(9//2)44

nameList = ['Harsh', 'Patrik', 'Bob', 'Dhruv']
pos = nameList.index("Carlos")
print(pos * 3)

D = dict()
for x in enumerate(range(2)):
    D[x[0]] = x[1]
    D[x[1]+7] = x[0]
print(D)

def myfunc(a):
    a = a + 2
        a = a * 2
    return a

print myfunc(2)

i=0
while i < 3:
    print(i)
    i +=1
else:
    print(0)

def f(value, values):
    v=1
    values[0]=44
t=3
v=[1,2,3]
f(t,v)
print(t,v[0])