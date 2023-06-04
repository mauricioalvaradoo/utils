''' Criba de Eratóstenes '''
''' Encontrar números primos hasta el máximo número pedido '''

class Prime():
    def __init__(self, maxnumb):
       assert maxnumb>=2, 'El máximo debe ser por lo menos 2.'
       assert type(maxnumb) == int, 'El número debe ser entero.'

       self.maxnumb = maxnumb

    def get_prime_numbers(self):
        prime_numbs = []

        for n in range(2, self.maxnumb+1):
            for i in range(2, n):
                if (n % i) == 0: # No primo
                    break
            else: # primo
                prime_numbs.append(n)
        
        return prime_numbs
    

# testing
prime_numbers = Prime(maxnumb=1000)
prime_numbers = prime_numbers.get_prime_numbers()
prime_numbers