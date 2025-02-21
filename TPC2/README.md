# Análise de um dataset de obras musicais


Neste segundo TPC foi nos apresentado o desafio de pegar num dataset em csv e responder a 3 simples perguntas.
O senão é que não se podia usar a biblioteca csv, que está disponivel para o python.

A primeira resposta a este desafio, foi criar uma função que faz parsing do ficheiro, esta função elimina um dos campos, este campo a descrição, como este campo tem certos problemas, um tem várias aspas o que torna dificil remover, como também os espaços. Por ultimo o desafio dos ';' em que estão neste enormes texto.
A função readfile verifica se o campo tem várias aspas e verifica se tem ;, junta a o texto todo numa frase para tornar mais fácil a leitura, para depois separar tudo, e adicionar num dicionário. Em que podemos fazer as queries pedidas.

## 1.Lista ordenada alfabeticamente dos compositores musicais

Esta função recebe o dicionário, faz sort de enumerador por compositor.

### Resultado

![exercio1!](/img/Captura de ecrã de 2025-02-20 12-01-19.png)


## 2. Distribuição das obras por período: quantas obras catalogadas em cada período

Já esta função faz um counter, que conta quantos obras existem por periodo.

### Resultado

![exercio2!]/img/Captura de ecrã de 2025-02-20 12-01-55.png)


## 3.  Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período

Nexta função ao receber o dicionario o cria um dicionario vazio, e adiciona o periodo senão existe, se já existir adiciona a obra ao periodo correspondente.

Por ultimo faz o sort das obras por periodo.

### Resultado

![exercio3!](/img/Captura de ecrã de 2025-02-20 12-07-49.png)
