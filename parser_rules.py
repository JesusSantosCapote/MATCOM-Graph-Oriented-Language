from lexer_rules import tokens
from ast_nodes import *
from ply import yacc

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV')
    )

def p_instructions_list(t) :
    'Instructions    : Instructions Instruction'
    t[1].append(t[2])
    t[0] = Instructions(t[1])


def p_instructions_instruction(t) :
    'Instructions    : Instruction '
    t[0] = Instructions([t[1]])


def p_instruction(t) :
    '''Instruction      : Plot_instr
                        | Assign_instr'''
    t[0] = t[1]


def p_Plot_instr(t):
    'Plot_instr    : PLOT OPAR ID CPAR'
    t[0] = Plot(t[3])


def p_assign_instr(t) :
    '''Assign_instr     : ID ASSIGN GRAPH OPAR INT COMMA edge_expression CPAR  
                        | ID ASSIGN DIGRAPH OPAR INT COMMA edge_expression CPAR
                        | ID ASSIGN MULTIGRAPH OPAR INT COMMA edge_expression CPAR
                        | ID ASSIGN PSEUDOGRAPH OPAR INT COMMA edge_expression CPAR                     
                    '''
    t[0] = Assign(t[1], t[3], t[5], t[7])

def p_edge_expression(t) :
    '''edge_expression  : edge_expression OPAR INT COMMA INT CPAR
                        | OPAR INT COMMA INT CPAR
                        | edge_expression OPAR INT COMMA INT COMMA INT CPAR
                        | OPAR INT COMMA INT COMMA INT CPAR
                        | edge_expression OPAR INT COMMA INT COMMA FLOAT CPAR 
                        | OPAR INT COMMA INT COMMA FLOAT CPAR
                        '''
    if len(t) == 7:
        print("ENTRE EN 1")
        t[1].append((t[3], t[5], 0))
        t[0] = t[1]
    elif len(t) == 6:
        print("ENTRE EN 2")
        t[0] = [(t[2], t[4], 0)]
    elif len(t) == 9:
        print("ENTRE EN 3")
        t[1].append((t[3], t[5], t[7]))
        t[0] =t[1]
    else:
        print("ENTRE EN 4")
        t[0] = [(t[2], t[4], t[6])]
    print(t[0])

parser = yacc.yacc(debug=True)
