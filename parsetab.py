
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CHAR CLOSE_BRACES CLOSE_BRACKETS CLOSE_PAREN COMMA CT_CHAR CT_FLOAT CT_INT CT_STRING DIVIDE DO ELSE EQUALS FLOAT FOR ID IF INT LESS_THAN LESS_THAN_EQUAL MAIN MINUS MODULE MORE_THAN MORE_THAN_EQUAL MULTIPLIES NOT_EQUALS OPEN_BRACES OPEN_BRACKETS OPEN_PAREN OR PLUS PROGRAM READ RETURN SEMICOLON THEN TO VARS VOID WHILE WRITEprogram : PROGRAM ID add_program SEMICOLON vars funcs main end_programadd_program : end_program : main : MAIN OPEN_PAREN CLOSE_PAREN blockfuncs : func_type MODULE ID add_module OPEN_PAREN funcs_params CLOSE_PAREN vars block\n    | empty\n    add_module :funcs_comp : ID add_module OPEN_PAREN funcs_params CLOSE_PAREN vars blockfuncs_params : var_type variable_params funcs_params_comp\n    | empty\n    funcs_params_comp : COMMA var_type variable_params funcs_params_comp\n    | empty\n    block : OPEN_BRACES statements CLOSE_BRACESfunc_type : var_type\n    | VOID\n    var_type : INT\n    | FLOAT\n    | CHAR\n    vars : VARS var_comp\n    | empty\n    var_comp : var_type ids_dec var_comp_2 var_comp_final\n    | var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive\n    var_comp_2 : COMMA ids_dec var_comp_3\n    | empty\n    var_comp_3 : var_comp_2var_comp_recursive : var_type ids_dec var_comp_2 var_comp_final\n    | var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive\n    var_comp_final : SEMICOLON\n    | var_module_trans\n    var_module_trans : SEMICOLON var_type MODULE funcs_comp\n    ids_dec : ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS OPEN_BRACKETS CT_INT CLOSE_BRACKETS\n    | ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS\n    | ID\n    ids : ID OPEN_BRACKETS exp CLOSE_BRACKETS OPEN_BRACKETS exp CLOSE_BRACKETS\n    | ID OPEN_BRACKETS exp CLOSE_BRACKETS\n    | ID\n    statements : assignment SEMICOLON statements\n    | read SEMICOLON statements \n    | write SEMICOLON statements\n    | condition statements\n    | return SEMICOLON statements\n    | func_call SEMICOLON statements\n    | empty\n    assignment : ids ASSIGN expressionsread : READ OPEN_PAREN ids g_quad_read read_comp CLOSE_PARENread_comp : COMMA ids g_quad_read read_comp\n    | empty \n    g_quad_read : write : WRITE OPEN_PAREN CT_STRING g_quad_write_str write_comp CLOSE_PAREN\n    | WRITE OPEN_PAREN expressions g_quad_write write_comp CLOSE_PAREN\n    write_comp : COMMA CT_STRING g_quad_write_str write_comp\n    | COMMA expressions g_quad_write write_comp\n    | empty\n    g_quad_write_str : g_quad_write : end_if : condition : IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block end_if\n    | IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block ELSE g_else_quad block end_if\n    | WHILE while_jump OPEN_PAREN expressions CLOSE_PAREN g_while_quad DO block end_while\n    | FOR ids validate_for ASSIGN expressions for_counter_control TO expressions for_counter_end DO block\n    g_if_quad :g_else_quad :while_jump :g_while_quad :end_while :validate_for :for_counter_control :for_counter_end :return : RETURN OPEN_PAREN exp CLOSE_PARENfunc_call : ID OPEN_PAREN func_call_comp CLOSE_PAREN\n    func_call_comp : expressions func_call_comp\n    | COMMA expressions func_call_comp\n    | empty\n    expressions : expressions_compexpressions_comp : expression_comp_2\n    | expression_comp_2 OR expressions_comp\n    expression_comp_2 : expression_comp_3\n    | expression_comp_3 AND expression_comp_2\n    expression_comp_3 : exp expressions_op exp g_quad_logic\n    | exp\n    g_quad_logic : expressions_op : LESS_THAN add_op\n    | LESS_THAN_EQUAL add_op\n    | MORE_THAN add_op\n    | MORE_THAN_EQUAL add_op\n    | EQUALS add_op\n    | NOT_EQUALS add_op\n    exp : term g_quad_exp_as\n    | term g_quad_exp_as exp_comp\n    g_quad_exp_as : exp_comp : PLUS add_op exp\n    | MINUS add_op exp\n    term : factor g_quad_exp_md\n    | factor g_quad_exp_md term_comp\n    g_quad_exp_md : term_comp : MULTIPLIES add_op term\n    | DIVIDE add_op term\n    add_op : factor : OPEN_PAREN add_fake expressions CLOSE_PAREN rem_fake\n    | variable \n    | func_call\n    | CT_INT add_ct_int\n    | CT_FLOAT add_ct_float\n    | CT_CHAR add_ct_char\n    add_fake : rem_fake : add_ct_int : add_ct_float : add_ct_char : variable_params : ID\n    | ID dim\n    variable : ID add_id\n    | ID dim\n    add_id : dim : OPEN_BRACKETS exp CLOSE_BRACKETSempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,19,24,38,68,],[0,-3,-1,-4,-13,]),'ID':([2,14,15,16,18,21,28,39,41,50,59,63,65,68,69,70,71,73,74,75,76,77,78,82,83,84,98,99,100,101,102,103,104,105,106,107,108,109,110,115,119,120,128,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,155,157,159,162,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,183,186,193,195,197,198,199,200,201,202,215,216,217,218,219,223,225,231,233,237,239,241,242,],[3,-16,-17,-18,23,26,23,61,23,61,81,87,89,-13,61,61,61,61,61,110,81,110,110,110,110,110,-74,-75,-77,-80,-90,-95,-105,-100,-101,-107,-108,-109,-114,110,110,110,110,110,110,110,-98,-98,-98,-98,-98,-98,-88,-93,110,-102,-103,-104,-112,-113,110,-70,110,87,-76,-78,-81,-82,-83,-84,-85,-86,-87,-89,-98,-98,-94,-98,-98,81,110,110,-115,-79,110,110,110,110,-106,-91,-92,-96,-97,-99,-56,110,-57,-65,-59,-56,-58,-60,]),'SEMICOLON':([3,4,22,23,27,29,36,43,44,45,47,48,49,51,52,66,90,97,98,99,100,101,102,103,105,106,107,108,109,110,132,142,143,145,146,147,148,149,156,157,166,167,168,175,178,195,197,202,203,205,208,215,216,217,218,219,],[-2,5,-116,-33,34,-24,-116,-23,-25,-32,69,70,71,73,74,-116,131,-44,-74,-75,-77,-80,-90,-95,-100,-101,-107,-108,-109,-114,-31,-88,-93,-102,-103,-104,-112,-113,-69,-70,-76,-78,-81,-89,-94,-115,-79,-106,-45,-49,-50,-91,-92,-96,-97,-99,]),'VARS':([5,85,214,],[7,7,7,]),'VOID':([5,6,8,17,33,34,35,42,68,88,130,131,165,235,],[-116,13,-20,-19,-21,-28,-29,-22,-13,-30,-26,-28,-27,-8,]),'INT':([5,6,7,8,17,33,34,35,40,42,68,88,125,130,131,164,165,235,],[-116,14,14,-20,-19,-21,14,-29,14,-22,-13,-30,14,-26,14,14,-27,-8,]),'FLOAT':([5,6,7,8,17,33,34,35,40,42,68,88,125,130,131,164,165,235,],[-116,15,15,-20,-19,-21,15,-29,15,-22,-13,-30,15,-26,15,15,-27,-8,]),'CHAR':([5,6,7,8,17,33,34,35,40,42,68,88,125,130,131,164,165,235,],[-116,16,16,-20,-19,-21,16,-29,16,-22,-13,-30,16,-26,16,16,-27,-8,]),'MAIN':([5,6,8,9,11,17,33,34,35,42,68,88,130,131,161,165,235,],[-116,-116,-20,20,-6,-19,-21,-28,-29,-22,-13,-30,-26,-28,-5,-27,-8,]),'OPEN_BRACES':([8,17,31,33,34,35,42,68,85,88,123,130,131,165,209,214,224,227,232,235,236,240,],[-20,-19,39,-21,-28,-29,-22,-13,-116,-30,39,-26,-28,-27,39,-116,39,39,-62,-8,39,39,]),'MODULE':([10,12,13,14,15,16,41,],[21,-14,-15,-16,-17,-18,65,]),'OPEN_PAREN':([20,26,32,55,56,57,58,60,61,75,77,78,79,82,83,84,89,98,99,100,101,102,103,104,105,106,107,108,109,110,115,119,120,128,129,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,155,157,159,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,186,193,195,197,198,199,200,201,202,215,216,217,218,219,225,],[25,-7,40,76,77,78,-63,82,83,104,104,104,115,104,104,104,-7,-74,-75,-77,-80,-90,-95,-105,-100,-101,-107,-108,-109,83,104,104,104,104,164,104,104,104,-98,-98,-98,-98,-98,-98,-88,-93,104,-102,-103,-104,-112,-113,104,-70,104,-76,-78,-81,-82,-83,-84,-85,-86,-87,-89,-98,-98,-94,-98,-98,104,104,-115,-79,104,104,104,104,-106,-91,-92,-96,-97,-99,104,]),'COMMA':([22,23,36,45,66,81,83,86,87,98,99,100,101,102,103,105,106,107,108,109,110,111,112,113,119,127,132,142,143,145,146,147,148,149,150,151,152,157,159,160,166,167,168,175,178,194,195,197,202,204,206,207,215,216,217,218,219,220,221,222,226,],[28,-33,28,-32,28,-36,120,125,-110,-74,-75,-77,-80,-90,-95,-100,-101,-107,-108,-109,-114,-48,-54,-55,120,-111,-31,-88,-93,-102,-103,-104,-112,-113,183,186,186,-70,120,-35,-76,-78,-81,-89,-94,125,-115,-79,-106,-48,-54,-55,-91,-92,-96,-97,-99,183,186,186,-34,]),'OPEN_BRACKETS':([23,45,61,81,87,110,160,],[30,67,84,84,128,128,193,]),'CLOSE_PAREN':([25,40,62,64,81,83,86,87,98,99,100,101,102,103,105,106,107,108,109,110,111,112,113,114,117,118,119,121,124,126,127,142,143,145,146,147,148,149,150,151,152,154,157,158,159,160,164,166,167,168,175,178,181,182,184,185,187,188,192,194,195,196,197,202,204,206,207,213,215,216,217,218,219,220,221,222,226,228,229,230,],[31,-116,85,-10,-36,-116,-116,-110,-74,-75,-77,-80,-90,-95,-100,-101,-107,-108,-109,-114,-48,-54,-55,153,156,157,-116,-73,-9,-12,-111,-88,-93,-102,-103,-104,-112,-113,-116,-116,-116,190,-70,-71,-116,-35,-116,-76,-78,-81,-89,-94,202,203,-47,205,-53,208,-72,-116,-115,214,-79,-106,-48,-54,-55,-11,-91,-92,-96,-97,-99,-116,-116,-116,-34,-46,-51,-52,]),'CT_INT':([30,67,75,77,78,82,83,84,98,99,100,101,102,103,104,105,106,107,108,109,110,115,119,120,128,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,155,157,159,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,186,193,195,197,198,199,200,201,202,215,216,217,218,219,225,],[37,91,107,107,107,107,107,107,-74,-75,-77,-80,-90,-95,-105,-100,-101,-107,-108,-109,-114,107,107,107,107,107,107,107,-98,-98,-98,-98,-98,-98,-88,-93,107,-102,-103,-104,-112,-113,107,-70,107,-76,-78,-81,-82,-83,-84,-85,-86,-87,-89,-98,-98,-94,-98,-98,107,107,-115,-79,107,107,107,107,-106,-91,-92,-96,-97,-99,107,]),'CLOSE_BRACKETS':([37,91,102,103,105,106,107,108,109,110,122,142,143,145,146,147,148,149,157,163,175,178,195,202,212,215,216,217,218,219,],[45,132,-90,-95,-100,-101,-107,-108,-109,-114,160,-88,-93,-102,-103,-104,-112,-113,-70,195,-89,-94,-115,-106,226,-91,-92,-96,-97,-99,]),'READ':([39,50,68,69,70,71,73,74,223,231,233,237,239,241,242,],[55,55,-13,55,55,55,55,55,-56,-57,-65,-59,-56,-58,-60,]),'WRITE':([39,50,68,69,70,71,73,74,223,231,233,237,239,241,242,],[56,56,-13,56,56,56,56,56,-56,-57,-65,-59,-56,-58,-60,]),'IF':([39,50,68,69,70,71,73,74,223,231,233,237,239,241,242,],[57,57,-13,57,57,57,57,57,-56,-57,-65,-59,-56,-58,-60,]),'WHILE':([39,50,68,69,70,71,73,74,223,231,233,237,239,241,242,],[58,58,-13,58,58,58,58,58,-56,-57,-65,-59,-56,-58,-60,]),'FOR':([39,50,68,69,70,71,73,74,223,231,233,237,239,241,242,],[59,59,-13,59,59,59,59,59,-56,-57,-65,-59,-56,-58,-60,]),'RETURN':([39,50,68,69,70,71,73,74,223,231,233,237,239,241,242,],[60,60,-13,60,60,60,60,60,-56,-57,-65,-59,-56,-58,-60,]),'CLOSE_BRACES':([39,46,50,53,68,69,70,71,72,73,74,92,93,94,95,96,223,231,233,237,239,241,242,],[-116,68,-116,-43,-13,-116,-116,-116,-40,-116,-116,-37,-38,-39,-41,-42,-56,-57,-65,-59,-56,-58,-60,]),'ASSIGN':([54,61,80,81,116,160,226,],[75,-36,-66,-36,155,-35,-34,]),'ELSE':([68,223,],[-13,232,]),'CT_FLOAT':([75,77,78,82,83,84,98,99,100,101,102,103,104,105,106,107,108,109,110,115,119,120,128,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,155,157,159,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,186,193,195,197,198,199,200,201,202,215,216,217,218,219,225,],[108,108,108,108,108,108,-74,-75,-77,-80,-90,-95,-105,-100,-101,-107,-108,-109,-114,108,108,108,108,108,108,108,-98,-98,-98,-98,-98,-98,-88,-93,108,-102,-103,-104,-112,-113,108,-70,108,-76,-78,-81,-82,-83,-84,-85,-86,-87,-89,-98,-98,-94,-98,-98,108,108,-115,-79,108,108,108,108,-106,-91,-92,-96,-97,-99,108,]),'CT_CHAR':([75,77,78,82,83,84,98,99,100,101,102,103,104,105,106,107,108,109,110,115,119,120,128,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,155,157,159,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,186,193,195,197,198,199,200,201,202,215,216,217,218,219,225,],[109,109,109,109,109,109,-74,-75,-77,-80,-90,-95,-105,-100,-101,-107,-108,-109,-114,109,109,109,109,109,109,109,-98,-98,-98,-98,-98,-98,-88,-93,109,-102,-103,-104,-112,-113,109,-70,109,-76,-78,-81,-82,-83,-84,-85,-86,-87,-89,-98,-98,-94,-98,-98,109,109,-115,-79,109,109,109,109,-106,-91,-92,-96,-97,-99,109,]),'CT_STRING':([77,186,],[112,206,]),'TO':([98,99,100,101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,166,167,168,175,178,191,195,197,202,211,215,216,217,218,219,],[-74,-75,-77,-80,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-76,-78,-81,-89,-94,-67,-115,-79,-106,225,-91,-92,-96,-97,-99,]),'DO':([98,99,100,101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,166,167,168,175,178,190,195,197,202,210,215,216,217,218,219,234,238,],[-74,-75,-77,-80,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-76,-78,-81,-89,-94,-64,-115,-79,-106,224,-91,-92,-96,-97,-99,-68,240,]),'OR':([99,100,101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,167,168,175,178,195,197,202,215,216,217,218,219,],[133,-77,-80,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-78,-81,-89,-94,-115,-79,-106,-91,-92,-96,-97,-99,]),'AND':([100,101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,168,175,178,195,197,202,215,216,217,218,219,],[134,-80,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-81,-89,-94,-115,-79,-106,-91,-92,-96,-97,-99,]),'LESS_THAN':([101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,175,178,195,202,215,216,217,218,219,],[136,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-89,-94,-115,-106,-91,-92,-96,-97,-99,]),'LESS_THAN_EQUAL':([101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,175,178,195,202,215,216,217,218,219,],[137,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-89,-94,-115,-106,-91,-92,-96,-97,-99,]),'MORE_THAN':([101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,175,178,195,202,215,216,217,218,219,],[138,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-89,-94,-115,-106,-91,-92,-96,-97,-99,]),'MORE_THAN_EQUAL':([101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,175,178,195,202,215,216,217,218,219,],[139,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-89,-94,-115,-106,-91,-92,-96,-97,-99,]),'EQUALS':([101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,175,178,195,202,215,216,217,218,219,],[140,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-89,-94,-115,-106,-91,-92,-96,-97,-99,]),'NOT_EQUALS':([101,102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,175,178,195,202,215,216,217,218,219,],[141,-90,-95,-100,-101,-107,-108,-109,-114,-88,-93,-102,-103,-104,-112,-113,-70,-89,-94,-115,-106,-91,-92,-96,-97,-99,]),'PLUS':([102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,178,195,202,217,218,219,],[-90,-95,-100,-101,-107,-108,-109,-114,176,-93,-102,-103,-104,-112,-113,-70,-94,-115,-106,-96,-97,-99,]),'MINUS':([102,103,105,106,107,108,109,110,142,143,145,146,147,148,149,157,178,195,202,217,218,219,],[-90,-95,-100,-101,-107,-108,-109,-114,177,-93,-102,-103,-104,-112,-113,-70,-94,-115,-106,-96,-97,-99,]),'MULTIPLIES':([103,105,106,107,108,109,110,143,145,146,147,148,149,157,195,202,219,],[-95,-100,-101,-107,-108,-109,-114,179,-102,-103,-104,-112,-113,-70,-115,-106,-99,]),'DIVIDE':([103,105,106,107,108,109,110,143,145,146,147,148,149,157,195,202,219,],[-95,-100,-101,-107,-108,-109,-114,180,-102,-103,-104,-112,-113,-70,-115,-106,-99,]),'THEN':([153,189,],[-61,209,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'add_program':([3,],[4,]),'vars':([5,85,214,],[6,123,227,]),'empty':([5,6,22,36,39,40,50,66,69,70,71,73,74,83,85,86,119,150,151,152,159,164,194,214,220,221,222,],[8,11,29,29,53,64,53,29,53,53,53,53,53,121,8,126,121,184,187,187,121,64,126,8,184,187,187,]),'funcs':([6,],[9,]),'func_type':([6,],[10,]),'var_type':([6,7,34,40,125,131,164,],[12,18,41,63,162,41,63,]),'var_comp':([7,],[17,]),'main':([9,],[19,]),'ids_dec':([18,28,41,],[22,36,66,]),'end_program':([19,],[24,]),'var_comp_2':([22,36,66,],[27,44,90,]),'add_module':([26,89,],[32,129,]),'var_comp_final':([27,90,],[33,130,]),'var_module_trans':([27,90,],[35,35,]),'block':([31,123,209,224,227,236,240,],[38,161,223,233,235,239,242,]),'var_comp_recursive':([34,131,],[42,165,]),'var_comp_3':([36,],[43,]),'statements':([39,50,69,70,71,73,74,],[46,72,92,93,94,95,96,]),'assignment':([39,50,69,70,71,73,74,],[47,47,47,47,47,47,47,]),'read':([39,50,69,70,71,73,74,],[48,48,48,48,48,48,48,]),'write':([39,50,69,70,71,73,74,],[49,49,49,49,49,49,49,]),'condition':([39,50,69,70,71,73,74,],[50,50,50,50,50,50,50,]),'return':([39,50,69,70,71,73,74,],[51,51,51,51,51,51,51,]),'func_call':([39,50,69,70,71,73,74,75,77,78,82,83,84,115,119,120,128,133,134,135,144,155,159,186,193,198,199,200,201,225,],[52,52,52,52,52,52,52,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,]),'ids':([39,50,59,69,70,71,73,74,76,183,],[54,54,80,54,54,54,54,54,111,204,]),'funcs_params':([40,164,],[62,196,]),'while_jump':([58,],[79,]),'variable_params':([63,162,],[86,194,]),'funcs_comp':([65,],[88,]),'expressions':([75,77,78,83,115,119,120,144,155,159,186,225,],[97,113,114,119,154,119,159,181,191,119,207,234,]),'expressions_comp':([75,77,78,83,115,119,120,133,144,155,159,186,225,],[98,98,98,98,98,98,98,166,98,98,98,98,98,]),'expression_comp_2':([75,77,78,83,115,119,120,133,134,144,155,159,186,225,],[99,99,99,99,99,99,99,99,167,99,99,99,99,99,]),'expression_comp_3':([75,77,78,83,115,119,120,133,134,144,155,159,186,225,],[100,100,100,100,100,100,100,100,100,100,100,100,100,100,]),'exp':([75,77,78,82,83,84,115,119,120,128,133,134,135,144,155,159,186,193,198,199,225,],[101,101,101,117,101,122,101,101,101,163,101,101,168,101,101,101,101,212,215,216,101,]),'term':([75,77,78,82,83,84,115,119,120,128,133,134,135,144,155,159,186,193,198,199,200,201,225,],[102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,217,218,102,]),'factor':([75,77,78,82,83,84,115,119,120,128,133,134,135,144,155,159,186,193,198,199,200,201,225,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'variable':([75,77,78,82,83,84,115,119,120,128,133,134,135,144,155,159,186,193,198,199,200,201,225,],[105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'validate_for':([80,],[116,]),'func_call_comp':([83,119,159,],[118,158,192,]),'funcs_params_comp':([86,194,],[124,213,]),'dim':([87,110,],[127,149,]),'expressions_op':([101,],[135,]),'g_quad_exp_as':([102,],[142,]),'g_quad_exp_md':([103,],[143,]),'add_fake':([104,],[144,]),'add_ct_int':([107,],[145,]),'add_ct_float':([108,],[146,]),'add_ct_char':([109,],[147,]),'add_id':([110,],[148,]),'g_quad_read':([111,204,],[150,220,]),'g_quad_write_str':([112,206,],[151,221,]),'g_quad_write':([113,207,],[152,222,]),'add_op':([136,137,138,139,140,141,176,177,179,180,],[169,170,171,172,173,174,198,199,200,201,]),'exp_comp':([142,],[175,]),'term_comp':([143,],[178,]),'read_comp':([150,220,],[182,228,]),'write_comp':([151,152,221,222,],[185,188,229,230,]),'g_if_quad':([153,],[189,]),'g_quad_logic':([168,],[197,]),'g_while_quad':([190,],[210,]),'for_counter_control':([191,],[211,]),'rem_fake':([202,],[219,]),'end_if':([223,239,],[231,241,]),'g_else_quad':([232,],[236,]),'end_while':([233,],[237,]),'for_counter_end':([234,],[238,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID add_program SEMICOLON vars funcs main end_program','program',8,'p_program','parser.py',52),
  ('add_program -> <empty>','add_program',0,'p_add_program','parser.py',55),
  ('end_program -> <empty>','end_program',0,'p_end_program','parser.py',72),
  ('main -> MAIN OPEN_PAREN CLOSE_PAREN block','main',4,'p_main','parser.py',82),
  ('funcs -> func_type MODULE ID add_module OPEN_PAREN funcs_params CLOSE_PAREN vars block','funcs',9,'p_funcs','parser.py',86),
  ('funcs -> empty','funcs',1,'p_funcs','parser.py',87),
  ('add_module -> <empty>','add_module',0,'p_add_module','parser.py',91),
  ('funcs_comp -> ID add_module OPEN_PAREN funcs_params CLOSE_PAREN vars block','funcs_comp',7,'p_funcs_comp','parser.py',109),
  ('funcs_params -> var_type variable_params funcs_params_comp','funcs_params',3,'p_funcs_params','parser.py',113),
  ('funcs_params -> empty','funcs_params',1,'p_funcs_params','parser.py',114),
  ('funcs_params_comp -> COMMA var_type variable_params funcs_params_comp','funcs_params_comp',4,'p_funcs_params_comp','parser.py',119),
  ('funcs_params_comp -> empty','funcs_params_comp',1,'p_funcs_params_comp','parser.py',120),
  ('block -> OPEN_BRACES statements CLOSE_BRACES','block',3,'p_block','parser.py',126),
  ('func_type -> var_type','func_type',1,'p_func_type','parser.py',130),
  ('func_type -> VOID','func_type',1,'p_func_type','parser.py',131),
  ('var_type -> INT','var_type',1,'p_var_type','parser.py',139),
  ('var_type -> FLOAT','var_type',1,'p_var_type','parser.py',140),
  ('var_type -> CHAR','var_type',1,'p_var_type','parser.py',141),
  ('vars -> VARS var_comp','vars',2,'p_vars','parser.py',149),
  ('vars -> empty','vars',1,'p_vars','parser.py',150),
  ('var_comp -> var_type ids_dec var_comp_2 var_comp_final','var_comp',4,'p_var_comp','parser.py',155),
  ('var_comp -> var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive','var_comp',5,'p_var_comp','parser.py',156),
  ('var_comp_2 -> COMMA ids_dec var_comp_3','var_comp_2',3,'p_var_comp_2','parser.py',160),
  ('var_comp_2 -> empty','var_comp_2',1,'p_var_comp_2','parser.py',161),
  ('var_comp_3 -> var_comp_2','var_comp_3',1,'p_var_comp_3','parser.py',165),
  ('var_comp_recursive -> var_type ids_dec var_comp_2 var_comp_final','var_comp_recursive',4,'p_var_comp_recursive','parser.py',168),
  ('var_comp_recursive -> var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive','var_comp_recursive',5,'p_var_comp_recursive','parser.py',169),
  ('var_comp_final -> SEMICOLON','var_comp_final',1,'p_var_comp_final','parser.py',173),
  ('var_comp_final -> var_module_trans','var_comp_final',1,'p_var_comp_final','parser.py',174),
  ('var_module_trans -> SEMICOLON var_type MODULE funcs_comp','var_module_trans',4,'p_var_module_trans','parser.py',179),
  ('ids_dec -> ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS OPEN_BRACKETS CT_INT CLOSE_BRACKETS','ids_dec',7,'p_ids_dec','parser.py',184),
  ('ids_dec -> ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS','ids_dec',4,'p_ids_dec','parser.py',185),
  ('ids_dec -> ID','ids_dec',1,'p_ids_dec','parser.py',186),
  ('ids -> ID OPEN_BRACKETS exp CLOSE_BRACKETS OPEN_BRACKETS exp CLOSE_BRACKETS','ids',7,'p_ids','parser.py',199),
  ('ids -> ID OPEN_BRACKETS exp CLOSE_BRACKETS','ids',4,'p_ids','parser.py',200),
  ('ids -> ID','ids',1,'p_ids','parser.py',201),
  ('statements -> assignment SEMICOLON statements','statements',3,'p_statements','parser.py',217),
  ('statements -> read SEMICOLON statements','statements',3,'p_statements','parser.py',218),
  ('statements -> write SEMICOLON statements','statements',3,'p_statements','parser.py',219),
  ('statements -> condition statements','statements',2,'p_statements','parser.py',220),
  ('statements -> return SEMICOLON statements','statements',3,'p_statements','parser.py',221),
  ('statements -> func_call SEMICOLON statements','statements',3,'p_statements','parser.py',222),
  ('statements -> empty','statements',1,'p_statements','parser.py',223),
  ('assignment -> ids ASSIGN expressions','assignment',3,'p_assignment','parser.py',228),
  ('read -> READ OPEN_PAREN ids g_quad_read read_comp CLOSE_PAREN','read',6,'p_read','parser.py',246),
  ('read_comp -> COMMA ids g_quad_read read_comp','read_comp',4,'p_read_comp','parser.py',251),
  ('read_comp -> empty','read_comp',1,'p_read_comp','parser.py',252),
  ('g_quad_read -> <empty>','g_quad_read',0,'p_g_quad_read','parser.py',257),
  ('write -> WRITE OPEN_PAREN CT_STRING g_quad_write_str write_comp CLOSE_PAREN','write',6,'p_write','parser.py',267),
  ('write -> WRITE OPEN_PAREN expressions g_quad_write write_comp CLOSE_PAREN','write',6,'p_write','parser.py',268),
  ('write_comp -> COMMA CT_STRING g_quad_write_str write_comp','write_comp',4,'p_write_comp','parser.py',273),
  ('write_comp -> COMMA expressions g_quad_write write_comp','write_comp',4,'p_write_comp','parser.py',274),
  ('write_comp -> empty','write_comp',1,'p_write_comp','parser.py',275),
  ('g_quad_write_str -> <empty>','g_quad_write_str',0,'p_g_quad_write_str','parser.py',280),
  ('g_quad_write -> <empty>','g_quad_write',0,'p_g_quad_write','parser.py',286),
  ('end_if -> <empty>','end_if',0,'p_end_if','parser.py',292),
  ('condition -> IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block end_if','condition',8,'p_condition','parser.py',298),
  ('condition -> IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block ELSE g_else_quad block end_if','condition',11,'p_condition','parser.py',299),
  ('condition -> WHILE while_jump OPEN_PAREN expressions CLOSE_PAREN g_while_quad DO block end_while','condition',9,'p_condition','parser.py',300),
  ('condition -> FOR ids validate_for ASSIGN expressions for_counter_control TO expressions for_counter_end DO block','condition',11,'p_condition','parser.py',301),
  ('g_if_quad -> <empty>','g_if_quad',0,'p_g_if_quad','parser.py',306),
  ('g_else_quad -> <empty>','g_else_quad',0,'p_g_else_quad','parser.py',318),
  ('while_jump -> <empty>','while_jump',0,'p_while_jump','parser.py',331),
  ('g_while_quad -> <empty>','g_while_quad',0,'p_g_while_quad','parser.py',336),
  ('end_while -> <empty>','end_while',0,'p_end_while','parser.py',346),
  ('validate_for -> <empty>','validate_for',0,'p_validate_for','parser.py',354),
  ('for_counter_control -> <empty>','for_counter_control',0,'p_for_counter_control','parser.py',364),
  ('for_counter_end -> <empty>','for_counter_end',0,'p_for_counter_end','parser.py',379),
  ('return -> RETURN OPEN_PAREN exp CLOSE_PAREN','return',4,'p_return','parser.py',388),
  ('func_call -> ID OPEN_PAREN func_call_comp CLOSE_PAREN','func_call',4,'p_func_call','parser.py',392),
  ('func_call_comp -> expressions func_call_comp','func_call_comp',2,'p_func_call_comp','parser.py',397),
  ('func_call_comp -> COMMA expressions func_call_comp','func_call_comp',3,'p_func_call_comp','parser.py',398),
  ('func_call_comp -> empty','func_call_comp',1,'p_func_call_comp','parser.py',399),
  ('expressions -> expressions_comp','expressions',1,'p_expressions','parser.py',404),
  ('expressions_comp -> expression_comp_2','expressions_comp',1,'p_expressions_comp','parser.py',408),
  ('expressions_comp -> expression_comp_2 OR expressions_comp','expressions_comp',3,'p_expressions_comp','parser.py',409),
  ('expression_comp_2 -> expression_comp_3','expression_comp_2',1,'p_expression_comp_2','parser.py',414),
  ('expression_comp_2 -> expression_comp_3 AND expression_comp_2','expression_comp_2',3,'p_expression_comp_2','parser.py',415),
  ('expression_comp_3 -> exp expressions_op exp g_quad_logic','expression_comp_3',4,'p_expression_comp_3','parser.py',420),
  ('expression_comp_3 -> exp','expression_comp_3',1,'p_expression_comp_3','parser.py',421),
  ('g_quad_logic -> <empty>','g_quad_logic',0,'p_g_quad_logic','parser.py',425),
  ('expressions_op -> LESS_THAN add_op','expressions_op',2,'p_expressions_op','parser.py',430),
  ('expressions_op -> LESS_THAN_EQUAL add_op','expressions_op',2,'p_expressions_op','parser.py',431),
  ('expressions_op -> MORE_THAN add_op','expressions_op',2,'p_expressions_op','parser.py',432),
  ('expressions_op -> MORE_THAN_EQUAL add_op','expressions_op',2,'p_expressions_op','parser.py',433),
  ('expressions_op -> EQUALS add_op','expressions_op',2,'p_expressions_op','parser.py',434),
  ('expressions_op -> NOT_EQUALS add_op','expressions_op',2,'p_expressions_op','parser.py',435),
  ('exp -> term g_quad_exp_as','exp',2,'p_exp','parser.py',441),
  ('exp -> term g_quad_exp_as exp_comp','exp',3,'p_exp','parser.py',442),
  ('g_quad_exp_as -> <empty>','g_quad_exp_as',0,'p_g_quad_exp_as','parser.py',447),
  ('exp_comp -> PLUS add_op exp','exp_comp',3,'p_exp_comp','parser.py',452),
  ('exp_comp -> MINUS add_op exp','exp_comp',3,'p_exp_comp','parser.py',453),
  ('term -> factor g_quad_exp_md','term',2,'p_term','parser.py',458),
  ('term -> factor g_quad_exp_md term_comp','term',3,'p_term','parser.py',459),
  ('g_quad_exp_md -> <empty>','g_quad_exp_md',0,'p_g_quad_exp_md','parser.py',464),
  ('term_comp -> MULTIPLIES add_op term','term_comp',3,'p_term_comp','parser.py',469),
  ('term_comp -> DIVIDE add_op term','term_comp',3,'p_term_comp','parser.py',470),
  ('add_op -> <empty>','add_op',0,'p_add_op','parser.py',474),
  ('factor -> OPEN_PAREN add_fake expressions CLOSE_PAREN rem_fake','factor',5,'p_factor','parser.py',567),
  ('factor -> variable','factor',1,'p_factor','parser.py',568),
  ('factor -> func_call','factor',1,'p_factor','parser.py',569),
  ('factor -> CT_INT add_ct_int','factor',2,'p_factor','parser.py',570),
  ('factor -> CT_FLOAT add_ct_float','factor',2,'p_factor','parser.py',571),
  ('factor -> CT_CHAR add_ct_char','factor',2,'p_factor','parser.py',572),
  ('add_fake -> <empty>','add_fake',0,'p_add_fake','parser.py',576),
  ('rem_fake -> <empty>','rem_fake',0,'p_rem_fake','parser.py',580),
  ('add_ct_int -> <empty>','add_ct_int',0,'p_add_ct_int','parser.py',585),
  ('add_ct_float -> <empty>','add_ct_float',0,'p_add_ct_float','parser.py',593),
  ('add_ct_char -> <empty>','add_ct_char',0,'p_add_ct_char','parser.py',600),
  ('variable_params -> ID','variable_params',1,'p_variable_params','parser.py',608),
  ('variable_params -> ID dim','variable_params',2,'p_variable_params','parser.py',609),
  ('variable -> ID add_id','variable',2,'p_variable','parser.py',614),
  ('variable -> ID dim','variable',2,'p_variable','parser.py',615),
  ('add_id -> <empty>','add_id',0,'p_add_id','parser.py',620),
  ('dim -> OPEN_BRACKETS exp CLOSE_BRACKETS','dim',3,'p_dim','parser.py',640),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',645),
]
