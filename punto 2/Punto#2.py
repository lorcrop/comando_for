M7 = 0
M9 = 0

for i in range(1000, 5001):

    if i % 7 == 0:
        M7 += 1
    else:
        pass

    if i % 9 == 0:
        M9 += 1
    else:
        pass

print("Cantidad de múltiplos de 7:", M7)
print("Cantidad de múltiplos de 9:", M9)
