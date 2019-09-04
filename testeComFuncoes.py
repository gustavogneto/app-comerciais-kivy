# testando funções
def soma(x, y):
    total = x + y
    print("-----------soma-----------")
    return total


# parametros defalt
def login(usuario="root", senha=123):
    print("-----------login-----------")
    print("usuario: %s" % usuario)
    print("senha: %i" % senha)
    print("-----------login-----------")


# parametros  nomeados
def dadospessoais(nome, sobrenome, idade, sexo):
    print("-----------dados pessoais-----------")
    print("nome: {}\nsobrenome: {}\nidade: {}\nsexo: {}"
          .format(nome, sobrenome, idade, sexo))
    print("-----------dados pessoais-----------")


# parametros posicionais
def dadosdocliente(estadocivil, filhos, trabalhacom):
    print("-----------dados do cliente-----------")
    print("Estado Civil: {}\nFilhos: {}\nProfissão: {}"
          .format(estadocivil, filhos, trabalhacom))
    print("-----------dados do cliente-----------")


# teste com return
print(soma(10, 11))
# teste com tipo void, com parametros defalt
login()
# saida parâmetros nomeados
dadospessoais(nome="gustavo", sobrenome="gomes", idade=26, sexo=True)
# saida parâmetros posicionais
dadosdocliente("noivo", "sim", "analista de ti")
