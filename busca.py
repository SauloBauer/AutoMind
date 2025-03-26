#importo a lista que armazena tudo
from database import usuarios

def buscar_usuario(): #nome que deseja buscar
    nome_procurado = input("Digite o nome do usuário que deseja buscar: ")

    for usuario in usuarios: #Entra na lista
        if usuario["nome"].lower() == nome_procurado.lower(): #Coloca todos os caracteres em minúsculo e procura o nome digitado
            print(f"\nUsuário encontrado:") #feedback
            print(f"Nome: {usuario['nome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}\n") #pega da lista e mostra
            return

    print("\nUsuário não encontrado.\n") #caso nao encontre, da um feedback