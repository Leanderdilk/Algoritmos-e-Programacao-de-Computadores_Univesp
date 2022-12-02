# primeiro programa em python: 
# Imprime o peso ideal de acordo com a altura e o sexo biológico.
# c = input("Digite a temperatura em Celsius: ")
# c_temp = eval(c)
# f = 1.8 * c_temp + 32
# print("A temperatura correspondente em Fahrenheit é",f)

# exemplo com condição
# calcula o peso ideal conforme altura e sexo

altura = eval(input("Qual a sua altura em metros?"))
sexo = input("Digite F para Feminino e M para Masculino")

if sexo == 'M':
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

    print("O peso ideal é:", peso)
    
    