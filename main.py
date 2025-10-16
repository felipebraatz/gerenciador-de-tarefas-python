tarefas = []

while True:
    print("\n--- Lista de Tarefas ---\n1. Adicionar tarefa.\n2. Ver tarefas.\n3. Remover tarefas.\n4. Sair.\n")
    try:
        escolha = int(input("Escolha uma das opcoes acima: "))
    except:
        print("Entrada invalida, tente novamente...")
        continue
    if escolha == 1:
        nova_tarefa = input("\nQual tarefa voce quer adicionar? ")
        tarefas.append(nova_tarefa)
        print("\nTarefa adicionada com sucesso!")
    elif escolha == 2:
        if len(tarefas) == 0:
            print("A lista de tarefas esta vazia.")
        else:
            for indice, tarefa in enumerate(tarefas):
                print(f"\n{indice+1}. {tarefa}.")
    elif escolha == 4:
        print("Finalizando Programa...")
        break
    elif escolha == 3:
        for indice, tarefa in enumerate(tarefas):
            print(f"\n{indice+1}. {tarefa}.")
            try:
                tarefa_remover = int(input("\nEscolha a tarefa que voce quer remover: "))
                tarefas.pop(tarefa_remover-1)
                print("Tarefa removida com sucesso...")
            except:
                print("Entrada invalida, digite um numero...")
                continue
    else:
        print("Opcao invalida, tente novamente...")
