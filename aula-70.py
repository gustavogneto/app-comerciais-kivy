# lista_num = [100,200,300,400]
# for item in lista_num:
# print(item)


# lista_num = [100,200,300,400]
# lista_indice = [0,1,2,3]
# for item in lista_indice:
#     lista_num[item] += 1000
# print(lista_num)

#
# lista_num = [100,200,300,400,500]
# lista_indice = range(lista_num.__len__())
# for item in lista_indice:
#     lista_num[item] += 1000
# print(lista_num)

lista_num = [100, 200, 300, 400, 500,600,700,800,900]
for idx, item in enumerate(lista_num):
    lista_num[idx] += 1000
    print(lista_num)
