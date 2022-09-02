#list


list1=[1,2,3,4,5]
list2=[7,8,9,10]

print("Appending an element to list:")
list1.append(5)
print(list1)

print("Remove an element from list:")
list2.remove(8)
print(list2)

print("poping an element from list:")
print(list1.pop(4))

print("concatenation of list:")
print(list1+list2)

print("Repeating a list:")
print(list1*2)

print("Slicing a list:")
print(list1[1:3])

print("reversing the list:")
print(list1[::-1])

print("Minimum element of list:")
print(min(list1))

print("Maximum element of list:")
print(max(list2))

print("Length of the list:")
print(len(list1))


#sets


set1={1,2,3,4,5,8,9}
set2={8,9,10,11,"lab"}
set3={}
list1=[1,11,6,5,9]

print("length of the set:")
print(len(set1))

print("type of ") 
print(type(set1))

print("popping an element:")
print(set1.pop())

print("To check if the element is present:")
print("lab" in set2)

print("to check if the element is not present:")
print("lab" not in set1)

print("the minimum of set: ")
print(min(set1))

print("the maximum of set:")
print(max(set1))

print("remove element of set2 from set1:")
print(set1-set2)

print("conversion of list to set")
print(set(list1))

print(set2.clear)

print("print a set")
print(set3)
print("set3 deleted")
del(set3)
print(set3)
