print("Sistema iniciando...")
alunos=[]
opcao = 999
def add_lista(alunos):
    aluno=input("Digite o nome do aluno:").lower()
    nota = float(input("Digite a nota do aluno:"))
    for item in alunos:
     if item[0] == aluno:
        print("Aluno ja pertence ao sistema!")
    else:
        alunos.append([aluno, nota])
        print("Aluno registrado com Sucesso!")
def ver_lista(alunos):
    if len(alunos) ==0:
        print("Nenhum aluno cadastrado!")
    else:
       for item in alunos:
           print("Aluno:", item[0], "| Nota:", round(item[1], 1))
def buscar_lista(alunos):
    aluno =input("Qual aluno deseja buscar:").lower()
    for item in alunos:
        if item[0] == aluno:
            print("Aluno:", item[0])
            print("Nota:", item[1])
            return
    print("Aluno não encontrado!")
def remover_lista(alunos):
    aluno =input("Qual aluno deseja remover do sistema:").lower()
    for item in alunos:
        if item[0] == aluno:
            print("Aluno removido de sistema!")
            alunos.remove(item)
            return
        
    print("Aluno não encontrado!")
def quantidade_listas(alunos):
    quantidade = len(alunos)
    print("Numero de alunos cadastrados:", quantidade)
def soma_notas(alunos):
    soma =0
    for item in alunos:
         soma = soma + item[1]
    return soma
def media_notas(alunos):
    media =0
    if len(alunos) ==0:
        print("Nenhuma nota registrada!")
    else:  
        media = soma_notas(alunos) / len(alunos)
    return media
def atualizar_lista(alunos):
    aluno = input("Digite o aluno:").lower()
    for item in alunos:
        if item[0] == aluno:
            nova_nota= float(input("Digite a nova nota:"))
            item[1] = nova_nota
            print("Nota atualizada!")
            return 
    print("Aluno não cadastrado!")
def maior_nota(alunos):
    maior = alunos[0]
    for item in alunos:
     if item[1] > maior[1]:
        maior = item
    return maior
def menor_nota(alunos):
    menor=alunos[0]
    for item in alunos:
        if item[1] < menor[1]:
            menor = item
    return menor
                    
while opcao!=0:
    print("1 - Adicionar aluno:")
    print("2 - Ver lista de alunos:")
    print("3 - Buscar aluno:")
    print("4 - Remover aluno:")
    print("5 - Numero de alunos Cadastrados:")
    print("6 - Media da turma:")
    print("7 - Atualizar nota:")
    print("8 - Maior e menor nota:")
    print("0 - Sair...")
    opcao =int(input())

    if opcao ==1:
        add_lista(alunos)
    elif opcao==2:
        ver_lista(alunos)
    elif opcao ==3:
        buscar_lista(alunos)
    elif opcao ==4:
        remover_lista(alunos)
    elif opcao ==5:
        quantidade_listas(alunos)
    elif opcao ==6:
        resultado_media = media_notas(alunos)
        print("Media da tuma:", resultado_media)
    elif opcao ==7:
        atualizar_lista(alunos)
    elif opcao ==8:
        if len(alunos) ==0:
            print("Nenhuma nota registrada!")
        else:
         resultado_maior = maior_nota(alunos)
         resultado_menor = menor_nota(alunos)
         print("Maior nota:", resultado_maior[0], "-", resultado_maior[1])
         print("Menor nota:", resultado_menor[0], "-", resultado_menor[1])
