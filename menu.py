#Aqui eu importo todas as funções
from cadastro import cadastrar_usuario
from listagem import listar_usuarios
from busca import buscar_usuario

#função do Menu
def menu():
    while True: #Enquanto o usuário digitar o número correto...
        print("1 -> Cadastrar Usuário")
        print("2 -> Listar Usuários")
        print("3 -> Buscar Usuário")
        print("4 -> Sair")

        opcao = input("\nEscolha uma opção: ")

        #Envio o usuário para função desejada
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            print("\nSaindo da aplicação.\n")
            break
        else: #Se o usúario não executar o código correto
            print("\nOpção inválida! Tente Novamente.\n")

#Executar a Função menu
menu()