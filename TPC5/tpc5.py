import json


def lerJason():    
    with open('/home/rubenoliveira/Documentos/Processamento de Linguagens/PL2025-A93625/TPC5/stock.json', 'r') as file:
         data = json.load(file)
    file.close()
    return data

def listar_produtos(stock):
    print("cod    |  nome        |  quantidade  |  preço")
    print("-------------------------------------------------")
    for produto in stock:
        print(f"{produto['cod']:6} | {produto['nome']:12} | {produto['quant']:10} | {produto['preco']:.2f}€")
       
def guardar_stock(stock):
    with open("/home/rubenoliveira/Documentos/Processamento de Linguagens/PL2025-A93625/TPC5/stock.json", "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)

def inserir_moedas():
    saldo = 0  
    valores = {"1e": 1.0, "50c": 0.5, "20c": 0.2, "10c": 0.1, "5c": 0.05, "2c": 0.02, "1c": 0.01} 
    
    entrada = input(">> MOEDA ").lower().replace(" ", "").split(",")  
    for moeda in entrada:
        if moeda in valores:
            saldo += valores[moeda]
        else:
            print(f"maq: Moeda inválida ({moeda}), ignorada.")

    print(f"maq: Saldo atualizado = {saldo:.2f}€")
    return saldo  

def calcular_troco(saldo):
    valores = [(1.0, "1e"), (0.5, "50c"), (0.2, "20c"), (0.1, "10c"), (0.05, "5c"), (0.02, "2c"), (0.01, "1c")]
    troco = {}
    for valor, nome in valores:
        if saldo >= valor:
            quantidade = int(saldo // valor)
            troco[nome] = quantidade
            saldo -= quantidade * valor
    return troco


def selecionar_produto(codigo, saldo, stock):
    for produto in stock:
        if produto["cod"] == codigo:
            if produto["quant"] > 0:
                if saldo >= produto["preco"]:
                    produto["quant"] -= 1
                    saldo -= produto["preco"]
                    print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                    return saldo
                else:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {saldo:.2f}€; Pedido = {produto['preco']:.2f}€")
                    return saldo
            else:
                print("maq: Produto esgotado!")
                return saldo
    print("maq: Código inválido!")
    return saldo

def main():
    stock = lerJason()
    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    #listar_produtos(stock)
    
    saldo = 0
    
    while True:
        comando = input(">> ").strip().upper()
        if comando == "LISTAR":
            listar_produtos(stock)
        elif comando.startswith("MOEDA"):
            saldo += inserir_moedas()
            print(f"maq: Saldo = {saldo:.2f}€")
        elif comando.startswith("SELECIONAR"):
            partes = comando.split()
            if len(partes) > 1:
                saldo = selecionar_produto(partes[1], saldo, stock)
        elif comando == "SAIR":
            troco = calcular_troco(saldo)
            print("maq: Pode retirar o troco:")
            for moeda, quantidade in troco.items():
                print(f"{quantidade}x {moeda}")
            print("maq: Até à próxima!")
            guardar_stock(stock)
            break
        else:
            print("maq: Comando inválido!")

if __name__ == "__main__":
    main()