# calclex.py
from sly import Lexer
import sys

class CalcLexer(Lexer):
    # Set of token names. This is always required 
    tokens = { ID, NUMBER, PLUS, MINUS, TIMES,
               DIVIDE, ASSIGN, LPAREN, RPAREN }
    
    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_comment = r'\/\* .* \*\\'
    
    # Regular expression rules for tokens
    # Átomos que representam palavras reservdadas da linguagem

    # Átomos que representam símbolos da linguagem
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
    # Átomos com regras de formação complexa
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'

    def error (self, t):
        print("Linha: %d - Caractere ilegal: %s" % (t.lineno, t.value))
        self.index += 1

if __name__ == '__main__':
    if (len(sys.argv) != 2 ):
        print("Execute: python3 lexico.py <nome_do_arquivo>")
    else:
        try:
            arq = open(sys.argv[1], "r")
            data = arq.read() 
            arq.close()
            lexer = CalcLexer()
            for tok in lexer.tokenize(data):
                print('[ %r, %r, %r ]' % (tok.lineno, tok.type, tok.value))
        except:
            print("Arquivo nao existe!")
            
