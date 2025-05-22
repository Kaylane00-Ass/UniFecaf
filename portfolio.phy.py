#gerenciamento de sistema para eventos universitarios 
#usando o conceito do while e if.
from types import NoneType

# from teste import mostrar_eventos

banco_dados = [ ]
opcao = " "
novo_evento = " "
mostrar_evento = 0 #variavel de controle para loop 
atualizar_evento = 0 
evento_cadastrados = 0 
evento_atualizado = 0

def mostrar_evento():
    contador = 1
    for item in banco_dados:
        print(f'{contador} - {item}')
        contador += 1 
#quando chamar essa funçao ela vai contar e listar os eventos.
while True:
    print('Bem-vindo ao sistema de gerenciamento de eventos universitarios!')
    print('---> Menu <---')
    print('1 - meu perfil') #vizualização de eventos cadastrados pela pessoa.
    print('2 - eventos') #vizualizar a lista dos eventos disponiveis cadastrados.
    print('3 - cadastrar') #cadastrar os eventos.
    print('4 - atualizacao ')  #atualizar os eventos cadastrados.
    print('5 - inscriçoes') #parte para a pessoa se inscrever e salvar no  "meu perfil".
    print('6 - exclusao_eventos') #excluir o evento da lista e possiveis inscricoes.
    print('0 - sair ') #sair do sistema.
    opcao = input("digite a sua opção:")
    if opcao == '1': #vizualização de eventos cadastrados pela pessoa.
        print('meus eventos:')
        banco_dados()
    elif opcao == '2': #vizualizar a lista dos eventos disponiveis cadastrados.
        print('eventos disponiveis:')
        mostrar_evento()
        evento_cadastrados_lista = [
            {'nome': 'Teck Week', 'data': '12/01/2023', 'hora': '10:00', 'descricao': 'evento de Nano-tecnologia para programadores entrar no mercado de trabalho.', 'vagas_disponiveis': 100},
            {'nome': 'Palestra 23', 'data': '02/11/2021', 'hora': '11:00', 'descricao': 'Palestra de como se introduzir na programação de video-games.', 'vagas_disponiveis': 150},
            {'nome': 'Cinema', 'data': '03/03/2025', 'hora': '13:00', 'descricao': 'como programadores podem trabalhar com a cinematrografia.', 'vagas_disponiveis': 175}
        ]
        for evento in evento_cadastrados_lista:
            print(f"Nome: {evento['nome']}")
            print(f"Data: {evento['data']}")
            print(f"Hora: {evento['hora']}")
            print(f"Descrição: {evento['descricao']}")
            print(f"Vagas disponíveis: {evento['vagas_disponiveis']}")
            print('------------------------')

    elif(opcao == '3'):#cadastrar os eventos
     mostrar_evento()
     nome = input('Digite o nome do evento: ')
     data = input('Digite a data do evento-mm/dd/aaaa: ')
     hora = input('Digite a hora do evento: ')
     descricao = input('Digite a descricao do evento: ')
     vagas_disponiveis = int(input('Digite a quantidade de vagas disponiveis: '))
     evento = [
           { 'nome': nome,
            'data': data,
            'hora': hora,
            'descricao': descricao,
            'vagas_disponiveis': vagas_disponiveis }
     ]
     for evento in evento:
            print(f"Nome: {evento['nome']}")
            print(f"Data: {evento['data']}")
            print(f"Hora: {evento['hora']}")
            print(f"Descrição: {evento['descricao']}")
            print(f"Vagas disponíveis: {evento['vagas_disponiveis']}")
            print('------------------------')
            evento_cadastrados = 1
     banco_dados.append(evento) #append e adicionar/anexar serve para criar 
     print('Evento cadastrado com sucesso!')
     print('deseja cadastrar outro evento?')
     resposta = input(' digite sim ou nao:')
     if resposta == 'sim':
             print('cadastrar outro evento')
             for cont in range(1):
                nome = input('Digite o nome do evento: ')
                data = input('Digite a data do evento-mm/dd/aaaa: ')
                hora = input('Digite a hora do evento: ')
                descricao = input('Digite a descricao do evento: ')
                vagas_disponiveis = int(input('Digite a quantidade de vagas disponiveis: '))
                evento = {
                    'nome': nome,
                    'data': data,
                    'hora': hora,
                    'descricao': descricao,
                    'vagas_disponiveis': vagas_disponiveis
                }
                banco_dados.append(evento)
                print('evento cadastrado com sucesso!')
             else:
                 print('Não ha eventos disponiveis no momento.') #se nao houver cadastro de eventos.

    if opcao =='4':#Atualizar os eventos cadastrados.
        def atualizar_evento():
          mostrar_evento()
    try:
        indice = int(input("Digite o número do evento que deseja atualizar: ")) - 1
        if 0 <= indice < len(banco_dados):
            evento = banco_dados[indice]
            print(f"Editando evento: {evento['nome']}")
            novo_nome = input('Novo nome (Enter para manter): ')
            nova_data = input('Nova data (Enter para manter): ')
            nova_descricao = input('Nova descrição (Enter para manter): ')

            if novo_nome:
                evento['nome'] = novo_nome
            if nova_data:
                evento['data'] = nova_data
            if nova_descricao:
                evento['descricao'] = nova_descricao

            print("Evento atualizado com sucesso!")
        else:
            print("Evento não encontrado.")
    except ValueError:
        print("Entrada inválida.")    

    if opcao == '5':  #inscriçoes
      def inscrever_em_evento():
         mostrar_evento()
    try:
        indice = int(input("Digite o número do evento que deseja se inscrever: ")) - 1
        if 0 <= indice < len(banco_dados):
            evento = banco_dados[indice]
            if evento["vagas_disponiveis"] > 0:
                evento["vagas_disponiveis"] -= 1
                print(f"Inscrição realizada com sucesso no evento: {evento['nome']}")
            else:
                print("Não há vagas disponíveis.")
        else:
            print("Evento não encontrado.")
    except ValueError:
        print("Entrada inválida.")   

    if opcao == '6': #exclusao_eventos
        mostrar_evento()
        numero_evento = int(input('digite o numero do evento que deseja excluir:'))
        del banco_dados[numero_evento - 1 ]
        print('evento excluido com sucesso!')   
        print('deseja excluir outro evento?')   
        resposta = input('digite sim ou nao:')
        if resposta == 'sim':
            print('excluir outro evento')
            for cont in range(1):
                mostrar_evento()
                numero_evento = int(input('digite o numero do evento que deseja excluir:'))
                del banco_dados[numero_evento - 1 ]
                print('evento excluido com sucesso!')
        else:
            print('Não ha eventos disponiveis no momento.')

    if opcao == '0':
        print('saindo do sistema...')
        break

