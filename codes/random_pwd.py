import random
import string


''' Generador de contraseñas seguras '''
''' Combina caracteres y números '''

# Declaración
longitud = 25

# Creación de contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation
pwd = ''.join(random.choice(caracteres) for i in range(longitud))

print(f'Contraseña: {pwd}')