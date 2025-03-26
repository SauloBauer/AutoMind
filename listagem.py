#importo a lista que armazena tudo
from database import usuarios

def listar_usuarios():
    if not usuarios: #se não tiver nada cadastrado
        print("\nNenhum usuário cadastrado.\n") #feedback
        return

    print("\nLista de Usuários:")
    for i, usuario in enumerate(usuarios, 1): #seleciona 1 usuário
        print(f"{i}. Nome: {usuario['nome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}")#mostra o usuário, informação completa
    print()