import ply.yacc as yacc
from pascal_lex import tokens, lexer

symbol_table = {}

def p_program(p):
    '''program : PROGRAM ID PONTO_VIRGULA var_declaration_part BEGIN body END PONTO'''
    p[0] = ('program', p[2], p[4], p[6][1])

def p_var_declaration_part(p):
    '''var_declaration_part : VAR var_declaration_list
                           | empty'''
    p[0] = p[2] if len(p) > 2 else []

def p_var_declaration_list_single(p):
    'var_declaration_list : var_declaration'
    p[0] = [p[1]]

def p_var_declaration_list_no_semicolon(p):
    'var_declaration_list : var_declaration_list var_declaration'
    p[0] = p[1] + [p[2]]

def p_var_declaration_list_with_semicolon(p):
    'var_declaration_list : var_declaration_list PONTO_VIRGULA var_declaration'
    p[0] = p[1] + [p[3]]

def p_var_declaration(p):
    '''var_declaration : id_list DOISPONTOS type PONTO_VIRGULA'''
    for var_id in p[1]:
        if var_id in symbol_table:
            raise SyntaxError(f"Variável '{var_id}' já declarada")
        symbol_table[var_id] = p[3]
    p[0] = ('var_declaration', p[1], p[3])

def p_id_list(p):
    '''id_list : ID
              | id_list VIRGULA ID'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

def p_body(p):
    'body : statements'
    p[0] = ('body', p[1])

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]

def p_statement(p):
    '''statement : assign
                 | writeln
                 | write
                 | readln
                 | read
                 | if
                 | case
                 | while
                 | for
                 | function
                 | procedure
                 | func_call'''
    p[0] = p[1]

def p_writeln(p):
    'writeln : WRITELN "(" Args ")" PONTO_VIRGULA'
    p[0] = ('writeln', p[3])

def p_write(p):
    'write : WRITE "(" Args ")" PONTO_VIRGULA'
    p[0] = ('write', p[3])

def p_readln(p):
    'readln : READLN "(" Args ")" PONTO_VIRGULA'
    p[0] = ('readln', p[3])

def p_read(p):
    'read : READ "(" Args ")" PONTO_VIRGULA'
    p[0] = ('read', p[3])

def p_parametro(p):
    'Args : Args VIRGULA Arg'
    p[0] = p[1] + [p[3]]

def p_args_single(p):
    'Args : Arg'
    p[0] = [p[1]]

def p_arg(p):
    '''Arg : const
           | var'''
    p[0] = p[1]

def p_statement_assign(p):
    'assign : var ASSIGN expression PONTO_VIRGULA'
    p[0] = ('assign', p[1], p[3])

def p_statement_if(p):
    '''if : IF expression THEN statement
          | IF expression THEN statement ELSE statement
          | IF expression THEN compound_statement
          | IF expression THEN compound_statement ELSE compound_statement'''
    if 'ELSE' in p:
        p[0] = ('if', p[2], p[4], p[6])
    else:
        p[0] = ('if', p[2], p[4])

def p_statement_case(p):
    '''case : CASE expression OF case_branches END PONTO_VIRGULA
            | CASE expression OF case_branches ELSE statements END PONTO_VIRGULA'''
    p[0] = ('case', p[2], p[4]) if len(p) == 7 else ('case', p[2], p[4], p[6])

def p_case_branches(p):
    '''case_branches : case_branches case_branch
                     | case_branch'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else [p[1]]

def p_case_branch(p):
    'case_branch : case_labels DOISPONTOS statement'
    p[0] = ('case_branch', p[1], p[3])

def p_case_labels(p):
    '''case_labels : case_labels VIRGULA const
                   | const'''
    p[0] = p[1] + [p[3]] if len(p) == 4 else [p[1]]

def p_expression(p):
    'expression : expression OR and_expr'
    p[0] = ('or', p[1], p[3])

def p_expression_base(p):
    'expression : and_expr'
    p[0] = p[1]

def p_and_expr(p):
    'and_expr : and_expr AND not_expr'
    p[0] = ('and', p[1], p[3])

def p_and_expr_base(p):
    'and_expr : not_expr'
    p[0] = p[1]

