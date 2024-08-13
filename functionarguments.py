#parameters are the values that are passed inside the brackets while defining a function
#arguments are the values that are passed inside the brackets while calling the function
#example of position arguments-> (a,b,c) while calling a function
#example of key word arguments-> (a=1,b=2,c=3) while calling a function
#we cannot use a positional argument after a keyword argument for eg-> (1,b=2,3)
#default arguments/parameters for eg -> def nums(a,b,c,d=4)
#to pass a parameter as a dictionary just put ** before the parameter

def name(**name):#parameters are taken as a dictionary,here "name " is considered a dictionary
    print(type(name))
    print("hello",name["fname"],name["mname"],name["lname"])

name(fname="harsh",mname="singh",lname="ruhil")


# *args parameter is used to give any number of arguments in the function
def funargs(*args,**kwargs):

    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,value)

har=["harsh","elon","steve"]
kw={"rohan":"monitor","harry":"fitness instructor","programmer":"coordinator"}
funargs(*har,**kw)#while using *args as a parameter we have to use * before the argument as well while calling the function
                  # same goes for kwargs as well,kwargs is used for a dictionary

