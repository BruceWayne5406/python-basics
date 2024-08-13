luckynumbers=[5,8,10,15,25]
friends=["jim","karen","steve","elon"]

friends.extend(luckynumbers)
print(friends)

friends.append("ambani")
print(friends)

friends.insert(0,"larry ellison")
print(friends)

luckynumbers.remove(25)
print(luckynumbers)

friends.clear()
print(friends)

luckynumbers.pop()
print(luckynumbers)



nlist=["me","me","them","those"]
print(nlist.count("me"))

luckynumbers.sort()
print(luckynumbers)

luckynumbers.reverse()
print(luckynumbers)

jnumbers=luckynumbers.copy()
print(jnumbers)