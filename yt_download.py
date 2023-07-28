# !pip install pytube
from pytube import YouTube

''' Descargar video de Youtube con la mayor resolución posible'''


# Definir 'url' de video y 'ruta' de descarga
url = 'https://www.youtube.com/watch?v=OPf0YbXqDm0'
path = './Descargas/'

video = YouTube(url)
video.streams.get_highest_resolution().download(path)
