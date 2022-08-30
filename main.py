from time import sleep
agenda = {}

def novoContato():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('E-mail: ')
    twitter = input('Twitter: ')
    instagram = input('Instagram: ')
    agenda[nome] = {'Telefone': telefone, 'Email': email, 'Twitter': twitter, 'Instagram': instagram}
    print('Contato cadastrado com sucesso!')

while True:
    print('='*30)
    print('[1] Inserir novo contato\n'
          '[2] Consultar contato\n'
          '[3] Alterar contato\n'
          '[4] Remover contato\n'
          '[5] Fechar agenda')
    print('='*30)
    opcao = input('Digite a opção desejada: ')
    if opcao == '5':
        print('Fechando agenda...')
        sleep(1)
        break

    elif opcao == '1':
        novoContato()
    elif opcao == '2':
        consultarContato()
    elif opcao == '3':
        alterarContato()
    elif opcao == '4':
        removerContato()
    else:
        print('ERRO: Opção inválida.')

print('Agenda fechada.')