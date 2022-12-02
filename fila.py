# Implementar um programa de gerenciamento de duas filas em um banco: prioritária e normal' 
# Seu programa deverá permitir que pessoas sejam inseridas no fim de cada fila, dependendo da idade'
#de cada uma (acima de 60 anos entra na fila prioritária).'
#A saída de pessoas da fila deve ocorrer da seguinte forma: a cada duas pessoas que saem da fila prioritária, ' \
#uma sai da fila norma. '


class Fila:

    def __init__(self):
        self.data = []

    def vazia(self):
        return len(self.data) == 0

    def inserir(self, x):
        return self.data.append(x)

    def remover(self):
        return self.data.pop(0)


filaPrioritaria = Fila()
fila = Fila()

atendimentoPrioritario = 0
atendimento = 0

cliente = 1
while cliente > 0:
    cliente = int(input('Digite sua idade ou 0 para sair: '))

    if cliente == 0:
        continue

    if cliente > 60:
        atendimentoPrioritario += 1
        filaPrioritaria.inserir(atendimentoPrioritario)
    else:
        atendimento += 1
        fila.inserir(atendimento)
print('-'*20)
print('Ordem das filas:')

while not filaPrioritaria.vazia() or not fila.vazia():
    for atendimentoPrioritario in range(2):
        if not filaPrioritaria.vazia():
            print('Atendimento prioritário: AP-', filaPrioritaria.remover())

    if not fila.vazia():
        print('Atendimento: A-', fila.remover())