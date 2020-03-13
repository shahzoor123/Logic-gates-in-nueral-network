## Logic gates in neural network ##

## or gate ##
def sumoid (x1,x2,w1,w2,w3,b):
    z = x1*w1+x2*w2+b*w3
    import math
    a = 1/1+math.e**(-z)
    if a>=0.5:
        print("1")
    else:
        print("0")
sumoid(x1=0,x2=0,w1=0.1,w2=0.1,w3=0,b=-0.1)  





#and gate
def sigmoid (x1,x2,w1,w2,w3,b):
    z = x1*w1+x2*w2+b*w3
    import math
    y = 1/(1+math.e**(-z))
    if y>=0.5:
        print("1")
    else:
        print("0")
sigmoid(x1=1,x2=1,w1=0.1,w2=0.2,w3=1,b=-0.3)        
    


#And gate
def sigmoid (x1,x2,w1,w2,w3,b):
    z = x1*w1+x2*w2+b*w3
    import math
    y = 1/(1+math.e**(-z))
    if y>=0.5:
        print("1")
    else:
        print("0")
sigmoid(x1=0,x2=0,w1=0.1,w2=0.2,w3=1,b=-0.3)    



# Nand gate #
def sigmoid (x1,x2,w1,w2,w3,b):
    z = x1*w1+x2*w2+b*w3
    import math
    y = 1/(1+math.e**(-z))
    if y>=0.5:
        print("1")
    else:
        print("0")
sigmoid(x1=1,x2=0,w1=-0.1,w2=-0.1,w3=1,b=0.1)    


# Nor gate #
def sigmoid (x1,x2,w1,w2,w3,b):
    z = x1*w1+x2*w2+b*w3
    import math
    y = 1/(1+math.e**(-z))
    if y>=0.5:
        print("1")
    else:
        print("0")
sigmoid(x1=0,x2=0,w1=-0.1,w2=-0.1,w3=0,b=0.1)




## not ## 


def sigmoid (x1,w1,w3,b):
    z = x1*w1+b*w3
    import math
    y = 1/(1+math.e**(-z))
    if y>=0.5:
        print("1")
    else:
        print("0")
sigmoid(x1=1,w1=-0.1,w3=0,b=-0.1)




# XOR gate #
def nn(x1,x2,w1,w2,w3,w4,w5,w6,b1,b2,b3):
    ## input for h1 ##
    h1in = x1*w1+x2*w3+b1
    import math
    ## hidden layer 1##
    h1out =  1/(1+math.e**(-h1in))
    print(h1out)
    
    ## hidden layer 2##
    
    ## input for h1 ##
    h2in = x1*w2+x2*w4+b2
    h2out = 1/(1+math.e**(-h2in))
    print(h2out)
    yin = h1out*w5+h2out*w6+b3
    yout = 1/(1+math.e**(-yin))
    print(yout)
    if yout>=0.5:
        print("1")
    else:
        print("0")
nn(x1=1,x2=1,w1=20,w2=-20,w3=20,w4=-20,w5=20,w6=20,b1=-10,b2=30,b3=-30)        
    
    
    
    

## xnor gate ##
def nn(x1,x2,w1,w2,w3,w4,w5,w6,b1,b2,b3):
    ## input for h1 ##
    h1in = x1*w1+x2*w3+b1
    import math
    ## hidden layer 1##
    h1out =  1/(1+math.e**(-h1in))
    print(h1out)
    
    ## hidden layer 2##
    
    ## input for h1 ##
    h2in = x1*w2+x2*w4+b2
    h2out = 1/(1+math.e**(-h2in))
    print(h2out)
    yin = h1out*w5+h2out*w6+b3
    yout = 1/(1+math.e**(-yin))
    print(yout)
    if yout>=0.5:
        print("1")
    else:
        print("0")
nn( x1=1
   ,x2=0
   
   ,w1=20
   ,w3=20
   ,b1=-10
   
   ,w2=-20
   ,w4=-12
   ,b2=30
   
   
   ,w5=20
   ,w6=20
   ,b3=-30)        
    
    
    
    


    
