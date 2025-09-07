#=====================+Bibliotecas+=====================#
import os

#=====================+Função limpar terminal+=====================#
def limpar_terminal():

    if os.name == "nt":
        _ = os.system("cls")

#=====================+Função Adicionar Tarefas+=====================#
def add_tarefa(lista_tarefa, tarefa):
    lista_tarefa.append(tarefa)
    print("Tarefa Adicionada Com sucesso!")
    return lista_tarefa

#=====================+Função Listar tarefas+=====================#
def listar_tarefas():
    print("==============+Lilith's to-do+==============")
    n = 1
    for tarefa in lista_tarefa:
        print(f"{n} - {tarefa}")
        n += 1
    print("\n============================================")

#=====================+Função de deletar tarefas+=====================#
def deletar_tarefa(lista_tarefa, tarefa):
    lista_tarefa.pop(tarefa - 1)
    return lista_tarefa

#=====================+Função de exibição do menu+=====================#
def menu_principal():
    print("==============+Lilith's to-do+==============\n"
        "1 - Inserir nova tarefa\n"
        "2 - Listar tarefas\n"
        "3 - Deletar Tarefa\n"
        "4 - Sair\n"
        "============================================" 
    )

#=====================+Funções do menu e loop principal+=====================#
lista_tarefa = []
rodando = True

while rodando:
    limpar_terminal()
    menu_principal()
    opcao = input("Selecione uma opção: ")

    if opcao == '1':
        limpar_terminal()
        tarefa = input("Insira uma nova tarefa: ")
        lista_tarefa = add_tarefa(lista_tarefa, tarefa)
    elif opcao == '2':
        limpar_terminal()
        listar_tarefas()
        input("Pressione 'Enter' para voltar")
    elif opcao == '3':
        #nessa parte do loop verificamos se a opção que deseja deletar é
        #númerica e se elas está dentro do range(tamanho) da nossa lista
        limpar_terminal()
        tarefa = input("Insira o número da tarefa que deseja deletar: ")
        if not tarefa.isnumeric():
            input("Opção inválida. Pressione 'Enter' e Tente novamente.")
        elif int(tarefa) > len(lista_tarefa):
            input("Opção inválida. Pressione 'Enter' e Tente novamente.")
        elif int(tarefa) <= 0:
            input("Opção inválida. Pressione 'Enter' e Tente novamente.")
        else:
            deletar_tarefa(lista_tarefa, int(tarefa))
    elif opcao == '4':
        limpar_terminal()
        input("Obrigade por usar Lilith's To-do, pressione 'enter' para encerrar...")
        rodando = False
    else:
        limpar_terminal()
        input("Opção inválida. Pressione 'Enter' e Tente novamente.")