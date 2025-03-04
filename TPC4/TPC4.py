import re
import sys

# Token
TOKEN_REGEX = [
    (r'SELECT', 'SELECT'),
    (r'WHERE', 'WHERE'),
    (r'LIMIT', 'LIMIT'),
    (r'\?[a-zA-Z_]\w*', 'VARIÁVEL'),
    (r'"[^"]*"', 'STRING'),
    (r'@[a-zA-Z]+', 'LINGUA'), 
    (r'\d+', 'NUMERO'), 
    (r'\.', 'PONTO'),
    (r'\{', 'ABRE_CHAVE'),
    (r'\}', 'FECHA_CHAVE'),
    (r'\s+', None),  
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFICADOR'),
    (r':', 'DOIS_PONTOS'),
    (r';', 'PONTO_VÍRGULA'),
]


class AnalisadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.tokens = []

    def analisar(self):
        while self.pos < len(self.codigo):
            token, tipo = self.extrair_token()
            if token:
                self.tokens.append((tipo, token))
        return self.tokens

    def extrair_token(self):
        for padrao, tipo in TOKEN_REGEX:
            regex = re.compile(padrao)
            match = regex.match(self.codigo, self.pos)
            if match:
                self.pos = match.end()
                return match.group(), tipo
        raise SyntaxError(f"Token inválido perto de: {self.codigo[self.pos:self.pos+10]}")

def main():
   
    md_text = []
    print("Digite a consulta (digite 'END' para finalizar):")

    while True:
        linha = input().strip()
        if linha == "END":
            break
        md_text.append(linha)

    markdown_input = "\n".join(md_text)
    analisador = AnalisadorLexico(markdown_input)
    tokens = analisador.analisar()

    print("\nTokens identificados:")
    for token in tokens:
        print(token)

        
if __name__ == "__main__":
    main()