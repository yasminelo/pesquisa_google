'''
Programa que pesquisa seus dados automaticamente no Google
'''

import webbrowser
print("Esse programa visa fazer uma apuração a fim de indentificar seus dados em sites disponíveis no Google.")
pergunta = input('Insira o dado que você deseja verificar: ')

pesquisar = ('https://www.google.com/search?q=')
pesquisaok = (pesquisar + pergunta)

webbrowser.open(pesquisaok)
