# !pip install moviepy
from moviepy.editor import VideoFileClip

''' Transformar archivo 'mp4' a gif '''


# Definir 'ruta' de entrada para archivo 'mp4' y salida del 'gif'
file_mp4 = './Descargas/NO GOD PLEASE NO!.mp4'
file_gif = './Resultados/NO GOD PLEASE NO!.gif'
fps = 20


video_clip = VideoFileClip(file_mp4)
video_clip = video_clip.set_fps(fps) # Default: 10
video_clip.write_gif(file_gif)


video_clip.close()