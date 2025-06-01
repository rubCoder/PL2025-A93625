import ply.lex as lex

literals=["(",")", "[", "]", "{", "}"] 

reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'begin': 'BEGIN',
    'end': 'END',
    'integer': 'INTEGER',
    'real': 'REAL',
    'string': 'STRING_TYPE',
    'writeln': 'WRITELN',
    'readln': 'READLN',
    'write': 'WRITE',
    'read': 'READ',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'to': 'TO',
    'function': 'FUNCTION',
    'procedure': 'PROCEDURE',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'boolean': 'BOOLEAN',
    'repeat' : 'REPEAT',
    'case': 'CASE',
    'of' : 'OF',
    'div' : 'DIV',
    'mod' : 'MOD',
    'type' : 'TYPE',
    'set' : 'SET',
    'return' : 'RETURN',
    'downto' : 'DOWNTO',
    'array' : 'ARRAY'
}
   
tokens = ['ID', 'NUM', 'STRING', 'MAIOR', 'MENOR', 'IGUAL', 'MAIOR_IGUAL', 'MENOR_IGUAL',
          'MAIS', 'MENOS', 'MULT', 'DIVIDE', 'DIFF', 'ASSIGN', 'COMMENT', 'NL',
          'DOUBLEPOINTS', 'PONTO_VIRGULA', 'DOISPONTOS', 'PONTO', 'VIRGULA','BUILTIN_FUNC'] + list(reserved.values())

def t_PROGRAM(t):
    r'(?i:program)'
    return t

def t_BEGIN(t):
    r'(?i:begin)'
    return t

def t_END(t):
    r'(?i:end)'
    return t

def t_WRITELN(t):
    r'(?i:writeln)'
    return t

def t_WRITE(t):
    r'(?i:write)'
    return t

def t_VAR(t):
    r'(?i:var)'
    return t
    
def t_INTEGER(t):
    r'(?i:integer)'
    return t

def t_REAL(t):
    r'(?i:real)'
    return t

def t_BOOLEAN(t):
    r'(?i:boolean)'
    return t


def t_STRING_TYPE(t):
    r'(?i:string)'
    return t

def t_READLN(t):
    r'(?i:readln)'
    return t

def t_READ(t):
    r'(?i:read)'
    return t

def t_IF(t):
    r'(?i:if)'
    return t

def t_CASE(t):
    r'(?i:case)'
    return t

def t_OF(t):
    r'(?i:of)'
    return t

def t_THEN(t):
    r'(?i:then)'
    return t

def t_ELSE(t):
    r'(?i:else)'
    return t

def t_WHILE(t):
    r'(?i:while)'
    return t

def t_DO(t):
    r'(?i:do)'
    return t

def t_FOR(t):
    r'(?i:for)'
    return t

def t_TO(t):
    r'(?i:to)'
    return t

def t_AND(t):
    r'(?i:and)'
    return t

def t_OR(t):
    r'(?i:or)'
    return t

def t_NOT(t):
    r'(?i:not)'
    return t

def t_FUNCTION(t):
    r'(?i:function)'
    return t

def t_PROCEDURE(t):
    r'(?i:procedure)'
    return t

def t_RETURN(t):
    r'(?i:return)'
    return t

def t_DIV(t):
    r'(?i:div)'
    return t

def t_MOD(t):
    r'(?i:mod)'
    return t

def t_DOWNTO(t):
    r'(?i:downto)'
    return t

def t_ARRAY(t):
    r'(?i:array)'
    return t

def t_NUM(t):
    r'\d+(\.\d+)?'
    if '.' not in t.value:
        t.value = int(t.value)
    else:
        t.value = float(t.value)
    return t

def t_STRING(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]
    return t

def t_ASSIGN(t):
    r'\:='
    return t

def t_PONTO_VIRGULA(t):
    r'\;'
    return t

def t_DOISPONTOS(t):
    r'\:'
    return t

def t_VIRGULA(t):
    r'\,'
    return t

def t_PONTO(t):
    r'\.'
    return t

def t_MAIOR_IGUAL(t):
    r'\>='
    return t

def t_MENOR_IGUAL(t):
    r'\<='
    return t

def t_DIFF(t):
    r'\<>'
    return t

def t_MAIOR(t):
    r'\>'
    return t

def t_MENOR(t):
    r'\<'
    return t

def t_MAIS(t):
    r'\+'
    return t

def t_MENOS(t):
    r'\-'
    return t

def t_IGUAL(t):
    r'\='
    return t

def t_MULT(t):
    r'\*'
    return t

def t_DIVIDE(t):
    r'\/'
    return t

def t_ID(t): 
    r'[a-zA-Z][a-zA-Z0-9_\.]*'
    return t

def t_DOUBLEPOINTS(t):
    r'\.\.'
    return t

def t_BUILTIN_FUNC(t):
    r'(?i:length|ord|chr)'
    t.type = 'BUILTIN_FUNC' 
    return t
    

def t_COMMENT(t):
    r'\{[^}]*\}'
    pass

def t_NL(t): 
    r'\n+'  
    t.lexer.lineno += 1
    
t_ignore = ' \t'

def t_error(t):
    print(f"erro:: '{t.value[0]}' na linha {t.lineno}") 
    t.lexer.skip(1)

  
lexer = lex.lex(debug=True)