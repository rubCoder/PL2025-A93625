import sys


def rec_inteitos(linha):
    sinal = 0
    somatorio=0
    i = 0
    #mete o texto todo em minusculas
    linhaMinuscula = linha.lower()
    #separa por espaços
    palavras = linhaMinuscula.split(" ")
    while(i < len(palavras)):
        if palavras[i] == "on":
            sinal = 0
        if palavras[i] == "off":
            sinal = 1
        if sinal == 0 :
            if palavras[i].isdigit() :
                somatorio = somatorio + int(palavras[i])
        
        if palavras[i] == "=":
            print(somatorio)
            somatorio = 0
        i+=1
    print(somatorio)
        
    

for linha in sys.stdin:
    rec_inteitos(linha.strip())
    
    
        
    