def p_not_expr_not(p):
    'not_expr : NOT not_expr'
    p[0] = ('not', p[2])

def p_not_expr_base(p):
    'not_expr : rel_expr'
    p[0] = p[1]

def p_rel_expr(p):
    '''rel_expr : arith_expr rel_op arith_expr
                | arith_expr'''
    p[0] = ('rel_op', p[2], p[1], p[3]) if len(p) == 4 else p[1]

def p_rel_op(p):
    '''rel_op : IGUAL
              | DIFF
              | MAIOR
              | MENOR
              | MENOR_IGUAL
              | MAIOR_IGUAL'''
    p[0] = p[1]

def p_arith_expr(p):
    'arith_expr : arith_expr add_op term'
    p[0] = ('bin_op', p[2], p[1], p[3])

def p_arith_expr_term(p):
    'arith_expr : term'
    p[0] = p[1]

def p_add_op(p):
    '''add_op : MAIS
              | MENOS
              | OR'''
    p[0] = p[1]

def p_term(p):
    'term : term mul_op factor'
    p[0] = ('bin_op', p[2], p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_mul_op(p):
    '''mul_op : MULT
              | DIVIDE
              | AND
              | DIV
              | MOD'''
    p[0] = p[1]

def p_factor(p):
    '''factor : const
              | var
              | "(" expression ")"
              | func_call'''
    p[0] = p[1] if len(p) == 2 else p[2]

def p_ciclo_while(p):
    '''while : WHILE expression DO compound_statement PONTO_VIRGULA
             | WHILE "(" expression ")" DO compound_statement PONTO_VIRGULA'''
    p[0] = ('while', p[3], p[6]) if len(p) == 8 else ('while', p[2], p[4])

def p_ciclo_for(p):
    '''for : FOR ID ASSIGN expression TO expression DO compound_statement PONTO_VIRGULA
           | FOR ID ASSIGN expression DOWNTO expression DO compound_statement PONTO_VIRGULA'''
    direction = p[5].lower()
    p[0] = ('for', direction, p[2], p[4], p[6], p[8])

def p_compound_statement(p):
    'compound_statement : BEGIN statements END'
    p[0] = p[2]

def p_proc_decl(p):
    'procedure : PROCEDURE ID "(" params ")" PONTO_VIRGULA var_declaration_part BEGIN body END PONTO_VIRGULA'
    p[0] = ('procedure', p[2], p[4], p[7], p[9])

def p_func_decl(p):
    'function : FUNCTION ID "(" params ")" DOISPONTOS type PONTO_VIRGULA var_declaration_part BEGIN body END PONTO_VIRGULA'
    p[0] = ('function', p[2], p[4], p[7], p[9], p[11])

def p_params(p):
    '''params : param_list
              | empty'''
    p[0] = p[1] if len(p) > 1 else []

def p_param_list(p):
    '''param_list : param
                  | param_list PONTO_VIRGULA param'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

def p_param(p):
    'param : id_list DOISPONTOS type'
    p[0] = ('param', p[1], p[3])

def p_const(p):
    '''const : STRING
             | NUM'''
    p[0] = ('const', p[1])

def p_var(p):
    '''var : ID
           | ID "[" expression "]"'''
    p[0] = ('var', p[1]) if len(p) == 2 else ('array_access', p[1], p[3])

def p_type(p):
    '''type : INTEGER
            | REAL
            | STRING_TYPE
            | BOOLEAN
            | array_type'''
    p[0] = p[1].lower() if isinstance(p[1], str) else p[1]

def p_array_type(p):
    '''array_type : ARRAY "[" NUM DOUBLEPOINTS NUM "]" OF type
                  | ARRAY "[" NUM "]" OF type'''
    if len(p) == 9:
        p[0] = ('array', p[3], p[5], p[8])
    else:
        p[0] = ('array', p[3], p[3], p[6])

def p_func_call(p):
    '''func_call : ID "(" Args ")"
                 | BUILTIN_FUNC "(" Args ")"'''
    p[0] = ('func_call', p[1], p[3])

def p_empty(p):
    'empty :'
    p[0] = []

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}, próximo ao token '{p.value}'")
    else:
        print("Erro de sintaxe no final do arquivo")

parser = yacc.yacc()
