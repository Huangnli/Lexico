# calclex.py
from sly import Lexer
import sys

class CalcLexer(Lexer):
    # Set of token names. This is always required 
    tokens = { ID, NUM, PLUS, MINUS, TIMES, DIVIDE, EQUAL, 
               LPAREN, RPAREN, LBRACK, RBRACK, LBRACE, RBRACE, 
               SCOLON, COLON, AND, LESS, DOT, NOT, KEYWORD, PRINT}
    
    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_EOF  = 'EOF'
    ignore_comment = r'//.*'

    @_(r'/\*(.|\n)*\*/') # ignora comentario /* */
    def ignore_comment2(self, t):
        for i in t.value:
            if i == '\n':
                self.lineno += 1

    # Regular expression rules for tokens
    # Átomos que representam símbolos da linguagem
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQUAL   = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACK  = r'\[' 
    RBRACK  = r'\]'
    LBRACE  = r'{'
    RBRACE  = r'}'
    SCOLON  = r';'
    COLON   = r','
    AND     = r'&&'
    LESS    = r'<'
    DOT     = r'\.'
    NOT     = r'!'
    # Átomos com regras de formação complexa e keywords
    PRINT = r'System\.out\.println'
    PRINT['System.out.println'] = KEYWORD
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['class']              = KEYWORD
    ID['String']             = KEYWORD
    ID['public']             = KEYWORD
    ID['static']             = KEYWORD
    ID['void']               = KEYWORD
    ID['main']               = KEYWORD
    ID['extends']            = KEYWORD
    ID['return']             = KEYWORD
    ID['boolean']            = KEYWORD
    ID['int']                = KEYWORD
    ID['if']                 = KEYWORD
    ID['else']               = KEYWORD
    ID['while']              = KEYWORD
    ID['true']               = KEYWORD
    ID['false']              = KEYWORD
    ID['this']               = KEYWORD
    ID['new']                = KEYWORD
    ID['length']             = KEYWORD
    NUM = r'\d+'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error (self, t):
        print("Linha: %d - Caractere ilegal: %s" % (t.lineno, t.value[0]))
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