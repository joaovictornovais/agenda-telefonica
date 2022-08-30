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

while True:
    print('='*30)
    print('[1] Inserir novo contato\n'
          '[2] Inserir dois ou mais contatos\n'
          '[3] Consultar contato\n'
          '[4] Modificar contato\n'
          '[5] Remover contato\n'
          '[6] Fechar agenda')
    print('='*30)
    opcao = input('Digite a opção desejada: ')
    if opcao == '6':
        print('Fechando agenda...')
        sleep(1)
        break

    elif opcao == '1':
        novoContato()
        print('Contato cadastrado com sucesso!')
    elif opcao == '2':
        novosContatos()
    elif opcao == '3':
        consultarContato()
    elif opcao == '3':
        modificarContato()
    elif opcao == '4':
        removerContato()
    else:
        print('ERRO: Opção inválida.')

print('Agenda fechada.')