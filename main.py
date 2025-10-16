tarefas = []

while True:
    print("\n--- Lista de Tarefas ---\n1. Adicionar tarefa.\n2. Ver tarefas.\n3. Remover tarefas.\n4. Marcar tarefa como concluida.\n5. Sair.\n")
    try:
        escolha = int(input("Escolha uma das opcoes acima: "))
    except:
        print("Entrada invalida, tente novamente...")
        continue
    if escolha == 1:
        descricao_tarefa = input("\nQual tarefa voce quer adicionar? ")
        nova_tarefa = {"descricao": descricao_tarefa, "status": "pendente"}
        tarefas.append(nova_tarefa)
        print("\nTarefa adicionada com sucesso!")
    elif escolha == 2:
        if len(tarefas) == 0:
            print("A lista de tarefas esta vazia.")
        else:
            for indice, tarefa in enumerate(tarefas):
                descricao = tarefa["descricao"]
                status = tarefa["status"]
                print(f"{indice+1}. [{status}] {descricao}")
    elif escolha == 5:
        print("Finalizando Programa...")
        break
    elif escolha == 3:
        for indice, tarefa in enumerate(tarefas):
            descricao = tarefa["descricao"]
            status = tarefa["status"]
            print(f"\n{indice+1}. [{status}] {descricao}.")
        try:
            tarefa_remover = int(input("\nEscolha a tarefa que voce quer remover: "))
            tarefas.pop(tarefa_remover-1)
            print("Tarefa removida com sucesso...")
        except:
            print("Entrada invalida, digite um numero...")
            continue
    elif escolha == 4:
        for indice, tarefa in enumerate(tarefas):
            descricao = tarefa["descricao"]
            status = tarefa["status"]
            print(f"\n{indice+1}. [{status}] {descricao}.")
        try:
            tarefa_concluida = int(input("Qual tarefa voce quer marcar como concluida? "))
            indice_alvo = tarefa_concluida - 1
            tarefas[indice_alvo]["status"] = 'concluida'
            print("\nTarefa marcada como concluida com sucesso!")
        except:
            print("\nEntrada invalida, por favor, digite um numero da lista.")

    else:
        print("Opcao invalida, tente novamente...")

