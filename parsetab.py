
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOLEAN CHAR CLOSE_BRACES CLOSE_BRACKETS CLOSE_PAREN COMMA CT_CHAR CT_FLOAT CT_INT CT_STRING DIVIDE DO ELSE EQUALS FLOAT FOR ID IF INT LESS_THAN MAIN MINUS MODULE MORE_THAN MULTIPLIES NOT_EQUALS OPEN_BRACES OPEN_BRACKETS OPEN_PAREN OR PLUS PROGRAM READ RETURN SEMICOLON THEN TO VARS VOID WHILE WRITEprogram : PROGRAM ID SEMICOLON vars funcs mainmain : MAIN OPEN_PAREN CLOSE_PAREN blockfuncs : func_type MODULE ID OPEN_PAREN var_type ID CLOSE_PAREN vars block\n    | empty\n    funcs_comp : ID OPEN_PAREN var_type ID CLOSE_PAREN vars block\n    block : OPEN_BRACES statements CLOSE_BRACESfunc_type : var_type\n    | VOID\n    var_type : INT\n    | FLOAT\n    | CHAR\n    vars : VARS var_comp\n    | empty\n    var_comp : var_type ids var_comp_2 var_comp_final\n    | var_type ids var_comp_2 SEMICOLON var_comp_recursive\n    var_comp_2 : COMMA ids var_comp_3\n    | empty\n    var_comp_3 : var_comp_2var_comp_recursive : var_type ids var_comp_2 var_comp_final\n    | var_type ids var_comp_2 SEMICOLON var_comp_recursive\n    var_comp_final : SEMICOLON\n    | var_module_trans\n    var_module_trans : SEMICOLON var_type MODULE funcs_comp\n    ids : ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS OPEN_BRACKETS CT_INT CLOSE_BRACKETS\n    | ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS\n    | ID\n    statements : assignment statements\n    | read statements\n    | write statements\n    | condition statements\n    | return statements\n    | func_call statements\n    | empty\n    assignment : ids ASSIGN expressions SEMICOLONread : READ OPEN_PAREN ids read_comp CLOSE_PAREN SEMICOLONread_comp : COMMA ids read_comp\n    | empty\n    write : WRITE OPEN_PAREN CT_STRING write_comp CLOSE_PAREN\n    | WRITE OPEN_PAREN expressions write_comp CLOSE_PAREN\n    write_comp : COMMA CT_STRING write_comp\n    | COMMA expressions write_comp\n    | empty\n    condition : IF OPEN_PAREN expressions CLOSE_PAREN THEN block ELSE block\n    | IF OPEN_PAREN expressions CLOSE_PAREN THEN block\n    | WHILE OPEN_PAREN expressions CLOSE_PAREN DO block\n    | FOR ids ASSIGN expressions TO expressions DO block\n    return : RETURN OPEN_PAREN exp CLOSE_PAREN SEMICOLONfunc_call : ID OPEN_PAREN func_call_comp CLOSE_PAREN SEMICOLONfunc_call_comp : ID func_call_comp\n    | COMMA ID func_call_comp\n    | expressions\n    expressions : exp expressions_op exp\n    | exp\n    expressions_op : LESS_THAN\n    | MORE_THAN\n    | EQUALS\n    | NOT_EQUALS\n    | AND\n    | OR\n    exp : term exp_compexp_comp : PLUS exp\n    | MINUS exp\n    | empty\n    term : factor term_compterm_comp : MULTIPLIES term\n    | DIVIDE term\n    | empty\n    factor : OPEN_PAREN expressions CLOSE_PAREN\n    | factor_comp ID\n    | factor_comp func_call\n    | ID\n    | func_call\n    | CT_INT\n    | CT_FLOAT\n    | CT_CHAR\n    factor_comp : PLUS\n    | MINUS\n    empty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,18,36,64,],[0,-1,-2,-6,]),'ID':([2,13,14,15,17,20,26,37,38,39,45,46,47,48,49,50,57,61,64,71,72,73,74,75,77,78,88,89,95,96,102,104,106,113,114,115,116,117,118,119,120,122,123,126,127,133,136,144,146,148,158,161,164,165,167,170,174,175,181,182,],[3,-9,-10,-11,22,24,22,59,60,22,59,59,59,59,59,59,22,81,-6,90,22,90,90,90,90,104,90,130,-76,-77,90,104,146,-34,90,-54,-55,-56,-57,-58,-59,90,90,90,90,22,90,104,104,169,-38,-39,90,-47,-48,-35,-44,-45,-43,-46,]),'SEMICOLON':([3,21,22,25,27,34,41,42,43,62,82,84,85,86,87,90,91,92,93,94,112,121,124,125,128,130,131,142,145,150,151,152,153,154,155,156,167,],[4,-78,-26,32,-17,-78,-16,-18,-25,-78,111,113,-53,-78,-78,-71,-72,-73,-74,-75,-24,-60,-63,-64,-67,-69,-70,165,167,-52,-61,-62,-65,-66,-68,170,-48,]),'VARS':([4,79,177,],[6,6,6,]),'VOID':([4,5,7,16,31,32,33,40,64,80,110,111,149,183,],[-78,12,-13,-12,-14,-21,-22,-15,-6,-23,-19,-21,-20,-5,]),'INT':([4,5,6,7,16,30,31,32,33,40,64,80,109,110,111,149,183,],[-78,13,13,-13,-12,13,-14,13,-22,-15,-6,-23,13,-19,13,-20,-5,]),'FLOAT':([4,5,6,7,16,30,31,32,33,40,64,80,109,110,111,149,183,],[-78,14,14,-13,-12,14,-14,14,-22,-15,-6,-23,14,-19,14,-20,-5,]),'CHAR':([4,5,6,7,16,30,31,32,33,40,64,80,109,110,111,149,183,],[-78,15,15,-13,-12,15,-14,15,-22,-15,-6,-23,15,-19,15,-20,-5,]),'MAIN':([4,5,7,8,11,16,31,32,33,40,64,80,110,111,147,149,183,],[-78,-78,-13,19,-4,-12,-14,-21,-22,-15,-6,-23,-19,-21,-3,-20,-5,]),'OPEN_BRACES':([7,16,29,31,32,33,40,64,79,80,108,110,111,149,162,163,177,178,179,180,183,],[-13,-12,37,-14,-21,-22,-15,-6,-78,-23,37,-19,-21,-20,37,37,-78,37,37,37,-5,]),'MODULE':([9,10,12,13,14,15,39,],[20,-7,-8,-9,-10,-11,61,]),'OPEN_PAREN':([19,24,53,54,55,56,58,59,71,73,74,75,77,78,81,88,90,102,104,114,115,116,117,118,119,120,122,123,126,127,130,136,144,146,164,],[23,30,72,73,74,75,77,78,88,88,88,88,88,88,109,88,78,88,144,88,-54,-55,-56,-57,-58,-59,88,88,88,88,78,88,88,88,88,]),'COMMA':([21,22,34,43,62,78,85,86,87,90,91,92,93,94,97,98,99,104,112,121,124,125,128,130,131,144,146,150,151,152,153,154,155,157,159,160,167,],[26,-26,26,-25,26,106,-53,-78,-78,-71,-72,-73,-74,-75,133,136,136,106,-24,-60,-63,-64,-67,-69,-70,106,106,-52,-61,-62,-65,-66,-68,133,136,136,-48,]),'OPEN_BRACKETS':([22,43,59,],[28,63,28,]),'ASSIGN':([22,43,52,59,76,112,],[-26,-25,71,-26,102,-24,]),'CLOSE_PAREN':([22,23,43,60,85,86,87,90,91,92,93,94,97,98,99,100,101,103,104,105,107,112,121,124,125,128,129,130,131,132,134,135,137,138,143,150,151,152,153,154,155,157,159,160,166,167,168,169,171,172,173,],[-26,29,-25,79,-53,-78,-78,-71,-72,-73,-74,-75,-78,-78,-78,139,140,142,-71,145,-51,-24,-60,-63,-64,-67,155,-69,-70,156,-37,158,-42,161,-49,-52,-61,-62,-65,-66,-68,-78,-78,-78,155,-48,-50,177,-36,-40,-41,]),'CT_INT':([28,63,71,73,74,75,77,78,88,102,104,114,115,116,117,118,119,120,122,123,126,127,136,144,146,164,],[35,83,92,92,92,92,92,92,92,92,92,92,-54,-55,-56,-57,-58,-59,92,92,92,92,92,92,92,92,]),'CLOSE_BRACKETS':([35,83,],[43,112,]),'READ':([37,45,46,47,48,49,50,64,113,158,161,165,167,170,174,175,181,182,],[53,53,53,53,53,53,53,-6,-34,-38,-39,-47,-48,-35,-44,-45,-43,-46,]),'WRITE':([37,45,46,47,48,49,50,64,113,158,161,165,167,170,174,175,181,182,],[54,54,54,54,54,54,54,-6,-34,-38,-39,-47,-48,-35,-44,-45,-43,-46,]),'IF':([37,45,46,47,48,49,50,64,113,158,161,165,167,170,174,175,181,182,],[55,55,55,55,55,55,55,-6,-34,-38,-39,-47,-48,-35,-44,-45,-43,-46,]),'WHILE':([37,45,46,47,48,49,50,64,113,158,161,165,167,170,174,175,181,182,],[56,56,56,56,56,56,56,-6,-34,-38,-39,-47,-48,-35,-44,-45,-43,-46,]),'FOR':([37,45,46,47,48,49,50,64,113,158,161,165,167,170,174,175,181,182,],[57,57,57,57,57,57,57,-6,-34,-38,-39,-47,-48,-35,-44,-45,-43,-46,]),'RETURN':([37,45,46,47,48,49,50,64,113,158,161,165,167,170,174,175,181,182,],[58,58,58,58,58,58,58,-6,-34,-38,-39,-47,-48,-35,-44,-45,-43,-46,]),'CLOSE_BRACES':([37,44,45,46,47,48,49,50,51,64,65,66,67,68,69,70,113,158,161,165,167,170,174,175,181,182,],[-78,64,-78,-78,-78,-78,-78,-78,-33,-6,-27,-28,-29,-30,-31,-32,-34,-38,-39,-47,-48,-35,-44,-45,-43,-46,]),'ELSE':([64,174,],[-6,178,]),'CT_FLOAT':([71,73,74,75,77,78,88,102,104,114,115,116,117,118,119,120,122,123,126,127,136,144,146,164,],[93,93,93,93,93,93,93,93,93,93,-54,-55,-56,-57,-58,-59,93,93,93,93,93,93,93,93,]),'CT_CHAR':([71,73,74,75,77,78,88,102,104,114,115,116,117,118,119,120,122,123,126,127,136,144,146,164,],[94,94,94,94,94,94,94,94,94,94,-54,-55,-56,-57,-58,-59,94,94,94,94,94,94,94,94,]),'PLUS':([71,73,74,75,77,78,86,87,88,90,91,92,93,94,102,104,114,115,116,117,118,119,120,122,123,125,126,127,128,130,131,136,144,146,153,154,155,164,167,],[95,95,95,95,95,95,122,-78,95,-71,-72,-73,-74,-75,95,95,95,-54,-55,-56,-57,-58,-59,95,95,-64,95,95,-67,-69,-70,95,95,95,-65,-66,-68,95,-48,]),'MINUS':([71,73,74,75,77,78,86,87,88,90,91,92,93,94,102,104,114,115,116,117,118,119,120,122,123,125,126,127,128,130,131,136,144,146,153,154,155,164,167,],[96,96,96,96,96,96,123,-78,96,-71,-72,-73,-74,-75,96,96,96,-54,-55,-56,-57,-58,-59,96,96,-64,96,96,-67,-69,-70,96,96,96,-65,-66,-68,96,-48,]),'CT_STRING':([73,136,],[98,159,]),'TO':([85,86,87,90,91,92,93,94,121,124,125,128,130,131,141,150,151,152,153,154,155,167,],[-53,-78,-78,-71,-72,-73,-74,-75,-60,-63,-64,-67,-69,-70,164,-52,-61,-62,-65,-66,-68,-48,]),'DO':([85,86,87,90,91,92,93,94,121,124,125,128,130,131,140,150,151,152,153,154,155,167,176,],[-53,-78,-78,-71,-72,-73,-74,-75,-60,-63,-64,-67,-69,-70,163,-52,-61,-62,-65,-66,-68,-48,179,]),'LESS_THAN':([85,86,87,90,91,92,93,94,104,121,124,125,128,130,131,151,152,153,154,155,167,],[115,-78,-78,-71,-72,-73,-74,-75,-71,-60,-63,-64,-67,-69,-70,-61,-62,-65,-66,-68,-48,]),'MORE_THAN':([85,86,87,90,91,92,93,94,104,121,124,125,128,130,131,151,152,153,154,155,167,],[116,-78,-78,-71,-72,-73,-74,-75,-71,-60,-63,-64,-67,-69,-70,-61,-62,-65,-66,-68,-48,]),'EQUALS':([85,86,87,90,91,92,93,94,104,121,124,125,128,130,131,151,152,153,154,155,167,],[117,-78,-78,-71,-72,-73,-74,-75,-71,-60,-63,-64,-67,-69,-70,-61,-62,-65,-66,-68,-48,]),'NOT_EQUALS':([85,86,87,90,91,92,93,94,104,121,124,125,128,130,131,151,152,153,154,155,167,],[118,-78,-78,-71,-72,-73,-74,-75,-71,-60,-63,-64,-67,-69,-70,-61,-62,-65,-66,-68,-48,]),'AND':([85,86,87,90,91,92,93,94,104,121,124,125,128,130,131,151,152,153,154,155,167,],[119,-78,-78,-71,-72,-73,-74,-75,-71,-60,-63,-64,-67,-69,-70,-61,-62,-65,-66,-68,-48,]),'OR':([85,86,87,90,91,92,93,94,104,121,124,125,128,130,131,151,152,153,154,155,167,],[120,-78,-78,-71,-72,-73,-74,-75,-71,-60,-63,-64,-67,-69,-70,-61,-62,-65,-66,-68,-48,]),'MULTIPLIES':([87,90,91,92,93,94,104,130,131,155,167,],[126,-71,-72,-73,-74,-75,-71,-69,-70,-68,-48,]),'DIVIDE':([87,90,91,92,93,94,104,130,131,155,167,],[127,-71,-72,-73,-74,-75,-71,-69,-70,-68,-48,]),'THEN':([139,],[162,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'vars':([4,79,177,],[5,108,180,]),'empty':([4,5,21,34,37,45,46,47,48,49,50,62,79,86,87,97,98,99,157,159,160,177,],[7,11,27,27,51,51,51,51,51,51,51,27,7,124,128,134,137,137,134,137,137,7,]),'funcs':([5,],[8,]),'func_type':([5,],[9,]),'var_type':([5,6,30,32,109,111,],[10,17,38,39,148,39,]),'var_comp':([6,],[16,]),'main':([8,],[18,]),'ids':([17,26,37,39,45,46,47,48,49,50,57,72,133,],[21,34,52,62,52,52,52,52,52,52,76,97,157,]),'var_comp_2':([21,34,62,],[25,42,82,]),'var_comp_final':([25,82,],[31,110,]),'var_module_trans':([25,82,],[33,33,]),'block':([29,108,162,163,178,179,180,],[36,147,174,175,181,182,183,]),'var_comp_recursive':([32,111,],[40,149,]),'var_comp_3':([34,],[41,]),'statements':([37,45,46,47,48,49,50,],[44,65,66,67,68,69,70,]),'assignment':([37,45,46,47,48,49,50,],[45,45,45,45,45,45,45,]),'read':([37,45,46,47,48,49,50,],[46,46,46,46,46,46,46,]),'write':([37,45,46,47,48,49,50,],[47,47,47,47,47,47,47,]),'condition':([37,45,46,47,48,49,50,],[48,48,48,48,48,48,48,]),'return':([37,45,46,47,48,49,50,],[49,49,49,49,49,49,49,]),'func_call':([37,45,46,47,48,49,50,71,73,74,75,77,78,88,89,102,104,114,122,123,126,127,136,144,146,164,],[50,50,50,50,50,50,50,91,91,91,91,91,91,91,131,91,91,91,91,91,91,91,91,91,91,91,]),'funcs_comp':([61,],[80,]),'expressions':([71,73,74,75,78,88,102,104,136,144,146,164,],[84,99,100,101,107,129,141,107,160,166,107,176,]),'exp':([71,73,74,75,77,78,88,102,104,114,122,123,136,144,146,164,],[85,85,85,85,103,85,85,85,85,150,151,152,85,85,85,85,]),'term':([71,73,74,75,77,78,88,102,104,114,122,123,126,127,136,144,146,164,],[86,86,86,86,86,86,86,86,86,86,86,86,153,154,86,86,86,86,]),'factor':([71,73,74,75,77,78,88,102,104,114,122,123,126,127,136,144,146,164,],[87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,]),'factor_comp':([71,73,74,75,77,78,88,102,104,114,122,123,126,127,136,144,146,164,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'func_call_comp':([78,104,144,146,],[105,143,105,168,]),'expressions_op':([85,],[114,]),'exp_comp':([86,],[121,]),'term_comp':([87,],[125,]),'read_comp':([97,157,],[132,171,]),'write_comp':([98,99,159,160,],[135,138,172,173,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON vars funcs main','program',6,'p_program','parser.py',7),
  ('main -> MAIN OPEN_PAREN CLOSE_PAREN block','main',4,'p_main','parser.py',12),
  ('funcs -> func_type MODULE ID OPEN_PAREN var_type ID CLOSE_PAREN vars block','funcs',9,'p_funcs','parser.py',16),
  ('funcs -> empty','funcs',1,'p_funcs','parser.py',17),
  ('funcs_comp -> ID OPEN_PAREN var_type ID CLOSE_PAREN vars block','funcs_comp',7,'p_funcs_comp','parser.py',21),
  ('block -> OPEN_BRACES statements CLOSE_BRACES','block',3,'p_block','parser.py',26),
  ('func_type -> var_type','func_type',1,'p_func_type','parser.py',30),
  ('func_type -> VOID','func_type',1,'p_func_type','parser.py',31),
  ('var_type -> INT','var_type',1,'p_var_type','parser.py',36),
  ('var_type -> FLOAT','var_type',1,'p_var_type','parser.py',37),
  ('var_type -> CHAR','var_type',1,'p_var_type','parser.py',38),
  ('vars -> VARS var_comp','vars',2,'p_vars','parser.py',43),
  ('vars -> empty','vars',1,'p_vars','parser.py',44),
  ('var_comp -> var_type ids var_comp_2 var_comp_final','var_comp',4,'p_var_comp','parser.py',49),
  ('var_comp -> var_type ids var_comp_2 SEMICOLON var_comp_recursive','var_comp',5,'p_var_comp','parser.py',50),
  ('var_comp_2 -> COMMA ids var_comp_3','var_comp_2',3,'p_var_comp_2','parser.py',54),
  ('var_comp_2 -> empty','var_comp_2',1,'p_var_comp_2','parser.py',55),
  ('var_comp_3 -> var_comp_2','var_comp_3',1,'p_var_comp_3','parser.py',59),
  ('var_comp_recursive -> var_type ids var_comp_2 var_comp_final','var_comp_recursive',4,'p_var_comp_recursive','parser.py',62),
  ('var_comp_recursive -> var_type ids var_comp_2 SEMICOLON var_comp_recursive','var_comp_recursive',5,'p_var_comp_recursive','parser.py',63),
  ('var_comp_final -> SEMICOLON','var_comp_final',1,'p_var_comp_final','parser.py',67),
  ('var_comp_final -> var_module_trans','var_comp_final',1,'p_var_comp_final','parser.py',68),
  ('var_module_trans -> SEMICOLON var_type MODULE funcs_comp','var_module_trans',4,'p_var_module_trans','parser.py',73),
  ('ids -> ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS OPEN_BRACKETS CT_INT CLOSE_BRACKETS','ids',7,'p_ids','parser.py',78),
  ('ids -> ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS','ids',4,'p_ids','parser.py',79),
  ('ids -> ID','ids',1,'p_ids','parser.py',80),
  ('statements -> assignment statements','statements',2,'p_statements','parser.py',85),
  ('statements -> read statements','statements',2,'p_statements','parser.py',86),
  ('statements -> write statements','statements',2,'p_statements','parser.py',87),
  ('statements -> condition statements','statements',2,'p_statements','parser.py',88),
  ('statements -> return statements','statements',2,'p_statements','parser.py',89),
  ('statements -> func_call statements','statements',2,'p_statements','parser.py',90),
  ('statements -> empty','statements',1,'p_statements','parser.py',91),
  ('assignment -> ids ASSIGN expressions SEMICOLON','assignment',4,'p_assignment','parser.py',96),
  ('read -> READ OPEN_PAREN ids read_comp CLOSE_PAREN SEMICOLON','read',6,'p_read','parser.py',100),
  ('read_comp -> COMMA ids read_comp','read_comp',3,'p_read_comp','parser.py',104),
  ('read_comp -> empty','read_comp',1,'p_read_comp','parser.py',105),
  ('write -> WRITE OPEN_PAREN CT_STRING write_comp CLOSE_PAREN','write',5,'p_write','parser.py',110),
  ('write -> WRITE OPEN_PAREN expressions write_comp CLOSE_PAREN','write',5,'p_write','parser.py',111),
  ('write_comp -> COMMA CT_STRING write_comp','write_comp',3,'p_write_comp','parser.py',116),
  ('write_comp -> COMMA expressions write_comp','write_comp',3,'p_write_comp','parser.py',117),
  ('write_comp -> empty','write_comp',1,'p_write_comp','parser.py',118),
  ('condition -> IF OPEN_PAREN expressions CLOSE_PAREN THEN block ELSE block','condition',8,'p_condition','parser.py',123),
  ('condition -> IF OPEN_PAREN expressions CLOSE_PAREN THEN block','condition',6,'p_condition','parser.py',124),
  ('condition -> WHILE OPEN_PAREN expressions CLOSE_PAREN DO block','condition',6,'p_condition','parser.py',125),
  ('condition -> FOR ids ASSIGN expressions TO expressions DO block','condition',8,'p_condition','parser.py',126),
  ('return -> RETURN OPEN_PAREN exp CLOSE_PAREN SEMICOLON','return',5,'p_return','parser.py',131),
  ('func_call -> ID OPEN_PAREN func_call_comp CLOSE_PAREN SEMICOLON','func_call',5,'p_func_call','parser.py',135),
  ('func_call_comp -> ID func_call_comp','func_call_comp',2,'p_func_call_comp','parser.py',139),
  ('func_call_comp -> COMMA ID func_call_comp','func_call_comp',3,'p_func_call_comp','parser.py',140),
  ('func_call_comp -> expressions','func_call_comp',1,'p_func_call_comp','parser.py',141),
  ('expressions -> exp expressions_op exp','expressions',3,'p_expressions','parser.py',146),
  ('expressions -> exp','expressions',1,'p_expressions','parser.py',147),
  ('expressions_op -> LESS_THAN','expressions_op',1,'p_expressions_op','parser.py',152),
  ('expressions_op -> MORE_THAN','expressions_op',1,'p_expressions_op','parser.py',153),
  ('expressions_op -> EQUALS','expressions_op',1,'p_expressions_op','parser.py',154),
  ('expressions_op -> NOT_EQUALS','expressions_op',1,'p_expressions_op','parser.py',155),
  ('expressions_op -> AND','expressions_op',1,'p_expressions_op','parser.py',156),
  ('expressions_op -> OR','expressions_op',1,'p_expressions_op','parser.py',157),
  ('exp -> term exp_comp','exp',2,'p_exp','parser.py',162),
  ('exp_comp -> PLUS exp','exp_comp',2,'p_exp_comp','parser.py',166),
  ('exp_comp -> MINUS exp','exp_comp',2,'p_exp_comp','parser.py',167),
  ('exp_comp -> empty','exp_comp',1,'p_exp_comp','parser.py',168),
  ('term -> factor term_comp','term',2,'p_term','parser.py',173),
  ('term_comp -> MULTIPLIES term','term_comp',2,'p_term_comp','parser.py',177),
  ('term_comp -> DIVIDE term','term_comp',2,'p_term_comp','parser.py',178),
  ('term_comp -> empty','term_comp',1,'p_term_comp','parser.py',179),
  ('factor -> OPEN_PAREN expressions CLOSE_PAREN','factor',3,'p_factor','parser.py',184),
  ('factor -> factor_comp ID','factor',2,'p_factor','parser.py',185),
  ('factor -> factor_comp func_call','factor',2,'p_factor','parser.py',186),
  ('factor -> ID','factor',1,'p_factor','parser.py',187),
  ('factor -> func_call','factor',1,'p_factor','parser.py',188),
  ('factor -> CT_INT','factor',1,'p_factor','parser.py',189),
  ('factor -> CT_FLOAT','factor',1,'p_factor','parser.py',190),
  ('factor -> CT_CHAR','factor',1,'p_factor','parser.py',191),
  ('factor_comp -> PLUS','factor_comp',1,'p_factor_comp','parser.py',196),
  ('factor_comp -> MINUS','factor_comp',1,'p_factor_comp','parser.py',197),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',202),
]
