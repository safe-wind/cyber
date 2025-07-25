# Scrivere un programma PYTHON che a partire da una stringa la 
# cifra con la tecnica XOR
# Successivamente mostrare che la stringa cifrata, riapplicando 
# lo stesso XOR, torna la stringa originale
# Per fare lo XOR utilizzate un solo valore: 57
# Quindi data la stringa di esempio “Nel mezzo del cammin di 
# nostra vita”, dovete fare per ogni carattere della stringa lo 
# xor con il valore 57
# “N” xor 57, “e” xor 57, …
# Ottenendo una lista di numeri es: 78 (che è il codice asciii  
# della lettera N) xor (si indica con il simbolo ^) 
# => 78 ^ 57 = 119
# E così via per tutta la stringa.
# Al termine stampare la lista di numeri ottenuti
# In fondo a partire dalla lista di numeri, riapplicare lo xor 
# sempre con 57 e quindi ottenere (ricostruendola) la stringa 
# originale
# NB: potreste utilizzare input(“…”) in modo da leggere sia la 
# stringa da cifrare, sia il valore segreto da applicare come 
# xor

valore = 57
frase_da_cript = input("Inserisci una stringa da criptare: ")
frase_da_cript = frase_da_cript.lower()
messaggio_cifrato = ""

lista_caratteri = list()

for el in frase_da_cript:

    el = ord(el) ^ 57
    lista_caratteri.append(el)

for el1 in lista_caratteri:

    el1 = chr(el1)
    nuova_frase+=el1

print(messaggio_cifrato.lower())





