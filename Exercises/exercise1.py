import math

class log:
    def func (x):
        return math.log(x)






learning_rate = 0.5
x_1 = -5
x_2 = -5

def f (x_a, x_b):
    


    y1 = mult(x_a, x_a)
    y2 = mult(x_b,x_b)
    y3 = mult(2,y2)
    y4 = mult(x_a,x_b)
    y5 = mult(2,y4)
    y6 = mult(2,x_b)
    y7 = add(y1,y3)
    y8 = add(y7, -y5)
    y9 = add(y8, -y6)
    y10 = add(y9,2)
    y11 = log(y10)
    
    # derr/derr = 1

    # derr/y11
    derr11 =    
    
    
    
    
    return y11

def der_f (err):
    der11 = (1/y10)*(der10/der_y9)

def log (x):
    return math.log(x)

def der_log (x, ):
    return 

def sq (x):
    return x * x

def mult (x_a, x_b):
    return x_a*x_b

def add (x_a, x_b):
    return x_a + x_b






print(f(x_1, x_2))


