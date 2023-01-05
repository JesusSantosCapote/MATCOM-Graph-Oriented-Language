from lexer_rules import tokens
from ast_nodes import *
from ply import yacc
from Tools import Bool_Operations, Arithmetic_Operations


precedence = (
    ('left', 'CONCAT'),
    ('left', 'UNION', 'INTERSECTION', 'DIFFERENCE'),
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV'),
    ('right','UMINUS'),
    )

def p_instructions_list(t) :
    'Instructions    : Instructions Instruction'
    t[1].node_list.append(t[2])
    t[0] = Instructions(t[1].node_list)


def p_instructions_instruction(t) :
    'Instructions    : Instruction '
    t[0] = Instructions([t[1]])


def p_instruction(t) :
    '''Instruction      : Plot_instr
                        | If_instr
                        | If_else_instr
                        | For_vertex_instr
                        | Assign_instr
                        | For_edge_instr
                        | Add_vertex_instr
                        | Add_edge_instr
                        | Add_vertex_and_edge_instr
                        | K_color_plot_instr
                        | Weighted_plt_instr'''
                        
    t[0] = t[1]


def p_if_instr(t):
    'If_instr         : IF OPAR logic_expression CPAR BEGIN Instructions END'
    t[0] = If(t[3], t[6])


def p_if_else_instr(t):
    'If_else_instr  : IF OPAR logic_expression CPAR BEGIN Instructions END ELSE BEGIN Instructions END'
    t[0] = If_else(t[3], t[6], t[10])


def p_for_vertex_instr(t):
    'For_vertex_instr   : FORVERTEX ID IN ID BEGIN Instructions END'
    t[0] = For_vertex(t[2], t[4], t[6], t.lineno(2))


def p_for_edge_instr(t):
    'For_edge_instr   : FOREDGE ID IN ID BEGIN Instructions END'
    t[0] = For_edge(t[2], t[4], t[6], t.lineno(2))



def p_plot_instr(t):
    'Plot_instr   : PLOT OPAR graph_expression CPAR'
    
    t[0] = Plot(t[3], t.lineno(1))


def p_assign_instr(t) :
    '''Assign_instr     : ID ASSIGN graph_expression'''

    t[0] = Assign(t[1], t[3])


def  p_add_vertex_instr(t) :
    'Add_vertex_instr      : ID ADD OPAR vertex_expression CPAR'

    t[0] = Add_vertex(t[1], t[4], t.lineno(2))


def p_k_color_plot_instr(t) :
    '''K_color_plot_instr       : K_COLOR_PLOT OPAR graph_expression CPAR'''

    t[0]= K_color_plot(t[3], t.lineno(1))


def p_weighted_plot_instr(t) :
    '''Weighted_plt_instr       : WEIGHTED_PLOT OPAR graph_expression CPAR''' 

    t[0] = Weighted_plot(t[3], t.lineno(1))
    
def p_add_edge_instr(t) :  
    'Add_edge_instr     : ID ADD OPAR edge_expression CPAR'

    t[0] = Add_edge(t[1], t[4], t.lineno(2))

def p_add_vertex_and_edge_instr(t) :
    'Add_vertex_and_edge_instr      : ID ADD OPAR vertex_expression COMMA edge_expression CPAR'

    t[0] = Add_vertex_and_edge(t[1], t[4], t[6], t.lineno(2))


def p_graph_expression_grouping(t):
    'graph_expression       : OPAR graph_expression CPAR'

    t[0] = t[2]

def p_graph_expression_algorithm(t):
    '''graph_expression         : KRUSKAL OPAR graph_expression CPAR
                                | PRIM OPAR graph_expression CPAR
                                | BFS OPAR graph_expression COMMA value_expression CPAR
                                | DIJKSTRA OPAR graph_expression COMMA value_expression COMMA value_expression CPAR'''
    if len(t) == 5:
        t[0] = MST(t[3], t[1], t.lineno(1))
    
    elif len(t) == 7:
        t[0] = BFS(t[3], t[5])
    
    else:
        t[0] = Dijkstra(t[3], t[5], t[7])
    
