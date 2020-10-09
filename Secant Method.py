## iv. using the Secant method ## x:- number of loyalty card holders

def f(x): 
    ## equation is 3x^2-9x-6
    f = 3*x**2 - 9*x - 6;  
    return f;  
  
def secant(x1, x2, E): 
    n = 0; xm = 0; x0 = 0; c = 0;  
    if (f(x1) * f(x2) < 0): 
        while True:  
              
            ## find intermediate value
            x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)));  
            ## check if x0
            c = f(x1) * f(x0);  
            ## update interval value
            x1 = x2;  
            x2 = x0;  
            ## update iteration
            n += 1;  
            ## break the loop (if x0 is the root of equation ) 
            
            if (c == 0):  
                break;  
            xm = ((x1 * f(x2) - x2 * f(x1)) / 
                            (f(x2) - f(x1))); 
              
            if(abs(xm - x0) < E): 
                break; 
          
        print("Root of the equation =", round(x0, 6));  
        print("Number of iterations = ", n);  
    else: 
        print("Can't find the root in this inteval");  

## given values  
x1 = 2;  
x2 = 4;  
E = 0.001;  
secant(x1, x2, E);  




