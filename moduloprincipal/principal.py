# coding: utf-8
# library reload modulo
import importlib
# library reload modulo
# importando modulo
import modulo


del(modulo.c)
modulo.a = 0
# recarregando modulo
importlib.reload(modulo)
# recarregando modulo
from pprint import pprint

pprint(modulo.__dict__)
# todo __main__, ponto de entrada principal da aplicação
# if __name__ == "__main__":
#     print("aplicação pode ser inicializada")

