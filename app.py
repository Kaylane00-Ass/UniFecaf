#codigo de exemplo para o estudo de caso e portifolio. (MENU)
opcao = ''
while opcao != '0':
    print ("1- nome do aluno")
    print ("2- nota do aluno")
    print ("3- situacao do aluno")
    print ("0- sair")
    opcao = input ("digite uma opcao:")
    if opcao == "1":
        print (input("digite o nome do aluno:"))
        input ("digite enter para continuar...")
        elif opcao == "2" :
        print (in(input("digite a nota do aluno:")))
        input ("digite enter para continuar...")
    elif opcao == "3":
        print ("aprovado!")
        input ("digite enter para continuar...")
        elif opcao == "0":
            print ("saindo do sistema...")
    else: 
        print("Opcao invalida, digite novamente")