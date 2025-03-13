# TPC 5 - Maquina de estados -Vending Machine

O objectivo deste tpc é criar uma vending machine que ao ler um ficheiro JSON, com um triplo de dados, são manipulados pelo o programa e depois gravados, no fim do processo

# Código

## 1-Ficheiro JSON

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_014.png)

Aqui vemos a estrutura do ficheiro que vai ser lido pelo o programa, em é constituido pelo quatro campos, codigo, nome, quantidade e preço.


## 2 - Leitura do Ficheiro JSON

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_011.png)

A função ler o ficheiro, como o nome implica le o ficheiro JSON que tem o stock da máquina, mete num dicionário

## 3 - Listar Produtos

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_012.png)

Na função de listar os produto é um simples for each que faz print de cada valor do dicionario.


## 4 - Inserir Moeda
![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_013.png)

Recebe uma sting do genero 1e50c divide os valores em 1e e 50c, e tranforma em valores númericos

## 5 - Selecionar o Produto

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_015.png)

Este codigo verifica, se o código do item existe, se tem quantidade e saldo sufeciente, depois de passar essas verificações
é atualizado o saldo do cliente como também a quantidade.

## 6 - Calcula o Troco

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_016.png)


## 7 - Menu
![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_017.png)

No menu o stock é carregado automáticamente e depois só tem de introduzir a opção que pretende, Exemplo: MOEDA 1e50

# Resultados

## 1 - Listar os dados

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_18.png)

## 2 - Inserir Moeda

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_19.png)

## 3 - Selecionar o Produto

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc5_20.png)
