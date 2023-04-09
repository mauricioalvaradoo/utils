# !pip install PyPDF2
import PyPDF2


''' División de PDFs '''


# Definición de PDFs y páginas
file       = 'Memoria-BCRP-2021'   # Nombre
input_pdf  = f'Objetos/{file}.pdf' # Ruta del PDF
start_page = 14
end_page   = 16
output_pdf = f'Resultados/{file}-{start_page}-{end_page}.pdf' # Ruta de salida


# Abriendo el pdf como binario
with open(input_pdf, 'rb') as f:

    pdf_reader = PyPDF2.PdfReader(f)
    pdf_writer = PyPDF2.PdfWriter()

    # Loop por página
    for page_num in range(start_page - 1, end_page):
       
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_file = f'{output_pdf}{str(page_num + 1)}.pdf'

    # Archivo con todas las páginas generadas
    with open(output_pdf, 'wb') as out_f:
        pdf_writer.write(out_f)
