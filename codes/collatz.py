import matplotlib.pyplot as plt

''' Conjetura de Collatz '''
''' Dado un número, si es par se divide entre 2, y si es impar se multiplica por 3 y se suma uno '''
''' Tras varias iteraciones, se entrerá a un ciclo de 1-4-2 '''


class Collatz():

    ''' Definir número entre 1-100 '''
    def __init__(self, number, iters=1_000):
        assert type(number) == int, 'El número debe ser entero'
        assert number >= 1, 'El número debe ser por lo menos 1.'
        assert number <= 100, 'El número debe ser máximo 100.'
        assert type(iters) == int, 'El número de iteraciones debe ser entero'
        assert iters >= 200, 'Por lo menos debes seleccionar 200 iteraciones'

        self.number = number
        self.iters = iters

    def iteraciones(self):
        numbers = {}
        new_number = self.number

        for i in range(1, self.iters+1):
            numbers[i] = new_number
        
            if new_number % 2 == 0: # par
                new_number = new_number/2
            else: # impar
                new_number = new_number*3 + 1
        
        return numbers


# testing
conjetura = Collatz(number=57, iters=200)
conjetura.iteraciones()
conjetura

# figura de las simulaciones
iters  = list(conjetura.keys())
values = list(conjetura.values())
plt.plot(iters, values)
plt.xlabel('iters')
plt.ylabel('values')
plt.show()