
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCONCATleftUNIONINTERSECTIONDIFFERENCEleftPLUSMINUSleftMULDIVrightUMINUSADD ASSIGN BEGIN BFS CBR COMMA COMPLEMENT CONCAT CONTAIN_EDGES CONTAIN_VERTEX CPAR DIFFERENCE DIGRAPH DIJKSTRA DIV EDGE EDGES_COUNT ELIF ELSE END EQUAL FLOAT FOREDGE FORVERTEX GRAPH GREATER GREATEREQ ID IF IN INT INTERSECTION KRUSKAL K_COLOR_PLOT LESS LESSEQ MINUS MUL MULTIGRAPH NEQUAL NODES_COUNT OBR OPAR PLOT PLUS POINT PRIM PSEUDOGRAPH STRING UNION WEIGHTED_PLOT WEIGHT_SUMInstructions    : Instructions InstructionInstructions    : Instruction Instruction      : Plot_instr\n                        | If_instr\n                        | If_else_instr\n                        | For_vertex_instr\n                        | Assign_instr\n                        | For_edge_instr\n                        | Add_vertex_instr\n                        | Add_edge_instr\n                        | Add_vertex_and_edge_instr\n                        | K_color_plot_instr\n                        | Weighted_plt_instrIf_instr         : IF OPAR logic_expression CPAR BEGIN Instructions ENDIf_else_instr  : IF OPAR logic_expression CPAR BEGIN Instructions END ELSE BEGIN Instructions ENDFor_vertex_instr   : FORVERTEX ID IN ID BEGIN Instructions ENDFor_edge_instr   : FOREDGE ID IN ID BEGIN Instructions ENDPlot_instr   : PLOT OPAR graph_expression CPARAssign_instr     : ID ASSIGN graph_expressionAdd_vertex_instr      : ID ADD OPAR vertex_expression CPARK_color_plot_instr       : K_COLOR_PLOT OPAR graph_expression CPARWeighted_plt_instr       : WEIGHTED_PLOT OPAR graph_expression CPARAdd_edge_instr     : ID ADD OPAR edge_expression CPARAdd_vertex_and_edge_instr      : ID ADD OPAR vertex_expression COMMA edge_expression CPARgraph_expression       : OPAR graph_expression CPARgraph_expression         : KRUSKAL OPAR graph_expression CPAR\n                                | PRIM OPAR graph_expression CPAR\n                                | BFS OPAR graph_expression COMMA value_expression CPAR\n                                | DIJKSTRA OPAR graph_expression COMMA value_expression COMMA value_expression CPARgraph_expression   : GRAPH OPAR value_expression COMMA edge_expression CPAR\n                            | DIGRAPH OPAR value_expression COMMA edge_expression CPAR\n                            | GRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR\n                            | DIGRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR\n                            | graph_expression UNION graph_expression\n                            | graph_expression INTERSECTION graph_expression\n                            | graph_expression DIFFERENCE graph_expression\n                            | graph_expression CONCAT graph_expression\n                            | COMPLEMENT OPAR graph_expression CPAR\n                            | ID\n                            vertex_expression    : vertex_expression INT\n                            | INTedge_expression  : edge_expression OPAR INT COMMA INT CPAR\n                        | OPAR INT COMMA INT CPAR\n                        | edge_expression OPAR INT COMMA INT COMMA INT CPAR\n                        | OPAR INT COMMA INT COMMA INT CPAR\n                        | edge_expression OPAR INT COMMA INT COMMA FLOAT CPAR \n                        | OPAR INT COMMA INT COMMA FLOAT CPAR\n                        | empty\n                        logic_expression     : value_expression EQUAL value_expression\n                            | value_expression GREATER value_expression\n                            | value_expression LESS value_expression\n                            | value_expression GREATEREQ value_expression\n                            | value_expression LESSEQ value_expression\n                            | value_expression NEQUAL value_expression\n                            | logic_functionvalue_expression     : algebraic_expression\n                            | numeric_functionalgebraic_expression      : INT\n                                | FLOATalgebraic_expression       : OPAR algebraic_expression CPARalgebraic_expression       : numeric_functionalgebraic_expression     : algebraic_expression PLUS algebraic_expression\n                                | algebraic_expression MINUS algebraic_expression\n                                | algebraic_expression MUL algebraic_expression\n                                | algebraic_expression DIV algebraic_expression\n                                | MINUS algebraic_expression %prec UMINUS\n                                empty :numeric_function     : graph_expression POINT NODES_COUNT\n                            | graph_expression POINT EDGES_COUNT\n                            | graph_expression POINT WEIGHT_SUMlogic_function       : graph_expression POINT CONTAIN_VERTEX value_expression\n                            | graph_expression POINT CONTAIN_EDGES edge_expression'
    
