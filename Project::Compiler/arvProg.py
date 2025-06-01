from pascal_lex import lexer
from pascal_sin import parser
from codegen import CodeGenerator
from pprint import pprint
import sys
from graphviz import Digraph

def visualize_ast(ast, filename="ast"):
    """Gera uma visualização da AST usando Graphviz com layout aprimorado"""
    dot = Digraph(comment='Árvore Sintática Abstrata (AST)')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.5', ranksep='0.8')
    
    # Estilos consistentes
    styles = {
        'program': {'shape': 'box3d', 'color': 'darkolivegreen2', 'style': 'filled'},
        'declaration': {'shape': 'box', 'color': 'lightblue2', 'style': 'filled'},
        'statement': {'shape': 'diamond', 'color': 'lightcoral', 'style': 'filled'},
        'control': {'shape': 'hexagon', 'color': 'gold', 'style': 'filled'},
        'operation': {'shape': 'circle', 'color': 'lightgreen', 'style': 'filled'},
        'io': {'shape': 'parallelogram', 'color': 'plum', 'style': 'filled'},
        'default': {'shape': 'ellipse', 'color': 'grey90', 'style': 'filled'}
    }

    node_counter = 0

    def add_node(label, node_type='default'):
        nonlocal node_counter
        node_counter += 1
        style = styles.get(node_type, styles['default'])
        dot.node(str(node_counter), label, **style)
        return str(node_counter)

    def process_node(node, parent_id=None):
        if isinstance(node, tuple):
            node_type = node[0]
            
            if node_type == 'program':
                current_id = add_node(f'Programa\n{node[1]}', 'program')
                # Processa declarações
                decls_id = add_node('Declarações', 'declaration')
                dot.edge(current_id, decls_id)
                for decl in node[2]:
                    process_node(decl, decls_id)
                # Processa statements
                stmts_id = add_node('Comandos', 'declaration')
                dot.edge(current_id, stmts_id)
                for stmt in node[3]:
                    process_node(stmt, stmts_id)
                return current_id
                
            elif node_type == 'var_declaration':
                current_id = add_node(
                    f'Declaração de Variáveis\n{", ".join(node[1])}\nTipo: {node[2]}', 
                    'declaration'
                )
                if parent_id:
                    dot.edge(parent_id, current_id)
                return current_id
                
            elif node_type in ('writeln', 'readln'):
                current_id = add_node(node_type.upper(), 'io')
                if parent_id:
                    dot.edge(parent_id, current_id)
                for arg in node[1]:
                    process_node(arg, current_id)
                return current_id
                
            elif node_type == 'assign':
                current_id = add_node('Atribuição', 'statement')
                if parent_id:
                    dot.edge(parent_id, current_id)
                process_node(node[1], current_id)
                process_node(node[2], current_id)
                return current_id
                
            elif node_type == 'for':
                current_id = add_node(
                    f'Loop FOR\nVariável: {node[2]}\nDe: {node[3][1]}\nAté: {node[4][1]}', 
                    'control'
                )
                if parent_id:
                    dot.edge(parent_id, current_id)
                process_node(node[5][0], current_id)
                return current_id
                
            elif node_type == 'bin_op':
                current_id = add_node(f'Operação\n{node[1]}', 'operation')
                if parent_id:
                    dot.edge(parent_id, current_id)
                process_node(node[2], current_id)
                process_node(node[3], current_id)
                return current_id
                
            elif node_type in ('var', 'const'):
                current_id = add_node(f'{node_type.upper()}\n{node[1]}', 'default')
                if parent_id:
                    dot.edge(parent_id, current_id)
                return current_id
                
            else:
                current_id = add_node(str(node_type), 'default')
                if parent_id:
                    dot.edge(parent_id, current_id)
                for child in node[1:]:
                    process_node(child, current_id)
                return current_id
                
        elif isinstance(node, list):
            current_id = add_node('Lista', 'default')
            if parent_id:
                dot.edge(parent_id, current_id)
            for item in node:
                process_node(item, current_id)
            return current_id
            
        else:
            current_id = add_node(str(node), 'default')
            if parent_id:
                dot.edge(parent_id, current_id)
            return current_id

    process_node(ast)
    
    # Ajustes de layout
    dot.attr(compound='true')
    dot.format = 'png'
    dot.render(filename, cleanup=True)
    print(f"Visualização da AST gerada em: {filename}.png")

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Insira o caminho do ficheiro Pascal (.pas): ")

    if not filename.endswith('.pas'):
        print("O arquivo deve ter extensão .pas!")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print("Ficheiro não encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    lexer.input(data)
    
    try:
        print("\n[1/3] Análise léxica concluída")
        ast = parser.parse(data, lexer=lexer)
        print("[2/3] Análise sintática concluída")
        
        print("\nÁrvore Sintática Abstrata (AST):")
        pprint(ast)
        
        output_base = filename.replace('.pas', '')
        visualize_ast(ast, output_base + '_ast')
        
        # Geração de código (opcional)
        if input("\nGerar código assembly? (s/n): ").lower() == 's':
            print("[3/3] Gerando código assembly...")
            codegen = CodeGenerator()
            asm_code = codegen.gen(ast)
            asm_file = output_base + '.asm'
            with open(asm_file, 'w') as f:
                f.write(asm_code)
            print(f"Código assembly gerado em: {asm_file}")
        
    except SyntaxError as e:
        print(f"\nErro de sintaxe: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == '__main__':
    print("=== Compilador Pascal ===")
    main()