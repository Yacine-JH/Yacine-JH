binaire = list(input("Entrer votre nombre en binaire"))
# print(binaire)
# print(binaire[0])
int_liste = list(map(int,binaire))
j = 0
s = 0
for i in int_liste:
    s = s + (int_liste[i] * 2**j)
    j = j+1
print(s)
