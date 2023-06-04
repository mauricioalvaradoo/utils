''' Sucesión de Fibonacci '''


class Fibonacci():
    def __init__(self, maxnumb):
        assert maxnumb >= 1, 'Por lo menos, el máximo número debe ser 1.'
        assert type(maxnumb) == int, 'Máximo número debe ser entero'

        self.maxnumb = maxnumb


    def get_fibonacci_sequence(self):
        sequence = {0: 0, 1: 1}
        
        for i in range(2, self.maxnumb + 1):
            sequence[i] = sequence[i-1] + sequence[i-2]

        return sequence
    

# testing
seq = Fibonacci(maxnumb=20)
seq = seq.get_fibonacci_sequence()
seq