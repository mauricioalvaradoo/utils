import numpy as np
import pandas as pd

''' Método numérico de Newton-Raphson '''


def newton_raphson(fx, dfx, x0, tolerance=0.1e-8):
    
    dif = abs(2 * tolerance)
    xi = x0
    
    # Store
    x_values  = [x0]
    fx_values = [fx(x0)]

    while dif >= tolerance:
        
        ''' x_n+1 = x_n + fx/f'x '''

        xnuevo = xi - fx(xi) / dfx(xi)
        dif = abs(xnuevo - xi)
        xi = xnuevo
        
        # Store
        x_values.append(xnuevo)
        fx_values.append(fx(xnuevo))

    # Stores
    df = pd.DataFrame({'x_i': x_values, 'fx': fx_values})
    
    return df


# testing


''' x^x = 100
    
    f(x)  = x^x - 100
    f'(x) = x^x * (1+ln(x))
'''

fx  = lambda x: x**x - 100 
dfx = lambda x: x**x * (1+np.log(x)) 


print(fx(3))
print(fx(4))
print(fx(3.5))

x0 = 3.5
print( newton_raphson(fx, dfx, x0) )

