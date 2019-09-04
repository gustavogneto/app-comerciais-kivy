"""a = int(input("insira o primeiro numero"))
b = int(input("insira o segundo numero"))

if (a > b):
    print("A, é maior");
elif (a < b):
    print("B, é maior");
elif (b == a):
    print("B = A");"""



acao = input("digite 1 para sim, digite dois para não")
while acao != 1 or acao !=2:

    if type(acao) is not int:
        print("não é um numero inteiro")
        acao = input("digite 1 para sim, digite dois para não")
    else:
        if acao == 1:
            print("você disse sim: %i" %acao)

        else:
            print("você disse não: %i" %acao)


