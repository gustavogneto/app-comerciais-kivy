# coding: utf-8

# try:
#     a = 10 / 0
#     print(a)
# except ZeroDivisionError:
#     print("não pode dividir de por 0")
# multiplas exceções

def erro(x):
    try:
        eval(x)
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError,  NameError):
        print("TypeError or NameError")

#typeerror . TypeError
erro("int+int")
#nameError
erro("a")
#ValueError
erro("int('a')")
#DivisionError
erro("5/0")
#sem error
erro("10+10")
print("aplicação finalizada")

# multiplas exceções

