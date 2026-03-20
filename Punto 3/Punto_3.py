#inicio
f=input("Ingrese una frase: ").lower()
vocales=""
a=0
e=0
i=0
o=0
u=0
for letra in f:
    if letra in "a":
        a=a+1
    elif letra in "e":
        e=e+1
    elif letra in "i":
        i=i+1
    elif letra in "o":
        o=o+1
    elif letra in "u":
        u=u+1
print("La letra a se repite: ",a," veces")
print("La letra e se repite: ",e," veces")
print("La letra i se repite: ",i," veces")
print("La letra o se repite: ",o," veces")
print("La letra u se repite: ",u," veces")
