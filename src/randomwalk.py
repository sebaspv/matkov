import random

for _ in range(10):
    valor = random.random()
    if valor < 0.5:
        print("izquierda")
    else:
        print("derecha")