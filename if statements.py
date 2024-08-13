ismale=True
istall=True

def usecase():
    if ismale and istall:
        print("you are male and tall")
    
    if ismale and not(istall):
        print("you are male but not tall")

    if not(ismale) and istall:
        print("you are not male but tall")

    elif not(ismale) and not(istall):
        
        print("you neither a male and nor tall")
    
usecase()