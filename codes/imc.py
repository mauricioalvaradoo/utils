import numpy as np

''' Estimar el IMC '''
''' 
El IMC es una métrica de peso corporal en relación a la altura de una persona.
Los rangos de referencia son las siguientes:
- Bajo peso: IMC < 18.5
- Peso normal: 18.5 <= IMC < 24.9
- Sobrepeso: 24.9 <= IMC < 29.9
- Obesidad: IMC >= 30
'''

class IMC():
    ''' El peso debe estar medido en kg, y la altura en metros. '''

    def __init__(self, peso, altura):
        assert peso > 0, 'Por lo menos debes colocar un peso mayor a 0.'
        assert altura > 0, 'Por lo menos debes colocar una altura mayor a 0.'
        
        self.peso = peso
        self.altura = altura


    def get_imc(self):
        imc = self.peso / (self.altura * self.altura)
        
        if imc < 18.5:
            print(f'Tu IMC es {np.round(imc, 1)}, lo cual te categoriza en bajo peso.')
        elif imc >= 18.5 and imc < 24.9:
            print(f'Tu IMC es {np.round(imc, 1)}, lo cual te categoriza en peso normal.')
        elif imc >= 24.9 and imc < 29.9:
            print(f'Tu IMC es {np.round(imc, 1)}, lo cual te categoriza en sobrepeso.')
        else:
            print(f'Tu IMC es {np.round(imc, 1)}, lo cual te categoriza en obesidad.')


# testing
imc = IMC(peso=70, altura=1.7)
imc.get_imc()