# Programando com condições

n1 = eval(input("Qual foi a sua nota na primeira prova?"))
n2 = eval(input("Qual foi a sua nota na segunda prova?"))

media = (0.4 * n1) + (0.6 * n2)

if media >= 5.0:
    print("A sua média foi:", media)
    print("Você foi aprovado")
else:
    print("A sua média foi:", media)
    print("Você foi reprovado")