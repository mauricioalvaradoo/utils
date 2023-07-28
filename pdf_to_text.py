# !pip install pytesseract
# !pip install pdf2image
# Desacarga e instalar el Tesseract OCR de https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract
from pdf2image import convert_from_path


''' OCR scanner para transformar PDFs a texto '''


# Definir rutas de 'pdf' y del ejecutable del 'Tesseract OCR'
pdf = './Objetos/Memoria-BCRP-1922.pdf'
ruta_texto = './Resultados/texto_extraido.txt'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.PSM = 6


# Extracción de texto de cada una de las páginas
# Abrir intérprete de Python con 'Permisos de Administrador'
pages = convert_from_path(pdf)
with open(ruta_texto, 'w') as f:
    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        f.write(f'--- Página {i+1} ---\n{text}\n\n')
        print(f'Texto de la página {i+1} extraído y guardado en {ruta_texto}')