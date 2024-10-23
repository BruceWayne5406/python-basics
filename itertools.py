#itertools module is a collection of datatypes for handling iterators
#iterators are datatatypes that can be used in a for loop

#itertools: product,permutations,combinations,accumulte,groupby and infinite iterators

from itertools import product
a=[1,2]
b=[3,4]
prod=product(a,b)
print(list(prod))# here we get the cartesian product

from itertools import permutations #this will give all possible permutations
st=[1,2,3]
p1=permutations(st)
print(list(p1))

p1=permutations(st,2)#here the second parameter i.e 2 specifies the length

from itertools import combinations 
#combinations


l2=[1,2,3,4]
comb=combinations(l2,2)# here we will get combinations without any repition 
print(list(comb))

#for eg we will not get 1,1 or 2,2 combination
#to do so we use the following

from itertools import combinations , combinations_with_replacement
l3=[3,4,5,6]
comb_wr=combinations_with_replacement(l3,2)
print(list(comb_wr))

#accumulate function is used to print accumulated sums or products
from itertools import accumulate

l4=[5,6,7,6,8]
acc=accumulate(l4)
print(l4)
print(list(acc))

# for products:
from itertools import accumulate
import operator
accc=accumulate(l4,func=operator.mul)
print(l4)
print(list(accc))

az=accumulate(l4,func=max)
print(list(az))



from itertools import groupby #didnt understand properly retry another time
persons=[{"name:tim","age:25"},{"name:dan","age:25"},{"name:lisa","age:27"}
         ,{"name:claire","age:28"}]
gp_obj=groupby(persons, key=lambda x: x["age"])
for key,value in gp_obj:
    print(key,list(value))


from itertools import count,cycle,repeat
for i in count(10):# cojunt funcion basically staryts the count from the given paramater(here 10) and goes to infinity
    print(i)

a=[1,2,3]
for i in cycle(a): #cycle function reads the given list infinite times here
    print(i)

for i in repeat(1,4):# repeat function gives the parameter repeatedly in this case 1. the second parameter is the number of times
    # you want the parameter to repeat in this case 4
    print(i)

