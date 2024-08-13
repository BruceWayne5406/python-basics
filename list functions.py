luckynumbers=[5,8,10,15,25]#creation of a list called "lucky numbers". list elements are enclosed inside []
friends=["jim","karen","steve","elon"]#creation of another list

friends.extend(luckynumbers)#this joins the list "friends" with "luckynumbers"
print(friends)#printing the list

friends.append("ambani")#this function appends an element i.e "ambani" in the list "friends"
print(friends)#printing the list

friends.insert(0,"larry ellison")#this inserts the element "larry ellison" at 
print(friends)#printing the list

luckynumbers.remove(25)#this function removes a specific element,in this case 25 from the "luckynumbers" list
print(luckynumbers)#printing the list

friends.clear()#this function deletes all the elements in the list
print(friends)#printing the list

luckynumbers.pop()#this function deletes an element from the end of the list
print(luckynumbers)#printing the list



nlist=["me","me","them","those"]#creating another list consisting of string elements
print(nlist.count("me"))#this function 

luckynumbers.sort()#here the numbers are sorted in increasing/decreasing order
print(luckynumbers)#printing the list

luckynumbers.reverse()#the sequence of all the elements gets reversed
print(luckynumbers)#printing the list

jnumbers=luckynumbers.copy()
print(jnumbers)
