''' Estimación del Mínimo Común Múltiplo (MCM) '''


class MCM():
    def __init__(self, numb1, numb2):
        assert numb1 > 0, 'El primer número debe ser mayor a cero'
        assert numb2 > 0, 'El segundo número debe ser mayor a cero'
        assert type(numb1) == int, 'El primer número debe ser entero'
        assert type(numb2) == int, 'El segundo número debe ser entero'
        
        self.numb1 = numb1
        self.numb2 = numb2

        self.comun = max(self.numb1, self.numb2)
        mcm = None

        while True:
            if self.comun % self.numb1 == 0 and self.comun % self.numb2 == 0:
                mcm = self.comun
                break
            self.comun += 1

        return print(mcm)


# testing
num1 = 10
num2 = 15

mcm = MCM(num1, num2)