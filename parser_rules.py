from lexer_rules import tokens
from ast_nodes import *
from ply import yacc
from Tools import Bool_Operations, Arithmetic_Operations

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV'),
    ('right','UMINUS'),
    )

def p_instructions_list(t) :
    'Instructions    : Instructions Instruction'
    print('Entro en 1')
    t[1].node_list.append(t[2])
    t[0] = Instructions(t[1].node_list)


def p_instructions_instruction(t) :
    'Instructions    : Instruction '
    print('Entre en 2')
    t[0] = Instructions([t[1]])


def p_instruction(t) : #TODO: Put some more Instructions here
    '''Instruction      : Plot_instr
                        | If_instr
                        | Assign_instr'''
                        
    t[0] = t[1]


def p_if_instr(t):
    'IF_instr         : IF OPAR logic_expression CPAR BEGIN Instructions END'
    t[0] = If(t[3], t[6])


def p_Plot_instr(t):
    'Plot_instr    : PLOT OPAR ID CPAR'
    t[0] = Plot(t[3], t.lineno(1))


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
        t[1].append((t[3], t[5], 0))
        t[0] = t[1]
    elif len(t) == 6:
        t[0] = [(t[2], t[4], 0)]
    elif len(t) == 9:
        t[1].append((t[3], t[5], t[7]))
        t[0] =t[1]
    else:
        t[0] = [(t[2], t[4], t[6])]

def p_logic_expression(t):
    '''logic_expression     :value_expression EQUAL value_expression
                            |value_expression GREATER value_expression
                            |value_expression LESS value_expression
                            |value_expression GREATEREQ value_expression
                            |value_expression LESSEQ value_expression
                            |value_expression NEQUAL value_expression'''
    t[0] = Bool_Operations[t[2]](t[1],t[3])

def p_value_expression(t):
    '''value_expression     :algebraic_expression
                            |function'''
    t[0] = t[1]


def p_algebraic_expression(t):
    '''algebraic_expression     :INT
                                |FLOAT
                                |algebraic_expression PLUS algebraic_expression
                                |algebraic_expression MINUS algebraic_expression
                                |algebraic_expression MUL algebraic_expression
                                |algebraic_expression DIV algebraic_expression
                                |MINUS algebraic_expression %prec UMINUS
                                '''
    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 4:
        t[0] = Arithmetic_Operations[t[2]](t[1],t[3])
    else:
        t[0] = -t[2]


def p_function(t):
    '''function     : '''
parser = yacc.yacc(debug=True)
