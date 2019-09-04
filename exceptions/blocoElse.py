# coding: utf-8


def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print(e)  # arguments as messages


    except ZeroDivisionError as e:
        print(e)
    except (TypeError, NameError) as e:
        print(e)
    else:
        print("nada aconteceu")
    finally:
        print("sempre vai rodar")

# typeerror . TypeError
erro("int+int")
# nameError
erro("a")
# ValueError
erro("int('a')")
# DivisionError
erro("5/0")
# sem error
print("aplicação finalizada")

erro("10 + 10")
