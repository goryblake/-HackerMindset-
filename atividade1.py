# Função para ler e exibir as 10 primeiras senhas do arquivo
def exibir_senhas():
    with open('SecLists/Passwords/darkweb2017-top100.txt', 'r') as arquivo:
        senhas = arquivo.readlines()
        for senha in senhas[:10]:
            print(senha.strip())

exibir_senhas()
