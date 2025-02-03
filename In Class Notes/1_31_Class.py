"""
ENGR 104
1/31/25 Class Notes
"""

myList = [0,3,17.2,28]


# a has 5 elements, but its  highest index 4
a = [6.7, "taco", 7, 9, "D"]

print(a[4])
print(a[3])
print(a[2])
print(a[1])
print(a[0])

print(a[-1])  # index -1 is last element
print(a[-2])  #negative indices work in reverse order

a[3] = "Cat"  # this changes the value at a particular index
a[-1] = 88 # this changes last element to 88 

print(a)

#string addition, i.e. concatenation
c = "I can code in python"
d = "C++"
e = c + " and " + d
print(e)
#list addition, i.e. concatenation

x = [0, "apple", 3]
y = [12.7, 3, "dog"]
z = x + y
print(z)

#intro to the range function

A = list(range(8))
print(A)

B = list(range(4,90))
print(B)

C = list(range(0,15,3))
print(C)

D = list(range(-7,10,2))
print(D)

E = list(range(16,0,-5))
print(E)



