#importo a lista que armazena tudo
from database import usuarios

def cadastrar_usuario(): #perguntar ao usuário os dados
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    idade = input("Digite a idade: ")

    usuario = {"nome": nome, "email": email, "idade": idade} #juntar os dados
    usuarios.append(usuario) #adiciono a lista usuários
    print("\nUsuário cadastrado com sucesso!\n") #mensagem de sucesso.