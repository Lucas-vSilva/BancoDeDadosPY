import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = ''

def menu():
    print('\nEscolha uma das opções abaixo:  \n\n' +
          '1. Cadastrar\n'                         +
          '2. Consultar\n'                         +
          '3. Atualizar Nome\n'                    +
          '4. Atualizar Telefone\n'                +
          '5. Atualizar Endereço\n'                +
          '6. Atualizar Data de Nascimento\n'      +
          '7. Deletar\n'                           +
          '0. Sair\n')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe o seu nome: ')
            nome = input()
            print('Informe o seu telefone: ')
            telefone = input()
            print('Informe o seu endereço: ')
            endereco = input()
            print('Informe o sua data de nascimento: ')
            dtNasc = input()
            #chamar o metodo inserir
            operacoes.inserir(nome, telefone, endereco, dtNasc)
        elif this.opcao == 2:
            #print('Informe o codigo que deseja consultar')
            #this.codigo = int(input())
            operacoes.consultar()
        elif this.opcao == 3:
            print('Informe o codigo que deseja atualizar')
            this.codigo = int(input())
            print('Informe o novo nome')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'nome', this.campo)
        elif this.opcao == 4:
            print('Informe o codigo que deseja atualizar')
            this.codigo = int(input())
            print('Informe o novo telefone')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'telefone', this.campo)
        elif this.opcao == 5:
            print('Informe o codigo que deseja atualizar')
            this.codigo = int(input())
            print('Informe o novo endereço')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'endereco', this.campo)
        elif this.opcao == 6:
            print('Informe o codigo que deseja atualizar')
            this.codigo = int(input())
            print('Informe a nova data')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'dataDeNascimento', operacoes.tratarData(this.campo))
        elif this.opcao == 7:
            print('Informe o codigo que deseja deletar')
            this.codigo = int(input())
            operacoes.excluir(this.codigo)
    else:
        print('Opção escolhida não é válida!')