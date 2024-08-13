#if conditional statements are used to execute a particular piece of code under a particular condition
#assigning boolean values to "ismale" and "istall" variables
#note: boolean values are "True" and "False"

ismale=True
istall=True

def usecase():#creating a function
    if ismale and istall:#if this is true , then the following code gets executed
        print("you are male and tall")
    
    if ismale and not(istall):#if this is true , then the following code gets executed
        print("you are male but not tall")

    if not(ismale) and istall:#if this is true , then the following code gets executed
        print("you are not male but tall")

    elif not(ismale) and not(istall):#if this is true , then the following code gets executed
        
        print("you neither a male and nor tall")
    
usecase()#calling the function