def p_graph_expression(t) :
    '''graph_expression   : GRAPH OPAR value_expression COMMA edge_expression CPAR
                            | DIGRAPH OPAR value_expression COMMA edge_expression CPAR
                            | GRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR
                            | DIGRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR
                            | graph_expression UNION graph_expression
                            | graph_expression INTERSECTION graph_expression
                            | graph_expression DIFFERENCE graph_expression
                            | graph_expression CONCAT graph_expression
                            | COMPLEMENT OPAR graph_expression CPAR
                            | ID
                            '''
    if len(t) == 5:
        t[0] = Unary_graph_operation(t[3], t[1])

    if len(t) == 7:
        t[0] = Create_graph(t[1], t[3], t[5], t.lineno(1))
    
    if len(t) == 9:
        t[0] = Create_graph_with_vertex(t[1], t[4], t[7], t.lineno(1))

    if len(t) == 4:
        t[0] = Binary_graph_operation(t[1], t[3], t[2], t.lineno(2))

    if len(t) == 2: 
        t[0] = Create_Graph_With_Variable(t[1], t.lineno(1))

def p_vertex_expression(t) :
    '''vertex_expression    : vertex_expression INT
                            | INT'''                            
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_edge_expression(t) :
    '''edge_expression  : edge_expression OPAR INT COMMA INT CPAR
                        | OPAR INT COMMA INT CPAR
                        | edge_expression OPAR INT COMMA INT COMMA INT CPAR
                        | OPAR INT COMMA INT COMMA INT CPAR
                        | edge_expression OPAR INT COMMA INT COMMA FLOAT CPAR 
                        | OPAR INT COMMA INT COMMA FLOAT CPAR
                        | empty
                        '''
    if len(t) == 7:
        t[1].append((t[3], t[5], 0))
        t[0] = t[1]
    elif len(t) == 6:
        t[0] = [(t[2], t[4], 0)]
    elif len(t) == 9:
        t[1].append((t[3], t[5], t[7]))
        t[0] =t[1]
    elif len(t) == 2:
        t[0] = []
    else:
        t[0] = [(t[2], t[4], t[6])]

def p_logic_expression(t):
    '''logic_expression     : value_expression EQUAL value_expression
                            | value_expression GREATER value_expression
                            | value_expression LESS value_expression
                            | value_expression GREATEREQ value_expression
                            | value_expression LESSEQ value_expression
                            | value_expression NEQUAL value_expression
                            | logic_function'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = Bool_Operation(t[1], t[3], t[2])
    

def p_value_expression(t):
    '''value_expression     : algebraic_expression
                            | numeric_function'''

    t[0] = t[1]


def p_algebraic_expression_number(t):
    '''algebraic_expression      : INT
                                | FLOAT'''
    t[0] = Numerical_value(t[1])


def p_algebraic_expression_grouping(t):
    'algebraic_expression       : OPAR algebraic_expression CPAR'

    t[0] = t[2]

def p_algebraic_expression_function(t):
    'algebraic_expression       : numeric_function'

    t[0] = Solve(t[1])


def p_algebraic_expression(t):
    '''algebraic_expression     : algebraic_expression PLUS algebraic_expression
                                | algebraic_expression MINUS algebraic_expression
                                | algebraic_expression MUL algebraic_expression
                                | algebraic_expression DIV algebraic_expression
                                | MINUS algebraic_expression %prec UMINUS
                                '''

    if len(t) == 4:
        t[0] = Algebraic_expression(t[1], t[3], t[2])
    else:
        t[0] = Minus_operation(t[2])

def p_empty(p):
    'empty :'
    pass

def p_numeric_functions(t):
    '''numeric_function     : graph_expression POINT NODES_COUNT
                            | graph_expression POINT EDGES_COUNT
                            | graph_expression POINT WEIGHT_SUM'''

    t[0] = Unary_function(t[1], t[3], t.lineno(3))


def p_logic_functions(t):
    '''logic_function       : graph_expression POINT CONTAIN_VERTEX value_expression
                            | graph_expression POINT CONTAIN_EDGES edge_expression'''
    if t[3] == 'contain_vertex':
        t[0] = Contain_vertex(t[1], t[4])
    else:
        t[0] = Contain_edges(t[1], t[4])


def p_error(t):
    if t:
          print("Syntax error at token", t.value, "at line", t.lineno)
          # Just discard the token and tell the parser it's okay.
          parser.errok()
    else:
          print("Syntax error at EOF")

parser = yacc.yacc(debug=True)
