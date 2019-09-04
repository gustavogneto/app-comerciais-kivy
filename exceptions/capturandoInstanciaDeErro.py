# coding: utf-8


def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError: ")
        print(type(e))  # instance error
        print(e)  # msgError
        print(e.args)  # arguments as messages
        print("ValueError end.")
        # print(e.with_traceback())
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError, NameError):
        print("TypeError or NameError")


# typeerror . TypeError
erro("int+int")
# nameError
erro("a")
# ValueError
erro("int('a')")
# DivisionError
erro("5/0")
# sem error
erro("10+10")
print("aplicação finalizada")

# multiplas exceções
