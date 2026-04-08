produtos=[]
def buscar_produto(produtos):
    busca=input("Digite o produto para busca-lo:").lower()
    achado = "nao"
    for produto in produtos:
        if busca == produto["nome"]:
            posicao = produtos.index(produto) +1
            achado = "sim"
    if achado =="sim":
        print("produto encontrado na posição:", posicao, "da lista!")
    else:
        if achado =="nao":
            print("produto não encontrado")
def adicionar_produto(produtos):
    busca=input("Digite o produto para adiciona-lo:").lower()
    preco=float(input("Digite o valor do produto:"))
    for produto in produtos:
        if busca == produto["nome"]:
            print("Esse produto ja pertence a lista!")
            return   
    produtos.append({"nome": busca, "preco": preco})
    print("Produto adicionado!")
def ver_lista(produtos):
    soma = 0
    if len(produtos) ==0:
        print("Não ha produtos no seu carrinho!")
        return
    for produto in produtos:
        print("produto:", produto["nome"], "|", "preço:", produto["preco"])
        soma = soma + produto["preco"]
    print("Total:", soma)
def remover_produto(produtos):
    remover = input("Digite o produto que deseja remover:").lower()
    for produto in produtos:
        if remover == produto["nome"]:
            confirmacao = input("Deseja remover o produto s/n:").lower() 
            while confirmacao not in ["s", "n"]:
                confirmacao = input("Deseja remover o produto s/n:").lower() 
            if confirmacao == "s":
                produtos.remove(produto)
                print("Produto removido!")
                return
            elif confirmacao =="n":
                print("Ação cancelada!")
    print("Produto não encontrado!")
def editar_produto(produtos):
    busca = input("Digite o produto que deseja atualizar:").lower()
    for produto in produtos:
        if busca == produto["nome"]:
            novo=float(input("Digite o novo preço:"))
            produto["preco"] = novo
            print("Produto atualizado!")
            return
    print("Produto não encontrado!")
opcao =999
while opcao !=0:
    print("1 - Adicionar produto:")
    print("2 - Ver produtos:")
    print("3 - Buscar produto:")
    print("4 - Remover produto:")
    print("5 - Editar produto:")
    print("6 - Somar carrinho:")
    print("0 - Sair...")
    opcao =int(input())
    if opcao ==3:
        buscar_produto(produtos)
    elif opcao ==1:
        adicionar_produto(produtos)
    elif opcao ==2:
        ver_lista(produtos)
    elif opcao ==4:
        remover_produto(produtos)
    elif opcao ==5:
        editar_produto(produtos)
    elif opcao ==6:
        soma_carrinho(produtos)