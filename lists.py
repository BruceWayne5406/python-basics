#lists are one of the most basic data structures in python
#lists are mutable which means changes can be made to a list
#the elements of a list are enclosed in []

mylist=["dad","mom","me","again me"]#here we have created a list consisting of several strings
print(mylist)#printing the list

#note: the elements of a list are counted from 0. this means that the first element in a list is at 0th position and not 1st.

print(mylist[0])#this prints the element at the 0th position i.e "dad".

#the position of the last element in a list can also be addressed by -1

print(mylist[-1])#prints the last element in the list
print(mylist[1:])#starts printing from the 2nd element till the last one.
print(mylist[0:2])#starts printing from the 1st element till the element on position 2(excluded)

print(mylist.index("dad"))#prints the position of the element "dad" in the list
mylist[3]="again dad"#changing the element on position 3 to "again dad"
print(mylist[3])#printing the element
