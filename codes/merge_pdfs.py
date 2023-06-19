# !pip install PyPDF2
import PyPDF2
import os


''' Unión de PDFs '''


# Definición de PDFs
path = 'Resultados/'
archivos = [
    'Memoria-BCRP-2021-14-16.pdf',
    'Memoria-BCRP-2021-18-44.pdf',
    'Memoria-BCRP-2021-46-78.pdf',
    'Memoria-BCRP-2021-80-101.pdf',
    'Memoria-BCRP-2021-103-109.pdf',
    'Memoria-BCRP-2021-111-148.pdf'
]
out = 'Resultados/Memoria-BCRP-2021-full.pdf'


names = [os.path.join(path, f) for f in archivos if os.path.isfile(os.path.join(path, f))]

# Unión
with PyPDF2.PdfMerger() as fusionador:
    for n in names:
        fusionador.append(n)

    with open(out, 'wb') as f:
        fusionador.write(f)
        
        
