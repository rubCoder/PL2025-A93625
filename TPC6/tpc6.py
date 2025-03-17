def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(int(num))
        elif expr[i] in '+-*/()':
            tokens.append(expr[i])
            i += 1
        elif expr[i] == ' ':
            i += 1  # ignora espaços
        else:
            raise ValueError(f"Caractere inválido: {expr[i]}")
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        token = self.peek()
        if token is not None:
            self.pos += 1
        return token

    def parse_expr(self):
        result = self.parse_term()
        while self.peek() in ('+', '-'):
            op = self.consume()
            right = self.parse_term()
            if op == '+':
                result += right
            else:
                result -= right
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.peek() in ('*', '/'):
            op = self.consume()
            right = self.parse_factor()
            if op == '*':
                result *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("Divisão por zero")
                result /= right
        return result

    def parse_factor(self):
        token = self.peek()
        if isinstance(token, int):
            self.consume()
            return token
        elif token == '(':
            self.consume()
            result = self.parse_expr()
            if self.peek() != ')':
                raise ValueError("Esperado ')'")
            self.consume()
            return result
        else:
            raise ValueError(f"Esperado número ou '(', obtido {token}")

def main():
    print("Calculadora (digite 'sair' para encerrar)")
    while True:
        expr = input(">> ")
        if expr.lower() in ('sair', 'exit', 'quit'):
            break
        try:
            tokens = tokenize(expr)
            parser = Parser(tokens)
            resultado = parser.parse_expr()
            # Verifica se todos os tokens foram consumidos
            if parser.peek() is not None:
                raise ValueError("Expressão mal formada")
            print(f"= {resultado}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
