from lexer_rules import tokens
from ast_nodes import *

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV')
    )


# def p_init(t) :
#     'Init            : Instructions'
#     t[0] = t[1]


def p_instructions_list(t) :
    'Instructions    : Instructions Instruction'
    t[1].append(t[2])
    t[0] = t[1]


def p_instructions_instruction(t) :
    'Instructions    : Instruccion '
    t[0] = [t[1]]


def p_instruction(t) :
    '''Instruction      : Plot_instr
                        | Assign_instr
                        | Forvertex_instr
                        | Foredge_instr
                        | If_instr
                        | If_else_instr'''
    t[0] = t[1]


def p_Plot_instr(t):
    'Plot_instr    : PLOT OPAR ID CPAR'
    t[0] = Plot(t[3])


def p_assign_instr(t) :
    '''Assign_instr     : ID EQUAL GRAPH OPAR INT COMMA edges_expression CPAR  
                        | ID EQUAL DIGRAPH OPAR INT COMMA edges_expression CPAR
                        | ID EQUAL MULTIGRAPH OPAR INT COMMA edges_expression CPAR
                        | ID EQUAL PSEUDOGRAPH OPAR INT COMMA edges_expression CPAR                     
                    '''
    t[0] = Assign(t[1], t[3], t[5], t[7])
