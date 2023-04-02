# !pip install moviepy
from moviepy.editor import VideoFileClip

''' Transformar archivo 'mp4' a 'mp3' '''


# Definir 'ruta' de entrada para archivo 'mp4' y salida del 'mp3'
file_mp4 = './Descargas/Mark Ronson - Uptown Funk (Official Video) ft Bruno Mars.mp4'
file_mp3 = './Resultados/Uptown_Funk.mp3'


video = VideoFileClip(file_mp4)
audio = video.audio
audio.write_audiofile(file_mp3)

video.close()
audio.close()