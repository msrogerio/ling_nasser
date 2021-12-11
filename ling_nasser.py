from datetime import datetime


var = {}
linhas = 0

def add_linhas(add=0):
    global linhas
    if add !=0:
        linhas += add
        return linhas
    linhas += 1
    return linhas


def armazena_memoria(chave, valor):
    var.update({chave: valor})

def help():
    print(
        '-h [--hel] - lista as funcoes da ;\n' +
        '-m [--mostra] - printa uma mensagem qualquer. Ex: -m "Hello Word" or --mostra "Hello Word";\n' +
        '-l [--limpa] - limpar a saída do console \n' + 
        '-i [--int] - declara variáveis inteiras \n' + 
        '\tEx.: -i x=10, y=20 or --int x=10\n' + 
        '-op [--operacao] - executa operacao atitimática simples entre dois números\n' +
        '\tEx.-op x-y or -op x + y\n' + 
        '-x [--exit] - sair do console\n'
    )
    add_linhas(8)

def mostra(retorno):
    linha = linhas
    retorno = retorno.split(None, 1)[1]
    if '"' in retorno:
        retorno = retorno.replace('"', '')
        print('<%d>..: %s ' % (add_linhas(), retorno))
    elif retorno in var:
        print('<%d>..: %s' % (add_linhas(), var[retorno]))
    elif not retorno in var:
        print('<%d>..:[Erro na linha %d] %s não definido' % (add_linhas(), linha, retorno))

def limpa():
    global var
    var = {}
    print('\n'*130)

def inteiro(opcao):
    linha = linhas
    opcao = opcao.split(None, 1)
    if isinstance(opcao, list):
        opcao = opcao[1].replace(' ', '')
    if isinstance(opcao, str):
        opcao = opcao.replace(' ', '')
    if ',' in opcao:
        opcao = opcao.split(',')
        for a in opcao:
            if not '=' in a:
                print('<%d>..:[Erro na linha %d] O operador "=" não foi informado' % (add_linhas(), linha))
                return False
            temp = a.split('=')
            if not temp[1].isdigit():
                print('<%d>..:[Erro na linha %d] Valor inteiro não informado' % (add_linhas(), linha))
                return False
            armazena_memoria(temp[0], int(temp[1]))
        return True
    else:
        if not '=' in opcao:
            print('<%d>..:[Erro na linha %d] O operador "=" não foi informado' % (add_linhas(), linha))
            return False
        temp = opcao.split('=')
        if not temp[1].isdigit():
            print('<%d>..:[Erro na linha %d] Valor inteiro não informado' % (add_linhas(), linha))
            return False
        armazena_memoria(temp[0], int(temp[1]))
        return True

def operacao(opcao):
    linha = linhas
    opcao = opcao.split(None, 1)
    opcao = opcao[1].replace(' ', '')
    if '+' in opcao:
        operacao = opcao.split('+')
        if not operacao[0] in var or not operacao[1] in var:
            print('<%d>..:[Erro na linha %d] Valor não encontrado' % (add_linhas(), linha))
            return False
        operacao = var[operacao[0]] + var[operacao[1]]
        print(operacao)
        return True
    if '-' in opcao:
        operacao = opcao.split('-')
        if not operacao[0] in var or not operacao[1] in var:
            print('<%d>..:[Erro na linha %d] Valor não encontrado' % (add_linhas(), linha))
            return False
        operacao = var[operacao[0]] - var[operacao[1]]
        print(operacao)
        return True

hoje = datetime.utcnow()
hoje = hoje.strftime('%d %m %Y, %H:%M:%S')

print('Nasserala 0.0.1 (main, %s' % hoje)

opcao = ''
saida = 1

print('-h ou --help para mais informações')
while(saida!=0):
    opcao = input('<%d>..: '%add_linhas())

    if '-h' in opcao or '--help' in opcao:
        help()
    
    elif '-m' in opcao or '--mostra' in opcao:
        mostra(opcao)
    
    elif '-l' in opcao or '--limpa' in opcao:
        limpa()

    elif '-i' in opcao or  '--int' in opcao:
        inteiro(opcao)

    elif '-op' in opcao or '--operacao' in opcao:
        operacao(opcao)
        
    elif '-x' in opcao or '--exit' in opcao:
        saida=0
    
    else:
        print('..:[Erro] %d Escolha uma opção válida.' % linhas)
        help()

print('Saindo do console...')    