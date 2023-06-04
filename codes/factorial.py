''' Estimación de factores '''
''' Estimación de una secuencia de factoriales '''


class Factorial():
    def __init__(self, maxnumb):
        assert maxnumb>=0, 'El número debe ser positivo.'

        self.maxnumb = maxnumb
        

    def get_factorial(self):
        
        if self.maxnumb == 0:
            return print(f'\nEl factorial de 0 es 0.')
        
        else:
            factorial = 1
            factorials = {1: 1}

            for i in range(1, self.maxnumb+1):
                factorial *= i
                factorials[i] = factorial

        return print(f'\nLa secuencia de factoriales es el siguiente:\n{factorials}.')


# testing
factorial = Factorial(maxnumb=10)
factorial = factorial.get_factorial()

