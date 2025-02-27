# TPC3 - Convertor MarkDown para HTML

O objetivo deste TPC, como o titulo sujere é pecorrer um texto, e converter as expressões em texto que estão assinaladas em Mark Down e converte-las para as tags incadas para HTML.

## Conversão expressões do tipo Titulo de # para tags tipo <h>

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-01.png)


No código apresentado, ao receber um string é usado uma expressão linear que faz um match para ver se tem o char #, depois conta quantas vezes esse caracter tem, que faz um add para a tag em html


![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-06.png)

Resultado da aplicção do código

## Negrito e Italico

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-02.png)

Aqui temos o a substituição de negrito e italico, são só duas expreções lineares, que fazem a substitição


![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-08.png)

Resultado da aplicação do código


## Listas

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-04.png)

Este código deveria aplicar um match há lista, se tivesse um numero decimal, pecorria essa lista e se ainda não ainda não tivesse match
metia a tag <lo> e punha até a tag <li>, com isto tem uma flag para meter a tag para parar. Este racioncion não resulta, e por falta de tempo não possível
melhorar o código.

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-07.png)

Resultado da aplicação dos código de conversão para as listas

## Imagens e Links

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-03.png)

Igual como a conversão do Negrito e Itálico 

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-09.png)

Resultado para as imagens

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-10.png)

Resultado para os Links

## MENU

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-05.png)

![Codigo das convesão para os titulos](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc4-11.png)

Esta função recebe um texto do stdin até o utilizador escrever end e depois aplica a conversão

