# Analisador Léxico
Código em Python do Analisador Léxico para a identificação dos átomos da linguagem MiniJava.

# Para usar sly 
Requer Python 3.6 ou mais recente.

Comando para baixar sly:

$ pip3 install sly

# Para executar no terminal

$ python3 lexico.py <nome_do_arquivo>

Exemplo: python3 lexico.py teste.txt

# Questões Léxicas

## Identificadores:
Um identificador é uma sequência de letras, dígitos e sublinhados, começando com uma letra. As letras maiúsculas são diferenciadas das minúsculas. Neste manual de referência, o símbolo id representa um identificador.

## Literais inteiros:
Uma sequência de dígitos decimais é uma constante inteira que denota o valor inteiro correspondente. Nesta especificação, o símbolo INTEGER_LITERAL representa uma constante inteira.

## Operadores binários:
Um operador binário representa um dos seguintes símbolos:

&&     <     +     -     *

Neste documento de referência, o símbolo op representa um operador binário.

## Comentários:
Um comentário pode aparecer entre dois tokens quaisquer da linguagem. Existem duas formas de representar comentários:

-um começa com /* termina com */ e pode ser aninhado;

-outro começa com // e vai até o final da linha.




