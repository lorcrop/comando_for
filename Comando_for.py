# inicio
C_p=0
C_i=0

for i in range (1,21):
    n=int(input("Digite el numero "+str(i)+":"))
    m=n%2
    if m==0:
        C_p=C_p+1
    else:
        C_i=C_i+1
#output
print("Losnumeros pares son:"+str(C_p))