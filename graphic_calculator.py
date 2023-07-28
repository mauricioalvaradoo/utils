import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np

''' Gráfico de una función solicitada '''


fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

x = np.arange(-5.0, 5.0, 0.001)
l, = ax.plot(x, np.zeros_like(x), lw=2)

def submit(expression):
    ''' Actualizar función
    Definir función mediante la variable 'x'

    '''
    ydata = eval(expression)
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()


y = str(input('Función solicitada: '))

axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, 'Función: ', textalignment='center')
text_box.on_submit(submit)
text_box.set_val(y)

plt.show()