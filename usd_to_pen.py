# !pip install yfinance
import yfinance as yf
import numpy as np


''' Conversor de moneda '''
''' Código creado para ser corrido en la terminal '''


usd  = yf.Ticker('PEN=X').history(period='1d')
last = usd.tail(1)

# Última cotización
date  = last.index.strftime('%d-%m-%Y').astype(str)[0]
price = last['Close'].astype(float)[0]


# Interfaz
print(' ')
print('Hola! ¿Qué conversión deseas realizar?')
print(f'--- Cotización: S/ {np.round(price, 3)} por 1 US$ ---')
print(f'--- Actualizado en Yahoo Finance al {date} ---')
print('1: Dólares a Soles, o 2: Soles a Dólares')
given = input('... ')
print(' ')


while True:
    
    try: 
        if int(given) == 1:
            print('¿Cuántos dólares deseas convertir?')
            try:
                usd_given = float(input('... US$ ')) 
                pen_conv  = price * usd_given
                
                print(' ')
                print(f'US$ {usd_given} equivale a S/ {np.round(pen_conv, 3)}')
                print(' ')
            except:
                print('Ups! Quizás tipeaste mal la operación.')
                
        elif int(given) == 2:
            print('¿Cuántos soles deseas convertir?')
            try:
                pen_given = float(input('... S/ ')) 
                usd_conv  = pen_given/price
                
                print(' ')
                print(f'S/ {pen_given} equivale a US$ {np.round(usd_conv, 3)}')
                print(' ')
            except:
                print('Ups! Quizás tipeaste mal la operación.')
    
        print('¿Deseas continuar? [Y/N]')
        solution_given = str(input('... '))
        
        if solution_given == 'Y':
            continue
        else:
            break
    

    except:
        print('Ups! Quizás tipeaste mal la operación.')
        print('¿Deseas continuar? [Y/N]')
        solution_given = str(input('... '))
        
        if solution_given == 'Y':
            print('1: Dólares a Soles, o 2: Soles a Dólares')
            given = int(input('... '))
            continue
        else:
            break    
    

    