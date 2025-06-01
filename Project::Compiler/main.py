from pascal_lex import lexer
from pascal_sin import parser
from codegen import CodeGenerator
from pprint import pprint

def main():
    filename = input("Insere o caminho do ficheiro Pascal (.pas): ")

    try:
        with open(filename, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print("Ficheiro não encontrado.")
        return

    lexer.input(data)
    
    try:
        print("\nAnálise sintática:")
        ast = parser.parse(data, lexer=lexer)
        print("\nÁrvore Sintática gerada:")
        pprint(ast) 
        codegen = CodeGenerator()
        asm_code = codegen.generate(ast)
        output_filename = filename.replace('.pas', '.asm')
        with open(output_filename, "w") as f:
            f.write(asm_code)    
    except SyntaxError as e:
        print(f"\n Erro : {e}")

if __name__ == '__main__':
    main()
