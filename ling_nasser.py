from datetime import datetime


var = {}
linhas = 0
contador_de_erros = 0
controle_erros = []

def add_erro(str):
    global contador_de_erros
    contador_de_erros += 1
    controle_erros.append(str)

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
        '\tEx.-op 1-2 or -op 1 + 2\n' + 
        '-a [--aceitacao] - verifica aceitação da expressaão\n' +
        '\tEx.-a x-y or -a x + y\n' + 
        '-x [--exit] - sair do console\n'
    )
    add_linhas(8)

def verifica_expressao(exp):
    """
    E = {q0, q1, q2}
    Σ = {t, +, -}
    t ∈ N
    δ:
        q0 <- t -> q1
        q0 <- + | - -> q2
        q1 <- t -> q2
        q1 <- - | + -> q0
        q2 <- - | + | t -> q2
    i = q0
    F = q0
    Γ = {x} 
    """
    exp = exp.split(None, 1)
    exp = exp[1].replace(' ', '')
    E = ['q0', 'q1', 'q2']
    i = E[0]
    F = E[1]
    e_atual = i
    for t in exp:
        if e_atual == E[0] and t.isdigit():
            e_atual = E[1]
        elif e_atual == E[0] and t=='+' or t=='-':
            e_atual = E[2]
        elif e_atual == E[1] and t.isdigit():
            e_atual = E[2]
        elif e_atual == E[1] and t=='+' or t=='-':
            e_atual = E[0]
        elif e_atual == E[2] and t=='+' or t=='-' or t.isdigit():
            e_atual = E[2]
    if e_atual == F:
        print('<%d>..: A expressão %s é aceita pelo autômato ' % (add_linhas(), exp))
        return True
    print('<%d>..: A expressão %s não é aceita pelo autômato ' % (add_linhas(), exp))
    return False

def mostra(retorno):
    linha = linhas
    retorno = retorno.split(None, 1)[1]
    if '"' in retorno:
        retorno = retorno.replace('"', '')
        print('<%d>..: %s ' % (add_linhas(), retorno))
        add_erro('[Erro linha %d]' % linha)
    elif retorno in var:
        print('<%d>..: %s' % (add_linhas(), var[retorno]))
        add_erro('[Erro linha %d]' % linha)
    elif not retorno in var:
        print('<%d>..:[Erro na linha %d] %s não definido' % (add_linhas(), linha, retorno))
        add_erro('[Erro linha %d]' % linha)

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
                add_erro('[Erro linha %d]' % linha)
                return False
            temp = a.split('=')
            if not temp[1].isdigit():
                print('<%d>..:[Erro na linha %d] Valor inteiro não informado' % (add_linhas(), linha))
                add_erro('[Erro linha %d]' % linha)
                return False
            armazena_memoria(temp[0], int(temp[1]))
        return True
    else:
        if not '=' in opcao:
            print('<%d>..:[Erro na linha %d] O operador "=" não foi informado' % (add_linhas(), linha))
            add_erro('[Erro linha %d]' % linha)
            return False
        temp = opcao.split('=')
        if not temp[1].isdigit():
            print('<%d>..:[Erro na linha %d] Valor inteiro não informado' % (add_linhas(), linha))
            add_erro('[Erro linha %d]' % linha)
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
            add_erro('[Erro linha %d]' % linha)
            return False
        operacao = var[operacao[0]] + var[operacao[1]]
        print('<%d>..: %s' % (add_linhas() ,operacao))
        return True
    if '-' in opcao:
        operacao = opcao.split('-')
        if not operacao[0] in var or not operacao[1] in var:
            print('<%d>..:[Erro na linha %d] Valor não encontrado' % (add_linhas(), linha))
            add_erro('[Erro linha %d]' % linha)
            return False
        operacao = var[operacao[0]] - var[operacao[1]]
        print('<%d>..: %s' % (add_linhas() ,operacao))
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

    elif '-a' in opcao or '--aceitacao' in opcao:
        verifica_expressao(opcao)
    
    else:
        print('<%d>..: [Erro na linha %d] Escolha uma opção válida.' % (add_linhas(),linhas))
        add_erro('[Erro linha %d]' % linhas)
        help()

for a in controle_erros:

    print('<%d>..: %s' % (add_linhas(), a))

print('<%d>..: Total de erros: %d' % (add_linhas(), contador_de_erros))
print('<%d>..: Saindo do console...' % add_linhas())