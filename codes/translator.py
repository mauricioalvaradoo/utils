# !pip install googletrans==4.0.0-rc1
# Alternativa: pygoogletranslation
from googletrans import Translator, LANGUAGES
import pandas as pd


''' Traductor de texto '''


# Consulta de lenguajes
print(
      pd.DataFrame.from_dict(
          LANGUAGES, orient='index', columns=['Lenguaje']
      ).to_string(index=True)
)


# Declaración
texto     = str(input('¿Qué deseas traducir?:\n... '))
lang_from = 'es'
lang_to   = 'en'


# Traducción
translator = Translator()
traduccion = translator.translate(texto, src=lang_from, dest=lang_to)
    
  
print(f'\n\nTraducción:\n... {traduccion.text}')


