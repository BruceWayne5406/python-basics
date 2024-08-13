#strings are ordered,immutable,text representations
mystring="   hello world   "
print(mystring)
my_string=mystring.strip()#.strip function cuts the spaces that i have provided in the string
print(my_string)

print(mystring.startswith("hello"))#returns a boolean value telling if the string starts with "hello" or not

print(my_string.find("o"))#gives the index of the character you searched for in the string
print(my_string.count("o"))#counts the number of times a character occurs

print(mystring.replace("world","india"))

string2="how are you doing"
print(string2.split(","))#arranges the words in string in a list
nstring="!".join(string2)#to join the elements of a list back into a string,whatever we put between the braces gets joined in between the characters
print(nstring)


#formatting strings
var="tom"
s1="the variable is %s" % var# %s indicates a reserved place for a string and "% var" indicates that the reserved place is taken
#by var
print(s1)

#the same thing can be done for numbers as well by using "%d" and for floating points we have "%f"
var1=5
s2="the new string is %d" % var1
print(s2)


# formatting the string using %s,d,f is an old method.the same thing nowadays is done in a different format:

var2="harsh"
s4="the name is {}".format(var2)#here the braces act as the placeholder
print(s4)

var3=3.142
var6=2.0011
s5="pi is approx {:.2f} and {}".format(var3,var6)# :.2f suggests that you only want 2 digits after decimal for var3
print(s5)


#however the latest way of formatting strings is using f-strings because they have the least run time and are more efficient
var7=5.666
var8=8.0055
s7=f"the var is {var7} and {var8}"
print(s7)