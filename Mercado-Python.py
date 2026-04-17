opcao=999
def add_prod(produtos):
    buscar=validar_nome()
    valor=validar_erro()
    produto={"nome": buscar, "preco": valor}
    for item in produtos:
        if buscar == item["nome"]:
            print("Este produto ja esta no seu carrinho!")
            return
    print("Produto Adicionado!")
    produtos.append(produto)
def ver_prod(produtos):
    soma =0
    if len(produtos) ==0:
            print("Carrinho vazio!")
            return
    for produto in produtos:
        soma = soma + produto["preco"]
        print("produto:", produto["nome"], "|", "preço:", produto["preco"])
    print("Valor:", soma)
def buscar_prod(produtos):
    buscar=input("Digite o produto que deseja buscar:").lower()
    for produto in produtos:
        if buscar == produto["nome"]:
            posicao = produtos.index(produto) +1
            print("Produto encontrado em seu carrinho")
            print("Na posição:", posicao)
            return
    print("Produto não encontrado!")
def remover_prod(produtos):
    busca=input("Digite o produto que deseja remover:").lower()
    for produto in produtos:
        if busca == produto["nome"]:
            confirmacao=input("Produto encontrado, deseja remover este produto? s/n:").lower()
            while confirmacao not in ["s", "n"]:
                confirmacao=input("Produto encontrado, deseja remover este produto? s/n:").lower()
            if confirmacao == "s":
                produtos.remove(produto)
                print("Produto removido!")
                return
            elif confirmacao =="n":
                print("Ação cancelada!")
                return
    print("Produto não encontrado!")
def editar_prod(produtos):
    buscar=input("Digite o produto que deseja editar:").lower()
    for produto in produtos:
        if buscar==produto["nome"]:
            print("Produto encontrado!")
            novo=validar_erro()
            produto["preco"] = novo
            print("Alteração feita com sucesso!")
            return
    print("Produto não encontrado!")
def salvar_produtos(produtos):
    with open ("produtos.txt", "w") as arquivo:
        for produto in produtos:
            nome = produto["nome"]
            preco = produto["preco"]
            arquivo.write(f"{nome},{preco}\n")
def carregar_produtos():
    produtos = []
    try:
        with open("produtos.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",")
                if len(partes) ==2:
                    nome, preco = partes
                    produto = {
                        "nome": nome,
                        "preco": float(preco)
                    }
                    produtos.append(produto)
                else:
                    print("Formato Invalido!")
    except FileNotFoundError:
        pass
    return produtos
produtos=carregar_produtos()
def validar_erro():
    while True:
        try:
            tentativa = float(input("Digite o preço do produto:"))
        except:
            print("Digite um número válido!")
            continue
        if tentativa <0:
            print("Digite um número válido!")
        else:
            return tentativa
def erro_menu(opcoes_validas):
    while True:
        try:
            tentativa=int(input("Digite a opção que deseja:"))
        except:
            print("Opção invalida!")
            continue
        if tentativa in opcoes_validas:
            return tentativa
        else:
            print("Opção invalida!")
def validar_nome():
    while True:
        buscar=input("Digite o produto que deseja adicionar:").lower()
        if buscar.strip() =="":
            print("Digite o Nome do produto:")
        else:
            return buscar
while opcao !=0:
    print("1 - Gerenciar produtos")
    print("0 - Sair...")
    opcao = erro_menu([0, 1])
    if opcao ==1:
        opcao2 =999
        while opcao2 !=0:
            print("1 - Adicionar produto:") 
            print("2 - Ver produtos:")
            print("3 - Buscar produto")
            print("4 - Remover produto:")
            print("5 - Editar produto:")
            print("0 - Voltar...")
            opcao2 = erro_menu([0, 1, 2, 3, 4, 5, ])
            if opcao2 ==1:
                add_prod(produtos)
                salvar_produtos(produtos)
            elif opcao2 ==2:
                ver_prod(produtos)
            elif opcao2 ==3:
                buscar_prod(produtos)
            elif opcao2==4:
                remover_prod(produtos)
                salvar_produtos(produtos)
            elif opcao2==5:
                editar_prod(produtos)
                salvar_produtos(produtos)