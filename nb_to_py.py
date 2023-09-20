# pip install nbconvert
import nbformat
from nbconvert import PythonExporter


''' Transformar archivo 'ipynb' a py '''


# Definir 'ruta' de entrada para archivo 'ipynb' y salida del 'py'
file_nb = './Objetos/Notebook_Running Code.ipynb'
file_py = './Resultados/Notebook_Running Code.py'

# 
py_exporter = PythonExporter()
py_exporter.exclude_input_prompt  = True
py_exporter.exclude_output_prompt = True


# Transformación
with open(file_nb, 'r', encoding='utf-8') as f:
    nb_content = nbformat.read(f, as_version=4)

py_code, _ = py_exporter.from_notebook_node(nb_content)

with open(file_py, 'w', encoding='utf-8') as f:
    f.write(py_code)
