"""
Class code
2/3/2025
"""

evensList = list(range(2,1001,2))   #using range for all evens from 2 to 1000
listLength = len(evensList)
print(f"The length of my evens list is {listLength}")

#different ways to insert into a list
listA = list(range(1,11))
print(listA)
listA.append(99)
print(listA)
listA.insert(3,-99)
print(listA)

#different ways to remove from a list


del listA[3]
print(listA)
print(f"the poppped value is {listA.pop(7)}")
print(listA)
listA.remove(6)

#looking at "slices" of a list

print(listA)
print(listA[:3])
print(listA[4:])
print(listA[2:6])

listB = list(range(1,17))
print(listB[0::2])
print(listB[1::2])
print(listB[2:15:3])

#sorting and reversing a list

listC = [5,-8,10,3,7]
listC.sort()
print(listC)
listD = ["dog", "elephant", "cat"]
listD.sort()
print(listD)

listD.reverse()
print(listD)



