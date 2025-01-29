"""
Notes from ENGR 104
1.27.2025
"""

print("Hello world!")

# this is a comment, it's not executed -- it's just for reference

# playing with variables

a = 17.2 #a floating point type
b = 10//3 #an integer type
c = "Cat" #a string type
d = 3 ** 4 # an integer type based on exponentiation

a = a + 10
a += 3   # same as a = a + 3
a *= 2   # same as a = a * 2

#Problem x.x

print("The value of a is:",a, "which is really big!")
#print f is a hack to print values of variables inside quotes
print(f"The value of a is: {a} which is really big!")

print("\n \n \n \t \t Matt")


v_0 = 10 #initial velo 10 m/s
g = 9.81 #gravity in m/s^2
t = 2 #time in seconds 
v = round(v_0 - g*t,3) #velecoity in m/s rounded
print(f"The velocity at time {t} seconds is {v}m/s")







