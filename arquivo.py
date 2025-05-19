#Codigo do estudo de caso
#Sistema para controle de estoque de produtos
opcao = " "
lista = []

def lista_estoque(param1):
    raise NotImplementedError

while opcao != '0':
    print ("1- produto")
    print ("2- cadastro")
    print ("3- estoque")
    print ("4- remover")
    print ("0- sair")
    opcao = input ("Escolha a sua opcao:")
    if opcao =='1':
        print(['maca', 'banana', 'laranja'])
        print(f"lista de produtos: {lista}")
    elif opcao =='2':
       for cont in range(3):
           produto = input("digite o nome do produto:")
           lista.append(produto)
       lista_adicional = input("digite um produto adicional:")
       lista.append(lista_adicional)    
       print(f"novos produtos: {lista}")
       
    elif opcao == '3':
      lista_estoque = (["45 maca = R$59,96", "35 banana = R$77,94", "35 laranja = R$44,75"])
      print(f"produtos em estoque: {lista_estoque}")
       
    elif opcao =='4': 
        produto = ["maca", "banana", "laranja"]
        produto_remover = input("digite o nome do produto que deseja remover:")
        if produto_remover in produto:
            produto.remove(produto_remover)
            print(f"produto {produto_remover} removido com sucesso")
        else:
            print(f"produto {produto_remover} não encontrado na lista")

    elif opcao == '0':
        print("Sistema encerrado")
    else:
        print("opção inválida, tente novamente")
           