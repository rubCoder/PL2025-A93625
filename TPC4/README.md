# TPC4 - Analisador Léxico

Objetivo do TPC é realizar um Analizador Léxico para um linguagens de consulta.

## TOKENS Utilizados

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc-01.png)

Aqui temos uma lista com padrões de expressões regulares(regex) para reconhecer um tipo de padrões, para depois serem comparadas.

Os principais padrões são:

- SELECT, WHERE, LIMIT: Palavras-chave da linguagem;
- \?[a-zA-Z_]\w*: Reconhece variáveis, como ?nome, ?desc;
- "[^\"]*": Captura strings entre aspas, como "Chuck Berry";
- \.: Captura o caractere ponto (.);
- \{, \}: Capturam { e } para abrir e fechar blocos;
- \s+: Captura espaços em branco ;
- [a-zA-Z_][a-zA-Z0-9_]*: Captura identificadores como dbo:MusicalArtist;
- :, ;: Capturam : e ; ;
- @[a-zA-Z]+ : O tipo de lingua;
- '\d+': Digitos.



![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc-02.png)

Neste pedaço de codigo temos a classe é a resposável pelo o analisador lexico, que vai dividir a string em **tokens**.
A classe analisa, usa um ciclo que ao encotrar o token e adiciona há lista.
A classe extrair_token, pecorre a listas de padrões e tenta fazer o match.

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc-03.png)

Por fim a classe main, é uma simples classe em que o utilizador mete o que quer por consulta, e ao escrever **END**, em maiusculas dá o resultado.

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc-dadosintroducao.png)

Aqui temos o input introduzido.

![LISTA DE TOKENS UTILIZADA](https://github.com/rubCoder/PL2025-A93625/blob/main/img/tpc-resultado.png)

O resultado do algoritmo.