_lr_action_items = {'PLOT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,39,51,57,93,94,95,96,97,98,99,111,127,129,133,134,135,136,143,144,147,151,158,159,161,163,164,166,168,177,182,183,184,185,190,],[14,14,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-1,-39,-19,-18,-21,-22,-25,-34,-35,-36,-37,14,14,-20,-23,14,-26,-27,-38,14,14,14,-14,-16,-24,-17,-28,-30,-31,14,-29,-32,-33,14,-15,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,39,51,57,93,94,95,96,97,98,99,111,127,129,133,134,135,136,143,144,147,151,158,159,161,163,164,166,168,177,182,183,184,185,190,],[15,15,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-1,-39,-19,-18,-21,-22,-25,-34,-35,-36,-37,15,15,-20,-23,15,-26,-27,-38,15,15,15,-14,-16,-24,-17,-28,-30,-31,15,-29,-32,-33,15,-15,]),'FORVERTEX':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,39,51,57,93,94,95,96,97,98,99,111,127,129,133,134,135,136,143,144,147,151,158,159,161,163,164,166,168,177,182,183,184,185,190,],[16,16,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-1,-39,-19,-18,-21,-22,-25,-34,-35,-36,-37,16,16,-20,-23,16,-26,-27,-38,16,16,16,-14,-16,-24,-17,-28,-30,-31,16,-29,-32,-33,16,-15,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,16,18,21,22,23,25,28,29,30,39,40,49,50,51,53,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,93,94,95,96,97,98,99,111,122,127,129,133,134,135,136,137,138,143,144,147,151,158,159,161,163,164,165,166,168,177,182,183,184,185,190,],[17,17,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,24,27,-1,39,39,39,39,39,39,-39,39,39,86,-19,92,-18,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-21,-22,-25,-34,-35,-36,-37,17,39,17,-20,-23,17,-26,-27,39,39,-38,17,17,17,-14,-16,-24,-17,-28,39,-30,-31,17,-29,-32,-33,17,-15,]),'FOREDGE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,39,51,57,93,94,95,96,97,98,99,111,127,129,133,134,135,136,143,144,147,151,158,159,161,163,164,166,168,177,182,183,184,185,190,],[18,18,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-1,-39,-19,-18,-21,-22,-25,-34,-35,-36,-37,18,18,-20,-23,18,-26,-27,-38,18,18,18,-14,-16,-24,-17,-28,-30,-31,18,-29,-32,-33,18,-15,]),'K_COLOR_PLOT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,39,51,57,93,94,95,96,97,98,99,111,127,129,133,134,135,136,143,144,147,151,158,159,161,163,164,166,168,177,182,183,184,185,190,],[19,19,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-1,-39,-19,-18,-21,-22,-25,-34,-35,-36,-37,19,19,-20,-23,19,-26,-27,-38,19,19,19,-14,-16,-24,-17,-28,-30,-31,19,-29,-32,-33,19,-15,]),'WEIGHTED_PLOT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,21,39,51,57,93,94,95,96,97,98,99,111,127,129,133,134,135,136,143,144,147,151,158,159,161,163,164,166,168,177,182,183,184,185,190,],[20,20,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-1,-39,-19,-18,-21,-22,-25,-34,-35,-36,-37,20,20,-20,-23,20,-26,-27,-38,20,20,20,-14,-16,-24,-17,-28,-30,-31,20,-29,-32,-33,20,-15,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,21,39,51,57,93,94,95,96,97,98,99,129,133,135,136,143,158,159,161,163,164,166,168,182,183,184,190,],[0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-1,-39,-19,-18,-21,-22,-25,-34,-35,-36,-37,-20,-23,-26,-27,-38,-14,-16,-24,-17,-28,-30,-31,-29,-32,-33,-15,]),'END':([2,3,4,5,6,7,8,9,10,11,12,13,21,39,51,57,93,94,95,96,97,98,99,129,133,135,136,143,144,147,151,158,159,161,163,164,166,168,182,183,184,185,190,],[-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-1,-39,-19,-18,-21,-22,-25,-34,-35,-36,-37,-20,-23,-26,-27,-38,158,159,163,-14,-16,-24,-17,-28,-30,-31,-29,-32,-33,190,-15,]),'OPAR':([14,15,19,20,22,23,25,26,28,29,30,32,33,34,35,36,37,38,40,49,52,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,89,91,122,123,130,137,138,139,141,146,149,154,156,165,167,169,172,175,176,181,186,187,191,192,],[22,23,28,29,30,40,30,52,30,30,30,62,63,64,65,66,67,68,40,40,87,30,30,30,30,30,30,30,30,40,40,30,40,40,40,40,40,40,40,40,40,40,132,-48,40,87,87,40,40,87,87,132,132,132,132,40,87,87,-43,132,132,-42,-45,-47,-44,-46,]),'ASSIGN':([17,],[25,]),'ADD':([17,],[26,]),'KRUSKAL':([22,23,25,28,29,30,40,49,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'PRIM':([22,23,25,28,29,30,40,49,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'BFS':([22,23,25,28,29,30,40,49,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'DIJKSTRA':([22,23,25,28,29,30,40,49,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'GRAPH':([22,23,25,28,29,30,40,49,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'DIGRAPH':([22,23,25,28,29,30,40,49,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'COMPLEMENT':([22,23,25,28,29,30,40,49,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'INT':([23,40,49,52,66,67,73,74,75,76,77,78,79,80,81,82,87,88,90,105,107,122,131,132,137,138,140,142,148,162,165,171,180,],[47,47,47,90,47,47,47,47,47,47,47,47,47,47,47,47,128,131,-41,90,90,47,-40,150,47,47,131,131,160,173,47,178,188,]),'FLOAT':([23,40,49,66,67,73,74,75,76,77,78,79,80,81,82,122,137,138,165,171,180,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,179,189,]),'MINUS':([23,40,44,45,47,48,49,66,67,69,71,73,74,75,76,77,78,79,80,81,82,84,109,118,119,120,121,122,124,125,126,137,138,165,],[49,49,80,-61,-58,-59,49,49,49,80,-61,49,49,49,49,49,49,49,49,49,49,-66,-60,-62,-63,-64,-65,49,-68,-69,-70,49,49,49,]),'IN':([24,27,],[50,53,]),'CPAR':([31,39,41,43,44,45,47,48,52,54,55,56,69,70,71,84,88,89,90,91,95,96,97,98,99,100,101,108,109,112,113,114,115,116,117,118,119,120,121,123,124,125,126,130,131,135,136,139,141,143,145,146,149,152,154,156,160,164,166,167,168,169,172,173,174,175,176,178,179,181,182,183,184,186,187,188,189,191,192,],[57,-39,72,-55,-56,-57,-58,-59,-67,93,94,95,109,95,-61,-66,129,133,-41,-48,-25,-34,-35,-36,-37,135,136,143,-60,-49,-50,-51,-52,-53,-54,-62,-63,-64,-65,-67,-68,-69,-70,-67,-40,-26,-27,-67,-67,-38,-71,-72,161,164,166,168,172,-28,-30,-67,-31,-67,-43,181,182,183,184,186,187,-42,-29,-32,-33,-45,-47,191,192,-44,-46,]),'UNION':([31,39,46,51,54,55,56,70,85,95,96,97,98,99,100,101,102,103,108,135,136,143,164,166,168,182,183,184,],[58,-39,58,58,58,58,58,58,58,-25,-34,-35,-36,58,58,58,58,58,58,-26,-27,-38,-28,-30,-31,-29,-32,-33,]),'INTERSECTION':([31,39,46,51,54,55,56,70,85,95,96,97,98,99,100,101,102,103,108,135,136,143,164,166,168,182,183,184,],[59,-39,59,59,59,59,59,59,59,-25,-34,-35,-36,59,59,59,59,59,59,-26,-27,-38,-28,-30,-31,-29,-32,-33,]),'DIFFERENCE':([31,39,46,51,54,55,56,70,85,95,96,97,98,99,100,101,102,103,108,135,136,143,164,166,168,182,183,184,],[60,-39,60,60,60,60,60,60,60,-25,-34,-35,-36,60,60,60,60,60,60,-26,-27,-38,-28,-30,-31,-29,-32,-33,]),'CONCAT':([31,39,46,51,54,55,56,70,85,95,96,97,98,99,100,101,102,103,108,135,136,143,164,166,168,182,183,184,],[61,-39,61,61,61,61,61,61,61,-25,-34,-35,-36,-37,61,61,61,61,61,-26,-27,-38,-28,-30,-31,-29,-32,-33,]),'POINT':([39,46,70,85,95,96,97,98,99,135,136,143,164,166,168,182,183,184,],[-39,83,110,110,-25,-34,-35,-36,-37,-26,-27,-38,-28,-30,-31,-29,-32,-33,]),'COMMA':([39,44,45,47,48,71,84,88,90,95,96,97,98,99,102,103,104,106,109,118,119,120,121,124,125,126,128,131,135,136,143,150,153,155,157,160,164,166,168,173,182,183,184,],[-39,-56,-57,-58,-59,-61,-66,130,-41,-25,-34,-35,-36,-37,137,138,139,141,-60,-62,-63,-64,-65,-68,-69,-70,148,-40,-26,-27,-38,162,165,167,169,171,-28,-30,-31,180,-29,-32,-33,]),'EQUAL':([42,44,45,47,48,71,84,109,118,119,120,121,124,125,126,],[73,-56,-57,-58,-59,-61,-66,-60,-62,-63,-64,-65,-68,-69,-70,]),'GREATER':([42,44,45,47,48,71,84,109,118,119,120,121,124,125,126,],[74,-56,-57,-58,-59,-61,-66,-60,-62,-63,-64,-65,-68,-69,-70,]),'LESS':([42,44,45,47,48,71,84,109,118,119,120,121,124,125,126,],[75,-56,-57,-58,-59,-61,-66,-60,-62,-63,-64,-65,-68,-69,-70,]),'GREATEREQ':([42,44,45,47,48,71,84,109,118,119,120,121,124,125,126,],[76,-56,-57,-58,-59,-61,-66,-60,-62,-63,-64,-65,-68,-69,-70,]),'LESSEQ':([42,44,45,47,48,71,84,109,118,119,120,121,124,125,126,],[77,-56,-57,-58,-59,-61,-66,-60,-62,-63,-64,-65,-68,-69,-70,]),'NEQUAL':([42,44,45,47,48,71,84,109,118,119,120,121,124,125,126,],[78,-56,-57,-58,-59,-61,-66,-60,-62,-63,-64,-65,-68,-69,-70,]),'PLUS':([44,45,47,48,69,71,84,109,118,119,120,121,124,125,126,],[79,-61,-58,-59,79,-61,-66,-60,-62,-63,-64,-65,-68,-69,-70,]),'MUL':([44,45,47,48,69,71,84,109,118,119,120,121,124,125,126,],[81,-61,-58,-59,81,-61,-66,-60,81,81,-64,-65,-68,-69,-70,]),'DIV':([44,45,47,48,69,71,84,109,118,119,120,121,124,125,126,],[82,-61,-58,-59,82,-61,-66,-60,82,82,-64,-65,-68,-69,-70,]),'OBR':([66,67,],[105,107,]),'BEGIN':([72,86,92,170,],[111,127,134,177,]),'CONTAIN_VERTEX':([83,],[122,]),'CONTAIN_EDGES':([83,],[123,]),'NODES_COUNT':([83,110,],[124,124,]),'EDGES_COUNT':([83,110,],[125,125,]),'WEIGHT_SUM':([83,110,],[126,126,]),'CBR':([90,131,140,142,],[-41,-40,155,157,]),'ELSE':([158,],[170,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Instructions':([0,111,127,134,177,],[1,144,147,151,185,]),'Instruction':([0,1,111,127,134,144,147,151,177,185,],[2,21,2,2,2,21,21,21,2,21,]),'Plot_instr':([0,1,111,127,134,144,147,151,177,185,],[3,3,3,3,3,3,3,3,3,3,]),'If_instr':([0,1,111,127,134,144,147,151,177,185,],[4,4,4,4,4,4,4,4,4,4,]),'If_else_instr':([0,1,111,127,134,144,147,151,177,185,],[5,5,5,5,5,5,5,5,5,5,]),'For_vertex_instr':([0,1,111,127,134,144,147,151,177,185,],[6,6,6,6,6,6,6,6,6,6,]),'Assign_instr':([0,1,111,127,134,144,147,151,177,185,],[7,7,7,7,7,7,7,7,7,7,]),'For_edge_instr':([0,1,111,127,134,144,147,151,177,185,],[8,8,8,8,8,8,8,8,8,8,]),'Add_vertex_instr':([0,1,111,127,134,144,147,151,177,185,],[9,9,9,9,9,9,9,9,9,9,]),'Add_edge_instr':([0,1,111,127,134,144,147,151,177,185,],[10,10,10,10,10,10,10,10,10,10,]),'Add_vertex_and_edge_instr':([0,1,111,127,134,144,147,151,177,185,],[11,11,11,11,11,11,11,11,11,11,]),'K_color_plot_instr':([0,1,111,127,134,144,147,151,177,185,],[12,12,12,12,12,12,12,12,12,12,]),'Weighted_plt_instr':([0,1,111,127,134,144,147,151,177,185,],[13,13,13,13,13,13,13,13,13,13,]),'graph_expression':([22,23,25,28,29,30,40,49,58,59,60,61,62,63,64,65,66,67,68,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[31,46,51,54,55,56,70,85,96,97,98,99,100,101,102,103,85,85,108,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'logic_expression':([23,],[41,]),'value_expression':([23,66,67,73,74,75,76,77,78,122,137,138,165,],[42,104,106,112,113,114,115,116,117,145,152,153,174,]),'logic_function':([23,],[43,]),'algebraic_expression':([23,40,49,66,67,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[44,69,84,44,44,44,44,44,44,44,44,118,119,120,121,44,44,44,44,]),'numeric_function':([23,40,49,66,67,73,74,75,76,77,78,79,80,81,82,122,137,138,165,],[45,71,71,45,45,45,45,45,45,45,45,71,71,71,71,45,45,45,45,]),'vertex_expression':([52,105,107,],[88,140,142,]),'edge_expression':([52,123,130,139,141,167,169,],[89,146,149,154,156,175,176,]),'empty':([52,123,130,139,141,167,169,],[91,91,91,91,91,91,91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Instructions","S'",1,None,None,None),
  ('Instructions -> Instructions Instruction','Instructions',2,'p_instructions_list','parser_rules.py',17),
  ('Instructions -> Instruction','Instructions',1,'p_instructions_instruction','parser_rules.py',23),
  ('Instruction -> Plot_instr','Instruction',1,'p_instruction','parser_rules.py',28),
  ('Instruction -> If_instr','Instruction',1,'p_instruction','parser_rules.py',29),
  ('Instruction -> If_else_instr','Instruction',1,'p_instruction','parser_rules.py',30),
  ('Instruction -> For_vertex_instr','Instruction',1,'p_instruction','parser_rules.py',31),
  ('Instruction -> Assign_instr','Instruction',1,'p_instruction','parser_rules.py',32),
  ('Instruction -> For_edge_instr','Instruction',1,'p_instruction','parser_rules.py',33),
  ('Instruction -> Add_vertex_instr','Instruction',1,'p_instruction','parser_rules.py',34),
  ('Instruction -> Add_edge_instr','Instruction',1,'p_instruction','parser_rules.py',35),
  ('Instruction -> Add_vertex_and_edge_instr','Instruction',1,'p_instruction','parser_rules.py',36),
  ('Instruction -> K_color_plot_instr','Instruction',1,'p_instruction','parser_rules.py',37),
  ('Instruction -> Weighted_plt_instr','Instruction',1,'p_instruction','parser_rules.py',38),
  ('If_instr -> IF OPAR logic_expression CPAR BEGIN Instructions END','If_instr',7,'p_if_instr','parser_rules.py',44),
  ('If_else_instr -> IF OPAR logic_expression CPAR BEGIN Instructions END ELSE BEGIN Instructions END','If_else_instr',11,'p_if_else_instr','parser_rules.py',49),
  ('For_vertex_instr -> FORVERTEX ID IN ID BEGIN Instructions END','For_vertex_instr',7,'p_for_vertex_instr','parser_rules.py',54),
  ('For_edge_instr -> FOREDGE ID IN ID BEGIN Instructions END','For_edge_instr',7,'p_for_edge_instr','parser_rules.py',59),
  ('Plot_instr -> PLOT OPAR graph_expression CPAR','Plot_instr',4,'p_plot_instr','parser_rules.py',65),
  ('Assign_instr -> ID ASSIGN graph_expression','Assign_instr',3,'p_assign_instr','parser_rules.py',71),
  ('Add_vertex_instr -> ID ADD OPAR vertex_expression CPAR','Add_vertex_instr',5,'p_add_vertex_instr','parser_rules.py',77),
  ('K_color_plot_instr -> K_COLOR_PLOT OPAR graph_expression CPAR','K_color_plot_instr',4,'p_k_color_plot_instr','parser_rules.py',83),
  ('Weighted_plt_instr -> WEIGHTED_PLOT OPAR graph_expression CPAR','Weighted_plt_instr',4,'p_weighted_plot_instr','parser_rules.py',89),
  ('Add_edge_instr -> ID ADD OPAR edge_expression CPAR','Add_edge_instr',5,'p_add_edge_instr','parser_rules.py',94),
  ('Add_vertex_and_edge_instr -> ID ADD OPAR vertex_expression COMMA edge_expression CPAR','Add_vertex_and_edge_instr',7,'p_add_vertex_and_edge_instr','parser_rules.py',99),
  ('graph_expression -> OPAR graph_expression CPAR','graph_expression',3,'p_graph_expression_grouping','parser_rules.py',105),
  ('graph_expression -> KRUSKAL OPAR graph_expression CPAR','graph_expression',4,'p_graph_expression_algorithm','parser_rules.py',110),
  ('graph_expression -> PRIM OPAR graph_expression CPAR','graph_expression',4,'p_graph_expression_algorithm','parser_rules.py',111),
  ('graph_expression -> BFS OPAR graph_expression COMMA value_expression CPAR','graph_expression',6,'p_graph_expression_algorithm','parser_rules.py',112),
  ('graph_expression -> DIJKSTRA OPAR graph_expression COMMA value_expression COMMA value_expression CPAR','graph_expression',8,'p_graph_expression_algorithm','parser_rules.py',113),
  ('graph_expression -> GRAPH OPAR value_expression COMMA edge_expression CPAR','graph_expression',6,'p_graph_expression','parser_rules.py',124),
  ('graph_expression -> DIGRAPH OPAR value_expression COMMA edge_expression CPAR','graph_expression',6,'p_graph_expression','parser_rules.py',125),
  ('graph_expression -> GRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR','graph_expression',8,'p_graph_expression','parser_rules.py',126),
  ('graph_expression -> DIGRAPH OPAR OBR vertex_expression CBR COMMA edge_expression CPAR','graph_expression',8,'p_graph_expression','parser_rules.py',127),
  ('graph_expression -> graph_expression UNION graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',128),
  ('graph_expression -> graph_expression INTERSECTION graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',129),
  ('graph_expression -> graph_expression DIFFERENCE graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',130),
  ('graph_expression -> graph_expression CONCAT graph_expression','graph_expression',3,'p_graph_expression','parser_rules.py',131),
  ('graph_expression -> COMPLEMENT OPAR graph_expression CPAR','graph_expression',4,'p_graph_expression','parser_rules.py',132),
  ('graph_expression -> ID','graph_expression',1,'p_graph_expression','parser_rules.py',133),
  ('vertex_expression -> vertex_expression INT','vertex_expression',2,'p_vertex_expression','parser_rules.py',151),
  ('vertex_expression -> INT','vertex_expression',1,'p_vertex_expression','parser_rules.py',152),
  ('edge_expression -> edge_expression OPAR INT COMMA INT CPAR','edge_expression',6,'p_edge_expression','parser_rules.py',160),
  ('edge_expression -> OPAR INT COMMA INT CPAR','edge_expression',5,'p_edge_expression','parser_rules.py',161),
  ('edge_expression -> edge_expression OPAR INT COMMA INT COMMA INT CPAR','edge_expression',8,'p_edge_expression','parser_rules.py',162),
  ('edge_expression -> OPAR INT COMMA INT COMMA INT CPAR','edge_expression',7,'p_edge_expression','parser_rules.py',163),
  ('edge_expression -> edge_expression OPAR INT COMMA INT COMMA FLOAT CPAR','edge_expression',8,'p_edge_expression','parser_rules.py',164),
  ('edge_expression -> OPAR INT COMMA INT COMMA FLOAT CPAR','edge_expression',7,'p_edge_expression','parser_rules.py',165),
  ('edge_expression -> empty','edge_expression',1,'p_edge_expression','parser_rules.py',166),
  ('logic_expression -> value_expression EQUAL value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',182),
  ('logic_expression -> value_expression GREATER value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',183),
  ('logic_expression -> value_expression LESS value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',184),
  ('logic_expression -> value_expression GREATEREQ value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',185),
  ('logic_expression -> value_expression LESSEQ value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',186),
  ('logic_expression -> value_expression NEQUAL value_expression','logic_expression',3,'p_logic_expression','parser_rules.py',187),
  ('logic_expression -> logic_function','logic_expression',1,'p_logic_expression','parser_rules.py',188),
  ('value_expression -> algebraic_expression','value_expression',1,'p_value_expression','parser_rules.py',196),
  ('value_expression -> numeric_function','value_expression',1,'p_value_expression','parser_rules.py',197),
  ('algebraic_expression -> INT','algebraic_expression',1,'p_algebraic_expression_number','parser_rules.py',203),
  ('algebraic_expression -> FLOAT','algebraic_expression',1,'p_algebraic_expression_number','parser_rules.py',204),
  ('algebraic_expression -> OPAR algebraic_expression CPAR','algebraic_expression',3,'p_algebraic_expression_grouping','parser_rules.py',209),
  ('algebraic_expression -> numeric_function','algebraic_expression',1,'p_algebraic_expression_function','parser_rules.py',214),
  ('algebraic_expression -> algebraic_expression PLUS algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',220),
  ('algebraic_expression -> algebraic_expression MINUS algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',221),
  ('algebraic_expression -> algebraic_expression MUL algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',222),
  ('algebraic_expression -> algebraic_expression DIV algebraic_expression','algebraic_expression',3,'p_algebraic_expression','parser_rules.py',223),
  ('algebraic_expression -> MINUS algebraic_expression','algebraic_expression',2,'p_algebraic_expression','parser_rules.py',224),
  ('empty -> <empty>','empty',0,'p_empty','parser_rules.py',233),
  ('numeric_function -> graph_expression POINT NODES_COUNT','numeric_function',3,'p_numeric_functions','parser_rules.py',237),
  ('numeric_function -> graph_expression POINT EDGES_COUNT','numeric_function',3,'p_numeric_functions','parser_rules.py',238),
  ('numeric_function -> graph_expression POINT WEIGHT_SUM','numeric_function',3,'p_numeric_functions','parser_rules.py',239),
  ('logic_function -> graph_expression POINT CONTAIN_VERTEX value_expression','logic_function',4,'p_logic_functions','parser_rules.py',245),
  ('logic_function -> graph_expression POINT CONTAIN_EDGES edge_expression','logic_function',4,'p_logic_functions','parser_rules.py',246),
]
