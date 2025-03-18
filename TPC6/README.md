# TPC6 Recursivo Descendente

O objeto do TPC 6 é criar um paser **recursivo descendente** que analise uma expressão aritmética, respeitando a forma de cálculo aritemético e por fim dar o resultado de tal expressão dada pelo o utilizador.
O parser vai ler as expressões +,-, os termos *,/, para representar a forma de calculo correto, (,), como expressões para forçar o que esteja dentro seja calculado primeiro, e em forma de termos os digitos.

## 1 - Função Tokenize

![função tokenize](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc6_2.png)

Esta função converte a string dada por o utilizado numa expressão matemática em uma lista de tokens (números e operadores)

## 2 - Classe Parser

### 2.1 - Funções init/peek/consume/parse_expr

![função parser1](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc6_3.png)

#### 2.1.1. Init

Inicializa a posição atual do token no início da lista.

#### 2.1.2 Peek

Olha o token atual sem consumir, e decide que operação decide fazer.

#### 2.1.3 Consume

Retorna o token consumido

#### 2.1.4 parse_expr

Calcula expressões com + e -

### 2.2 - Funções parse_term e parse_factor

![função parser2](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc6_4.png)

#### 2.2.1 Parse_term

Calcula expressões com * e /.

#### 2.2.2 Parse_factor

Analisa números e expressões entre parênteses

## 3 - main
![função main](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc6_5.png)

Temos um ciclo quase infinito que só acaba quando o utilizador escrever "sair", para cada expressão introduzida, cria o parser, depois cria os tokens e por final, cerifica de todos os tokens foram utilizados

O fluxo da Main:
1. O utilizador introduz a expressão
2. tokenize(): transforma em tokens.
3. Parser() → configura o parser.
4. parse_expr() → chama outras funções recursivamente.
5. Calcula resultado e imprime.



## 4 - Resultados

![resultados](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc6_6.png)

Aqui temos alguns resultados, com o programa a correr.
