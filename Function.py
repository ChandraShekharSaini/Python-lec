

def myFun(x): 
    global y 
    y = 89
   
    print("I am Function",x)


myFun(12)    
print(y)