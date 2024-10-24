#A lambda function is a simple function of the form "lambda arguments: expression"

add10=lambda x: x+10
print(add10(5))#prints 15

mult=lambda x,y:x*y
print(mult(2,3))#prints 6

#NOTE: no doubt that we can do these things by creating a func using def(),but since the lesson is about lambda functions
#we are doing it this way

points_2d=[(1,2),(15,1),(5,-1),(10,4)]
sort=sorted(points_2d,key=lambda x:x[0]+x[1])
#here the key tells us how we want to sort the list
#according to the lambda func in the key we want both the coordinates to be sorted i.e x and y

print(sort)

# a map function is of the form:
#map(func,sequence)

a=[5,6,7,8]
b=map(lambda x:x*2,a)
print(list(b))

#a filter function is of the form:
#filter(func,sequence)
#a filter function gives only those values from the sequence for which the "func" returns true

a=[1,2,3,4,5,6]
b=filter(lambda x:x%2==0,a)#odd numbers get filtered out
print(list(b))

# a reduce function is of the form "reduce(func,sequence)"
#reduce function has to be imported
# it repeatedly applies the func to the elements and returns a single value

from functools import reduce
c=[1,2,3,4]
d=reduce(lambda x,y:x*y,c)#reduce function always has two parameters,here they are x and y
print(list(d))#After repetedly applying the func to the elements of the sequence we get 24