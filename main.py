print("Iniciando sistema...")
def add_lista(numeros):
    numero = int(input("Digite o numero que deseja adicionar:"))
    if numero in numeros:
        print("Este numero ja esta na lista!!!")
    else:
     numeros.append(numero)
def ver_lista(numeros):
    if len(numeros) ==0:
        print("Nenhum Item Adicionado ainda!")
    else:
        for numero in numeros:
            print(numero)
def soma_lista(numeros):
    soma=0
    for numero in numeros:
        soma = soma + numero
    return soma
def maior_lista(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior
def menor_lista(numeros):
    menor=numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor
def media_lista(numeros):
     media = soma_lista(numeros) / len(numeros)
     return media 
def quantidade_lista(numeros):
    return (len(numeros))
def remover_lista(numeros):
    numero = int(input("Digite o numero para remove-lo:"))
    if numero in numeros:
        numeros.remove(numero)
    else:
         print("Numero desejado não foi encontrado")
def buscar_lista(numeros):
    numero = int(input("Digite o numero que deseja buscar:"))
    if numero in numeros:
        posicao = numeros.index(numero)
        print("Numero encontrado na posição", posicao)
        print("Numero Encontrado!")
    else:
        print("Numero não encontrado")
def ordenar_lista(numeros):
    if len(numeros) ==0:
        print("Lista Vazia!")
        return
    print("1 - Ordem crescente:")
    print("2 - Ordem decrescente:")
    print("0 - Sair...")
    escolha = int(input("Escolha a opção desejada:"))
    if escolha ==1:
        ordenado = sorted(numeros)
        print(ordenado)
    elif escolha ==2:
        ordenado = sorted(numeros, reverse = True)
        print(ordenado)
    elif escolha ==0:
        print("saindo...")
    else:
        print("opção invalida!")
def limpar_lista(numeros):
         
         if len(numeros) ==0:
             print("Lista Vazia!")
             return
         resposta = (input("Deseja Limpar a lista? S ou N?"))
         resposta = resposta.lower()
         if resposta =="s":
             numeros.clear()
             print("Lista Limpa!")
         else:
             print("Ação cancelada!")
numeros=[]
opcao=999
while opcao !=0:
    print("1 - Adicionar Numero a lista:")
    print("2 - Ver lista:")
    print("3 - Ver dados:")
    print("4 - Quantidade:")
    print("5 - Remover Numero:")
    print("6 - Buscar numero:")
    print("7 - Ordenar lista:")
    print("8 - Limpar lista:")
    print("0 - Sair...")
    
    opcao=int(input())
    if opcao ==1:
        add_lista(numeros)
    elif opcao ==2:
        ver_lista(numeros)
    elif opcao ==3:
        if len(numeros) ==0:
            print("Nenhum dado salvo no momento!")
        else:
         resultado_soma =soma_lista(numeros)
         resultado_maior = maior_lista(numeros)
         resultado_menor= menor_lista(numeros)
         resultado_media= media_lista(numeros) 
         print("------Dados ------")
         print("Soma:", resultado_soma)
         print("Maior:", resultado_maior)
         print("Menor:", resultado_menor)
         print("Media:", resultado_media)
         print("-------------------")
    elif opcao ==4:
        resultado_quantidade = quantidade_lista(numeros)
        print("Quantidade:", resultado_quantidade)
    elif opcao ==5:
        remover_lista(numeros)
    elif opcao ==6:
        buscar_lista(numeros)
    elif opcao ==7:
        ordenar_lista(numeros)
    elif opcao ==8:
        limpar_lista(numeros)