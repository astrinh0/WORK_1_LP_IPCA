import ply.lex as lex
from utils import slurp

tokens = ("NUMBEROFTESTS", "OK", "NOTOK", "NROFSUBTESTS", "NROFSUBSUBTESTS", "OKSUB", "OKSUBSUB", "NOTOKSUB", "NOTOKSUBSUB", "COMMENTS")

t_NUMBEROFTESTS = r"1\.\.[0-9]+\n"

t_NROFSUBTESTS = r"[ ]+1\.\.[0-9]+\n"

t_NROFSUBSUBTESTS = r"[ ]+1\.\.[0-9]+\n"

t_OK = r"ok[ ][0-9]+([ ]-[ ][\w ]+\n|\n|[ ][#].*\n)"

t_OKSUB = r"[ ][ ][ ][ ]ok[ ][0-9]+([ ]-[ ][\w ]+\n|\n|[ ][#].*\n)"

t_OKSUBSUB = r"[ ][ ][ ][ ][ ][ ][ ][ ]ok[ ][0-9]+([ ]-[ ][\w ]+\n|\n|[ ][#].*\n)"

t_NOTOK = r"not[ ]ok[ ][0-9]+([ ]-[ ][\w ]+\n|\n|[ ][#].*\n)"

t_NOTOKSUB = r"[ ][ ][ ][ ]not[ ]ok[ ][0-9]+([ ]-[ ][\w ]+\n|\n|[ ][#].*\n)"

t_NOTOKSUBSUB = r"[ ][ ][ ][ ][ ][ ][ ][ ]not[ ]ok[ ][0-9]+([ ]-[ ][\w ]+\n|\n|[ ][#].*\n)"

t_COMMENTS = r"[ ]+[#].*\n|([#].*\n)"







def t_error(t):
    print("error [%s]" % t.value)
    exit(1)

lexer = lex.lex()
lexer.input(slurp("teste3.t"))
for token in iter(lexer.token, None):
    print(token)
