#from curses.ascii import isalpha
from pydoc import text
from statistics import quantiles
from string import printable


texto = "int total = 10; total += 5; if (total >= 15 && total != 20) { total++; }"

linhas = texto.splitlines(keepends= True) # separa as linhas e mantem o ultimo caractere de quebra
print("quantidade de linhas:", len(linhas))

#-------
lVazias = 0
for i iin linhas:
    if i == "\n":
        lVazias += 1

print("quantidade de linhas vazias ", lVazias)

#---------

semEspaco = texto.replace(' ', '') # remove os espacos 
semQuebra = semEspaco.replace('\n','')# remove as quebras de linha 
qntCaracteres = len(semQuebra)
print(f"Quantidade de caracteres sem quebra: {qntCaracteres}")

#-----------

qntLetras = 0 

#contar quantas letras 
for i in semQuebra:
    if i.isalpha():
        qntLetras += 1
print(f"Quantidade de letras: {qntLetras}")



