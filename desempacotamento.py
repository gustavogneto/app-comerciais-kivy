#desempacotamento



def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

lista = ["gustavo","gomes",37]
pessoa(*lista)


lista = [ 11 , 10 , 12 ]
def func(a,b,c):
    print(a)
    print(b)
    print(c)

func(**dict(zip(("b", "a", "c"), lista)))