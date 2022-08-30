from time import sleep
agenda = {}


def novoContato():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('E-mail: ')
    twitter = input('Twitter: ')
    instagram = input('Instagram: ')
    agenda[nome] = {'Telefone': telefone, 'Email': email, 'Twitter': twitter, 'Instagram': instagram}


def novosContatos():
    qtd = int(input('Quantos contatos você deseja adicionar? '))
    for i in range(qtd):
        novoContato()
        print(f'Contato {i+1} cadastrado com sucesso')

def consultarContato():
    try:
        nomeConsulta = input('Digite o nome do contato que deseja consultar: ')
        print(f'Dados do {nomeConsulta}')
        for k, v in agenda[nomeConsulta].items():
            print(f'{k}: {v}')
    except:
        print('ERRO: Não foi encontrado nenhum contato em sua agenda com esse nome.')


def modificarContato():
    try:
        nomeModificar = input('Digite o nome do contato que deseja modificar: ')
        opcao = input('[1] Nome\n[2] Telefone\n[3] E-mail\n[4] Twitter\n[5] Instagram\nDigite a opção correspondente ao item que deseja alterar: ')
        if opcao == '1':
            novoNome = input('Digite o novo nome: ')
            agenda[novoNome] = agenda.pop(nomeModificar)
            print('Nome alterado com sucesso!')
        elif opcao == '2':
            novoTelefone = input('Digite o novo telefone: ')
            agenda[nomeModificar]['Telefone'] = novoTelefone
            print('Telefone alterado com sucesso!')
        elif opcao == '3':
            novoEmail = input('Digite o novo email: ')
            agenda[nomeModificar]['Email'] = novoEmail
            print('E-mail alterado com sucesso!')
        elif opcao == '4':
            novoTwitter = input('Digite o novo twitter: ')
            agenda[nomeModificar]['Twitter'] = novoTwitter
            print('Twitter alterado com sucesso!')
        elif opcao == '5':
            novoInstagram = input('Digite o novo instagram: ')
            agenda[nomeModificar]['Instagram'] = novoInstagram
            print('Instagram alterado com sucesso!')
        else:
            print('ERRO: Opção inválida.')
    except:
        print('ERRO: Não foi encontrado nenhum contato em sua agenda com esse nome.')


def removerContato():
    try:
        nomeRemover = input('Digite o nome do contato que deseja remover: ')
        confirmacao = input(f'Você tem certeza que deseja remover {nomeRemover} de sua agenda? (S/N): ')
        if confirmacao in 'Ss':
            del agenda[nomeRemover]
            print('Contato removido com sucesso!')
        elif confirmacao in 'Nn':
            print('Operação cancelada.')
        else:
            print('ERRO: Opção inválida.')
    except:
        print('ERRO: Não foi encontrado nenhum contato em sua agenda com esse nome.')


def relatorioAgenda():
    contador = 0
    print(f'{"Nro":<4}{"Nome":<20}{"E-mail":<32}{"Telefone":<20}{"Twitter":<20}{"Instagram"}')
    for i in agenda.keys():
        contador += 1
        print(
            f'{contador:<4}{i:<20}{agenda[i]["Email"]:<32}{agenda[i]["Telefone"]:<20}{agenda[i]["Twitter"]:<20}{agenda[i]["Instagram"]}')
while True:
    print('='*30)
    print('[1] Inserir novo contato\n'
          '[2] Inserir dois ou mais contatos\n'
          '[3] Relatório da agenda\n'
          '[4] Consultar contato\n'
          '[5] Modificar contato\n'
          '[6] Remover contato\n'
          '[7] Fechar agenda')
    print('='*30)
    opcao = input('Digite a opção desejada: ')
    if opcao == '7':
        print('Fechando agenda...')
        sleep(1)
        break

    elif opcao == '1':
        novoContato()
        print('Contato cadastrado com sucesso!')
    elif opcao == '2':
        novosContatos()
    elif opcao == '3':
        relatorioAgenda()
    elif opcao == '4':
        consultarContato()
    elif opcao == '5':
        modificarContato()
    elif opcao == '6':
        removerContato()
    else:
        print('ERRO: Opção inválida.')

print('Agenda fechada.')