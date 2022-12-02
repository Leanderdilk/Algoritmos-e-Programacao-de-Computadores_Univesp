class Pilha:

    def __init__(self):
        self.data = []

    def empty(self):
        return len(self.data) == 0

    def pop(self):
        if not self.empty():
            return self.data.pop(-1)

    def top(self):
        if not self.empty():
            return self.data[-1]

    def push(self, x):
        self.data.append(x)

p = Pilha()
num = 32150

while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

while not p.empty():
    print(p.pop())