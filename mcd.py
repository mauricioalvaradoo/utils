''' Estimación del Máximo Común Divisor (MCD) '''


class MCD():
    def __init__(self, numb1, numb2):
        assert numb1 > 0, 'El primer número debe ser mayor a cero'
        assert numb2 > 0, 'El segundo número debe ser mayor a cero'
        assert type(numb1) == int, 'El primer número debe ser entero'
        assert type(numb2) == int, 'El segundo número debe ser entero'
        
        self.numb1 = numb1
        self.numb2 = numb2
    
        while self.numb2 != 0:
            self.numb1, self.numb2 = self.numb2, self.numb1 % self.numb2
        
        return print(self.numb1)


# testing
num1 = 44
num2 = 22

mcd = MCD(num1, num2)