#EXEMPLOS DE TUPLAS
# inicio = 0
# fim = 0  # type: int
# for fim in range(inicio,100):
#
#     tupla=(range(inicio,fim))
#     fim += 1
#     if fim == 50:
#
#         print ("--------------------------")
#         print("fim, break %i " %fim)
#         break
#     for i in tupla:
#         print(tupla)
#         if i == 3:
#
#             print("--------------------------")
#             print("fim, depois do break %i " % fim)
#             break")

#EXEMPLOS DE LISTAS


entrada=""
hd = []
while entrada != "z":
    entrada = input("digite algo: ")
    hd.append(entrada)

print(hd)
print(hd.__len__())
