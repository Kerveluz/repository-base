"""Hello World Multi Language.

Dependendo da lingua configurada no ambiente o programa
exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR.UTF-8

Execucao:

    python3 hello.py
"""
__version__ = "0.0.1"
__author__ = "Kerveluz"
__license__ = "Unlicense"


#Este programa imprime Hello World

import os   

current_language = os.getenv("LANG", "en_US")[:5]

msg = 'Hello, World!'

if current_language == 'pt_BR':
    msg = 'Olá, Mundo!'

elif current_language == 'it_IT':
    msg = 'Salve, Mondo'

print(msg)

 
