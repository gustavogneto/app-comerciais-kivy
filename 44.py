idade =int(input("Informe sua idade: "))

if (idade<=0):
    print("sidade não pode ser menor ou igual a zero");
elif idade >= 150:
    print("Sua idade não pode ser maior que 150 anos");
elif idade < 18:
    print("Você é de menor");
else:
    print("você está dentro dos requisitos de entrada")