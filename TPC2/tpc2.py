import re
from collections import Counter


def readFile(data_dic): 
    with open("obras.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()

    
    corrected_lines = []
    temp_line = ""
    inside_quotes = False

    for line in lines:
        line = line.strip()
        
        if '"' in line:  # Verifica se há aspas
            inside_quotes ^= line.count('"') % 2 != 0  
        
        temp_line += (" " if temp_line else "") + line  
        
        if not inside_quotes:  
            corrected_lines.append(temp_line)
            temp_line = ""
            
            
        
    # Processar cabeçalho
    header = corrected_lines[0].split(";")
    filtered_header = [col for col in header if col != "desc"] 

    # Processar dados
    for line in corrected_lines[1:]:  
        
        values = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)

        values = [val.strip('"') for val in values]

        
        filtered_values = [val for i, val in enumerate(values) if i < len(header) and header[i] != "desc"]
        
        data_dic.append(dict(zip(filtered_header, filtered_values)))

    
def listar_compositores(data_dict):
    compositores = sorted(set(obra["compositor"] for obra in data_dict))
    print(compositores)
    return

def contagem_obras_por_periodo(data_dic):
    contagem_periodos = Counter(obra['periodo'] for obra in data_dic)
    print(contagem_periodos)
    return

def lista_de_obras_periodo(data_dic):
    obras_por_periodo = {}

    for obra in data_dic:
        periodo = obra['periodo']
        nome = obra['nome']
        if periodo not in obras_por_periodo:
            obras_por_periodo[periodo] = []  # Criar lista se não existir
        obras_por_periodo[periodo].append(nome)# Adicionar obra ao período correspondente
        
    for periodo in obras_por_periodo:
        obras_por_periodo[periodo].sort()
            
    print(obras_por_periodo)
 

def main():
    data_dict = []
    readFile(data_dict)
    listar_compositores(data_dict)
    contagem_obras_por_periodo(data_dict)
    lista_de_obras_periodo(data_dict)
    
if __name__ == "__main__":
    main()
