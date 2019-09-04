# exemplo de funcões variadicas


def valores(*arqs):
    print(arqs)

def listadeargumentroassociativos(**kwarqs):
    print(kwarqs)

def argumentos(*args, **kwargs):
    print(args, kwargs)

valores(1,2,3,4,5,6)
valores("um", "dois", "tres", "quatro")

listadeargumentroassociativos(a=1,b=2,c=3,d=4,e=5,f=6)
listadeargumentroassociativos(um=1,dois=2,tres=3,quatro=4)
argumentos(1,2,3,4,5,6,um=1,dois=2,tres=3,quatro=4)