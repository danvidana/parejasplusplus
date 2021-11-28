
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CHAR CLOSE_BRACES CLOSE_BRACKETS CLOSE_PAREN COMMA CT_CHAR CT_FLOAT CT_INT CT_STRING DIVIDE DO ELSE EQUALS FLOAT FOR ID IF INT LESS_THAN LESS_THAN_EQUAL MAIN MINUS MODULE MORE_THAN MORE_THAN_EQUAL MULTIPLIES NOT_EQUALS OPEN_BRACES OPEN_BRACKETS OPEN_PAREN OR PLUS PROGRAM READ RETURN SEMICOLON THEN TO VARS VOID WHILE WRITEprogram : PROGRAM g_main_quad ID add_program SEMICOLON vars funcs main end_programadd_program : end_program : main : MAIN OPEN_PAREN CLOSE_PAREN fill_main_quad blockg_main_quad :fill_main_quad :funcs : func_type MODULE ID add_module OPEN_PAREN funcs_params CLOSE_PAREN add_parameter_amount vars count_local_vars block end_funcs funcs\n    | empty\n    end_funcs :count_local_vars :add_module :funcs_comp : ID add_module OPEN_PAREN funcs_params CLOSE_PAREN add_parameter_amount vars count_local_vars block end_funcs funcsadd_parameter_amount :funcs_params : var_type variable_params funcs_params_comp\n    | empty\n    funcs_params_comp : COMMA var_type variable_params funcs_params_comp\n    | empty\n    variable_params : ID\n    | ID dim\n    block : OPEN_BRACES statements CLOSE_BRACESfunc_type : var_type\n    | VOID\n    var_type : INT\n    | FLOAT\n    | CHAR\n    vars : VARS var_comp\n    | empty\n    var_comp : var_type ids_dec var_comp_2 var_comp_final\n    | var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive\n    var_comp_2 : COMMA ids_dec var_comp_3\n    | empty\n    var_comp_3 : var_comp_2var_comp_recursive : var_type ids_dec var_comp_2 var_comp_final\n    | var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive\n    var_comp_final : SEMICOLON\n    | var_module_trans\n    var_module_trans : SEMICOLON var_type MODULE funcs_comp\n    ids_dec : ids_dec_matrix\n    | ids_dec_array\n    | ids_dec_single\n    ids_dec_matrix : ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS OPEN_BRACKETS CT_INT CLOSE_BRACKETSids_dec_array : ID OPEN_BRACKETS CT_INT CLOSE_BRACKETSids_dec_single : IDids : ids_matrix\n    | ids_array\n    | ids_single\n    ids_matrix : ID OPEN_BRACKETS exp CLOSE_BRACKETS OPEN_BRACKETS exp CLOSE_BRACKETSids_array : ID OPEN_BRACKETS exp CLOSE_BRACKETSids_single : IDstatements : assignment SEMICOLON statements\n    | read SEMICOLON statements \n    | write SEMICOLON statements\n    | condition statements\n    | return SEMICOLON statements\n    | func_call SEMICOLON statements\n    | empty\n    assignment : ids ASSIGN expressionsread : READ OPEN_PAREN ids g_quad_read read_comp CLOSE_PARENread_comp : COMMA ids g_quad_read read_comp\n    | empty \n    g_quad_read : write : WRITE OPEN_PAREN CT_STRING g_quad_write_str write_comp CLOSE_PAREN\n    | WRITE OPEN_PAREN expressions g_quad_write write_comp CLOSE_PAREN\n    write_comp : COMMA CT_STRING g_quad_write_str write_comp\n    | COMMA expressions g_quad_write write_comp\n    | empty\n    g_quad_write_str : g_quad_write : end_if : condition : IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block end_if\n    | IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block ELSE g_else_quad block end_if\n    | WHILE while_jump OPEN_PAREN expressions CLOSE_PAREN g_while_quad DO block end_while\n    | FOR ids validate_for ASSIGN expressions for_counter_control TO expressions for_counter_end DO block end_for\n    g_if_quad :g_else_quad :while_jump :g_while_quad :end_while :validate_for :for_counter_control :for_counter_end :end_for :return : RETURN OPEN_PAREN expressions CLOSE_PAREN g_quad_returng_quad_return :func_call : ID verify_function_exists OPEN_PAREN era_activation func_call_comp CLOSE_PAREN g_gosub_quad function_call_end\n    function_call_end :g_gosub_quad :change_to_global :verify_function_exists :era_activation :func_call_comp : expressions g_parameter_quad func_call_comp\n    | COMMA expressions g_parameter_quad func_call_comp\n    | empty\n    g_parameter_quad :expressions : expressions_compexpressions_comp : expression_comp_2\n    | expression_comp_2 OR expressions_comp\n    expression_comp_2 : expression_comp_3\n    | expression_comp_3 AND expression_comp_2\n    expression_comp_3 : exp expressions_op exp g_quad_logic\n    | exp\n    g_quad_logic : expressions_op : LESS_THAN add_op\n    | LESS_THAN_EQUAL add_op\n    | MORE_THAN add_op\n    | MORE_THAN_EQUAL add_op\n    | EQUALS add_op\n    | NOT_EQUALS add_op\n    exp : term g_quad_exp_as_alone\n    | term g_quad_exp_as exp_comp\n    g_quad_exp_as : g_quad_exp_as_alone : exp_comp : PLUS add_op exp\n    | MINUS add_op exp\n    term : factor g_quad_exp_md_alone\n    | factor g_quad_exp_md term_comp\n    g_quad_exp_md : g_quad_exp_md_alone : term_comp : MULTIPLIES add_op term\n    | DIVIDE add_op term\n    add_op : factor : OPEN_PAREN add_fake expressions CLOSE_PAREN rem_fake\n    | variable \n    | func_call\n    | CT_INT add_ct_int\n    | CT_FLOAT add_ct_float\n    | CT_CHAR add_ct_char\n    add_fake : rem_fake : add_ct_int : add_ct_float : add_ct_char : variable : ID add_id\n    | ID dim\n    add_id : dim : OPEN_BRACKETS exp CLOSE_BRACKETSempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,20,28,49,83,],[0,-3,-1,-4,-20,]),'ID':([2,3,15,16,17,19,22,32,44,50,52,54,61,70,83,84,85,86,88,89,90,91,92,93,97,99,105,116,117,118,119,120,121,122,123,124,125,126,127,128,133,136,139,143,144,145,146,147,148,149,150,151,152,154,156,157,158,159,160,161,167,169,173,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,192,195,203,204,206,210,211,212,213,214,215,225,226,227,231,232,233,234,235,239,241,242,244,251,253,255,259,262,265,266,268,],[-5,4,-23,-24,-25,27,30,27,27,72,78,80,72,96,-20,72,72,72,72,72,128,96,128,128,128,128,128,-95,-96,-98,-101,-112,-118,-128,-123,-124,-130,-131,-132,-135,128,-90,78,128,128,128,-121,-121,-121,-121,-121,-121,-109,-115,128,-125,-126,-127,-133,-134,128,128,-136,-97,-99,-102,-103,-104,-105,-106,-107,-108,-110,-121,-121,-116,-121,-121,96,128,-94,128,128,-100,128,128,128,128,-129,-87,128,-94,-113,-114,-119,-120,-122,-69,128,-86,128,-70,-78,-85,-72,-69,-71,-82,-73,]),'SEMICOLON':([4,5,23,24,25,26,27,31,33,40,46,47,48,55,58,59,60,62,63,81,109,115,116,117,118,119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,168,173,175,176,177,184,187,201,210,215,216,218,221,225,231,232,233,234,235,242,255,],[-2,6,-137,-38,-39,-40,-43,38,-31,-137,-30,-32,-42,-137,84,85,86,88,89,108,-41,-57,-95,-96,-98,-101,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-84,-136,-97,-99,-102,-110,-116,-83,-100,-129,-58,-62,-63,-87,-113,-114,-119,-120,-122,-86,-85,]),'VARS':([6,76,100,209,230,],[8,-13,8,-13,8,]),'VOID':([6,7,9,12,18,37,38,39,45,79,83,107,108,142,207,229,246,261,264,267,],[-137,14,-27,-8,-26,-28,-35,-36,-29,-37,-20,-33,-35,-34,-9,14,-7,-9,14,-12,]),'INT':([6,7,8,9,12,18,37,38,39,43,45,79,83,102,107,108,141,142,207,229,246,261,264,267,],[-137,15,15,-27,-8,-26,-28,15,-36,15,-29,-37,-20,15,-33,15,15,-34,-9,15,-7,-9,15,-12,]),'FLOAT':([6,7,8,9,12,18,37,38,39,43,45,79,83,102,107,108,141,142,207,229,246,261,264,267,],[-137,16,16,-27,-8,-26,-28,16,-36,16,-29,-37,-20,16,-33,16,16,-34,-9,16,-7,-9,16,-12,]),'CHAR':([6,7,8,9,12,18,37,38,39,43,45,79,83,102,107,108,141,142,207,229,246,261,264,267,],[-137,17,17,-27,-8,-26,-28,17,-36,17,-29,-37,-20,17,-33,17,17,-34,-9,17,-7,-9,17,-12,]),'MAIN':([6,7,9,10,12,18,37,38,39,45,79,83,107,108,142,207,229,246,261,264,267,],[-137,-137,-27,21,-8,-26,-28,-35,-36,-29,-37,-20,-33,-35,-34,-9,-137,-7,-9,-137,-12,]),'OPEN_BRACES':([9,12,18,35,37,38,39,42,45,76,79,83,100,107,108,138,142,171,207,209,222,229,230,240,246,247,252,257,258,261,263,264,267,],[-27,-8,-26,-6,-28,-35,-36,50,-29,-13,-37,-20,-137,-33,-35,-10,-34,50,-9,-13,50,-137,-137,50,-7,-10,-75,50,50,-9,50,-137,-12,]),'MODULE':([11,13,14,15,16,17,44,],[22,-21,-22,-23,-24,-25,54,]),'OPEN_PAREN':([21,30,36,66,67,68,69,71,72,80,90,92,93,94,97,98,99,105,106,116,117,118,119,120,121,122,123,124,125,126,127,128,133,136,143,144,145,146,147,148,149,150,151,152,154,156,157,158,159,160,161,167,169,173,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,195,203,204,206,210,211,212,213,214,215,225,226,227,231,232,233,234,235,241,242,244,255,],[29,-11,43,91,92,93,-76,97,-89,-11,122,122,122,133,122,136,122,122,141,-95,-96,-98,-101,-112,-118,-128,-123,-124,-130,-131,-132,-89,122,-90,122,122,122,-121,-121,-121,-121,-121,-121,-109,-115,122,-125,-126,-127,-133,-134,122,122,-136,-97,-99,-102,-103,-104,-105,-106,-107,-108,-110,-121,-121,-116,-121,-121,122,-94,122,122,-100,122,122,122,122,-129,-87,122,-94,-113,-114,-119,-120,-122,122,-86,122,-85,]),'COMMA':([23,24,25,26,27,40,48,55,73,74,75,77,78,96,104,109,116,117,118,119,120,121,123,124,125,126,127,128,129,130,131,136,152,154,157,158,159,160,161,162,163,164,169,170,172,173,175,176,177,184,187,203,210,215,217,219,220,225,226,227,231,232,233,234,235,236,237,238,242,244,245,255,],[32,-38,-39,-40,-43,32,-42,32,-44,-45,-46,102,-18,-49,-19,-41,-95,-96,-98,-101,-112,-118,-123,-124,-130,-131,-132,-135,-61,-67,-68,-90,-109,-115,-125,-126,-127,-133,-134,192,195,195,204,-48,102,-136,-97,-99,-102,-110,-116,-94,-100,-129,-61,-67,-68,-87,204,-94,-113,-114,-119,-120,-122,192,195,195,-86,204,-47,-85,]),'OPEN_BRACKETS':([27,48,72,78,96,128,170,],[34,56,99,105,99,105,206,]),'CLOSE_PAREN':([29,43,51,53,73,74,75,77,78,96,101,103,104,116,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,135,136,141,152,154,157,158,159,160,161,162,163,164,166,169,170,172,173,174,175,176,177,184,187,190,191,193,194,196,197,202,203,205,208,210,215,217,219,220,225,226,227,231,232,233,234,235,236,237,238,242,243,244,245,248,249,250,255,256,],[35,-137,76,-15,-44,-45,-46,-137,-18,-49,-14,-17,-19,-95,-96,-98,-101,-112,-118,-123,-124,-130,-131,-132,-135,-61,-67,-68,165,168,-90,-137,-109,-115,-125,-126,-127,-133,-134,-137,-137,-137,199,-137,-48,-137,-136,209,-97,-99,-102,-110,-116,215,216,-60,218,-66,221,225,-94,-93,-16,-100,-129,-61,-67,-68,-87,-137,-94,-113,-114,-119,-120,-122,-137,-137,-137,-86,-91,-137,-47,-59,-64,-65,-85,-92,]),'CT_INT':([34,56,90,92,93,97,99,105,116,117,118,119,120,121,122,123,124,125,126,127,128,133,136,143,144,145,146,147,148,149,150,151,152,154,156,157,158,159,160,161,167,169,173,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,195,203,204,206,210,211,212,213,214,215,225,226,227,231,232,233,234,235,241,242,244,255,],[41,82,125,125,125,125,125,125,-95,-96,-98,-101,-112,-118,-128,-123,-124,-130,-131,-132,-135,125,-90,125,125,125,-121,-121,-121,-121,-121,-121,-109,-115,125,-125,-126,-127,-133,-134,125,125,-136,-97,-99,-102,-103,-104,-105,-106,-107,-108,-110,-121,-121,-116,-121,-121,125,-94,125,125,-100,125,125,125,125,-129,-87,125,-94,-113,-114,-119,-120,-122,125,-86,125,-85,]),'CLOSE_BRACKETS':([41,82,120,121,123,124,125,126,127,128,137,140,152,154,157,158,159,160,161,173,184,187,215,225,228,231,232,233,234,235,242,255,],[48,109,-112,-118,-123,-124,-130,-131,-132,-135,170,173,-109,-115,-125,-126,-127,-133,-134,-136,-110,-116,-129,-87,245,-113,-114,-119,-120,-122,-86,-85,]),'READ':([50,61,83,84,85,86,88,89,239,251,253,259,262,265,266,268,],[66,66,-20,66,66,66,66,66,-69,-70,-78,-72,-69,-71,-82,-73,]),'WRITE':([50,61,83,84,85,86,88,89,239,251,253,259,262,265,266,268,],[67,67,-20,67,67,67,67,67,-69,-70,-78,-72,-69,-71,-82,-73,]),'IF':([50,61,83,84,85,86,88,89,239,251,253,259,262,265,266,268,],[68,68,-20,68,68,68,68,68,-69,-70,-78,-72,-69,-71,-82,-73,]),'WHILE':([50,61,83,84,85,86,88,89,239,251,253,259,262,265,266,268,],[69,69,-20,69,69,69,69,69,-69,-70,-78,-72,-69,-71,-82,-73,]),'FOR':([50,61,83,84,85,86,88,89,239,251,253,259,262,265,266,268,],[70,70,-20,70,70,70,70,70,-69,-70,-78,-72,-69,-71,-82,-73,]),'RETURN':([50,61,83,84,85,86,88,89,239,251,253,259,262,265,266,268,],[71,71,-20,71,71,71,71,71,-69,-70,-78,-72,-69,-71,-82,-73,]),'CLOSE_BRACES':([50,57,61,64,83,84,85,86,87,88,89,110,111,112,113,114,239,251,253,259,262,265,266,268,],[-137,83,-137,-56,-20,-137,-137,-137,-53,-137,-137,-50,-51,-52,-54,-55,-69,-70,-78,-72,-69,-71,-82,-73,]),'ASSIGN':([65,72,73,74,75,95,96,134,170,245,],[90,-49,-44,-45,-46,-79,-49,167,-48,-47,]),'ELSE':([83,239,],[-20,252,]),'CT_FLOAT':([90,92,93,97,99,105,116,117,118,119,120,121,122,123,124,125,126,127,128,133,136,143,144,145,146,147,148,149,150,151,152,154,156,157,158,159,160,161,167,169,173,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,195,203,204,206,210,211,212,213,214,215,225,226,227,231,232,233,234,235,241,242,244,255,],[126,126,126,126,126,126,-95,-96,-98,-101,-112,-118,-128,-123,-124,-130,-131,-132,-135,126,-90,126,126,126,-121,-121,-121,-121,-121,-121,-109,-115,126,-125,-126,-127,-133,-134,126,126,-136,-97,-99,-102,-103,-104,-105,-106,-107,-108,-110,-121,-121,-116,-121,-121,126,-94,126,126,-100,126,126,126,126,-129,-87,126,-94,-113,-114,-119,-120,-122,126,-86,126,-85,]),'CT_CHAR':([90,92,93,97,99,105,116,117,118,119,120,121,122,123,124,125,126,127,128,133,136,143,144,145,146,147,148,149,150,151,152,154,156,157,158,159,160,161,167,169,173,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,195,203,204,206,210,211,212,213,214,215,225,226,227,231,232,233,234,235,241,242,244,255,],[127,127,127,127,127,127,-95,-96,-98,-101,-112,-118,-128,-123,-124,-130,-131,-132,-135,127,-90,127,127,127,-121,-121,-121,-121,-121,-121,-109,-115,127,-125,-126,-127,-133,-134,127,127,-136,-97,-99,-102,-103,-104,-105,-106,-107,-108,-110,-121,-121,-116,-121,-121,127,-94,127,127,-100,127,127,127,127,-129,-87,127,-94,-113,-114,-119,-120,-122,127,-86,127,-85,]),'CT_STRING':([92,195,],[130,219,]),'TO':([116,117,118,119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,175,176,177,184,187,200,210,215,224,225,231,232,233,234,235,242,255,],[-95,-96,-98,-101,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-97,-99,-102,-110,-116,-80,-100,-129,241,-87,-113,-114,-119,-120,-122,-86,-85,]),'DO':([116,117,118,119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,175,176,177,184,187,199,210,215,223,225,231,232,233,234,235,242,254,255,260,],[-95,-96,-98,-101,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-97,-99,-102,-110,-116,-77,-100,-129,240,-87,-113,-114,-119,-120,-122,-86,-81,-85,263,]),'OR':([117,118,119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,176,177,184,187,210,215,225,231,232,233,234,235,242,255,],[143,-98,-101,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-99,-102,-110,-116,-100,-129,-87,-113,-114,-119,-120,-122,-86,-85,]),'AND':([118,119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,177,184,187,210,215,225,231,232,233,234,235,242,255,],[144,-101,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-102,-110,-116,-100,-129,-87,-113,-114,-119,-120,-122,-86,-85,]),'LESS_THAN':([119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,184,187,215,225,231,232,233,234,235,242,255,],[146,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-110,-116,-129,-87,-113,-114,-119,-120,-122,-86,-85,]),'LESS_THAN_EQUAL':([119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,184,187,215,225,231,232,233,234,235,242,255,],[147,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-110,-116,-129,-87,-113,-114,-119,-120,-122,-86,-85,]),'MORE_THAN':([119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,184,187,215,225,231,232,233,234,235,242,255,],[148,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-110,-116,-129,-87,-113,-114,-119,-120,-122,-86,-85,]),'MORE_THAN_EQUAL':([119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,184,187,215,225,231,232,233,234,235,242,255,],[149,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-110,-116,-129,-87,-113,-114,-119,-120,-122,-86,-85,]),'EQUALS':([119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,184,187,215,225,231,232,233,234,235,242,255,],[150,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-110,-116,-129,-87,-113,-114,-119,-120,-122,-86,-85,]),'NOT_EQUALS':([119,120,121,123,124,125,126,127,128,152,154,157,158,159,160,161,173,184,187,215,225,231,232,233,234,235,242,255,],[151,-112,-118,-123,-124,-130,-131,-132,-135,-109,-115,-125,-126,-127,-133,-134,-136,-110,-116,-129,-87,-113,-114,-119,-120,-122,-86,-85,]),'PLUS':([120,121,123,124,125,126,127,128,153,154,157,158,159,160,161,173,187,215,225,233,234,235,242,255,],[-111,-118,-123,-124,-130,-131,-132,-135,185,-115,-125,-126,-127,-133,-134,-136,-116,-129,-87,-119,-120,-122,-86,-85,]),'MINUS':([120,121,123,124,125,126,127,128,153,154,157,158,159,160,161,173,187,215,225,233,234,235,242,255,],[-111,-118,-123,-124,-130,-131,-132,-135,186,-115,-125,-126,-127,-133,-134,-136,-116,-129,-87,-119,-120,-122,-86,-85,]),'MULTIPLIES':([121,123,124,125,126,127,128,155,157,158,159,160,161,173,215,225,235,242,255,],[-117,-123,-124,-130,-131,-132,-135,188,-125,-126,-127,-133,-134,-136,-129,-87,-122,-86,-85,]),'DIVIDE':([121,123,124,125,126,127,128,155,157,158,159,160,161,173,215,225,235,242,255,],[-117,-123,-124,-130,-131,-132,-135,189,-125,-126,-127,-133,-134,-136,-129,-87,-122,-86,-85,]),'THEN':([165,198,],[-74,222,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'g_main_quad':([2,],[3,]),'add_program':([4,],[5,]),'vars':([6,100,230,],[7,138,247,]),'empty':([6,7,23,40,43,50,55,61,77,84,85,86,88,89,100,141,162,163,164,169,172,226,229,230,236,237,238,244,264,],[9,12,33,33,53,64,33,64,103,64,64,64,64,64,9,53,193,196,196,205,103,205,12,9,193,196,196,205,12,]),'funcs':([7,229,264,],[10,246,267,]),'func_type':([7,229,264,],[11,11,11,]),'var_type':([7,8,38,43,102,108,141,229,264,],[13,19,44,52,139,44,52,13,13,]),'var_comp':([8,],[18,]),'main':([10,],[20,]),'ids_dec':([19,32,44,],[23,40,55,]),'ids_dec_matrix':([19,32,44,],[24,24,24,]),'ids_dec_array':([19,32,44,],[25,25,25,]),'ids_dec_single':([19,32,44,],[26,26,26,]),'end_program':([20,],[28,]),'var_comp_2':([23,40,55,],[31,47,81,]),'add_module':([30,80,],[36,106,]),'var_comp_final':([31,81,],[37,107,]),'var_module_trans':([31,81,],[39,39,]),'fill_main_quad':([35,],[42,]),'var_comp_recursive':([38,108,],[45,142,]),'var_comp_3':([40,],[46,]),'block':([42,171,222,240,257,258,263,],[49,207,239,253,261,262,266,]),'funcs_params':([43,141,],[51,174,]),'statements':([50,61,84,85,86,88,89,],[57,87,110,111,112,113,114,]),'assignment':([50,61,84,85,86,88,89,],[58,58,58,58,58,58,58,]),'read':([50,61,84,85,86,88,89,],[59,59,59,59,59,59,59,]),'write':([50,61,84,85,86,88,89,],[60,60,60,60,60,60,60,]),'condition':([50,61,84,85,86,88,89,],[61,61,61,61,61,61,61,]),'return':([50,61,84,85,86,88,89,],[62,62,62,62,62,62,62,]),'func_call':([50,61,84,85,86,88,89,90,92,93,97,99,105,133,143,144,145,156,167,169,195,204,206,211,212,213,214,226,241,244,],[63,63,63,63,63,63,63,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,]),'ids':([50,61,70,84,85,86,88,89,91,192,],[65,65,95,65,65,65,65,65,129,217,]),'ids_matrix':([50,61,70,84,85,86,88,89,91,192,],[73,73,73,73,73,73,73,73,73,73,]),'ids_array':([50,61,70,84,85,86,88,89,91,192,],[74,74,74,74,74,74,74,74,74,74,]),'ids_single':([50,61,70,84,85,86,88,89,91,192,],[75,75,75,75,75,75,75,75,75,75,]),'variable_params':([52,139,],[77,172,]),'funcs_comp':([54,],[79,]),'while_jump':([69,],[94,]),'verify_function_exists':([72,128,],[98,98,]),'add_parameter_amount':([76,209,],[100,230,]),'funcs_params_comp':([77,172,],[101,208,]),'dim':([78,128,],[104,161,]),'expressions':([90,92,93,97,133,156,167,169,195,204,226,241,244,],[115,131,132,135,166,190,200,203,220,227,203,254,203,]),'expressions_comp':([90,92,93,97,133,143,156,167,169,195,204,226,241,244,],[116,116,116,116,116,175,116,116,116,116,116,116,116,116,]),'expression_comp_2':([90,92,93,97,133,143,144,156,167,169,195,204,226,241,244,],[117,117,117,117,117,117,176,117,117,117,117,117,117,117,117,]),'expression_comp_3':([90,92,93,97,133,143,144,156,167,169,195,204,226,241,244,],[118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,]),'exp':([90,92,93,97,99,105,133,143,144,145,156,167,169,195,204,206,211,212,226,241,244,],[119,119,119,119,137,140,119,119,119,177,119,119,119,119,119,228,231,232,119,119,119,]),'term':([90,92,93,97,99,105,133,143,144,145,156,167,169,195,204,206,211,212,213,214,226,241,244,],[120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,233,234,120,120,120,]),'factor':([90,92,93,97,99,105,133,143,144,145,156,167,169,195,204,206,211,212,213,214,226,241,244,],[121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,]),'variable':([90,92,93,97,99,105,133,143,144,145,156,167,169,195,204,206,211,212,213,214,226,241,244,],[123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,]),'validate_for':([95,],[134,]),'expressions_op':([119,],[145,]),'g_quad_exp_as_alone':([120,],[152,]),'g_quad_exp_as':([120,],[153,]),'g_quad_exp_md_alone':([121,],[154,]),'g_quad_exp_md':([121,],[155,]),'add_fake':([122,],[156,]),'add_ct_int':([125,],[157,]),'add_ct_float':([126,],[158,]),'add_ct_char':([127,],[159,]),'add_id':([128,],[160,]),'g_quad_read':([129,217,],[162,236,]),'g_quad_write_str':([130,219,],[163,237,]),'g_quad_write':([131,220,],[164,238,]),'era_activation':([136,],[169,]),'count_local_vars':([138,247,],[171,257,]),'add_op':([146,147,148,149,150,151,185,186,188,189,],[178,179,180,181,182,183,211,212,213,214,]),'exp_comp':([153,],[184,]),'term_comp':([155,],[187,]),'read_comp':([162,236,],[191,248,]),'write_comp':([163,164,237,238,],[194,197,249,250,]),'g_if_quad':([165,],[198,]),'g_quad_return':([168,],[201,]),'func_call_comp':([169,226,244,],[202,243,256,]),'g_quad_logic':([177,],[210,]),'g_while_quad':([199,],[223,]),'for_counter_control':([200,],[224,]),'g_parameter_quad':([203,227,],[226,244,]),'end_funcs':([207,261,],[229,264,]),'rem_fake':([215,],[235,]),'g_gosub_quad':([225,],[242,]),'end_if':([239,262,],[251,265,]),'function_call_end':([242,],[255,]),'g_else_quad':([252,],[258,]),'end_while':([253,],[259,]),'for_counter_end':([254,],[260,]),'end_for':([266,],[268,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM g_main_quad ID add_program SEMICOLON vars funcs main end_program','program',9,'p_program','parser.py',63),
  ('add_program -> <empty>','add_program',0,'p_add_program','parser.py',66),
  ('end_program -> <empty>','end_program',0,'p_end_program','parser.py',83),
  ('main -> MAIN OPEN_PAREN CLOSE_PAREN fill_main_quad block','main',5,'p_main','parser.py',97),
  ('g_main_quad -> <empty>','g_main_quad',0,'p_g_main_quad','parser.py',100),
  ('fill_main_quad -> <empty>','fill_main_quad',0,'p_fill_main_quad','parser.py',106),
  ('funcs -> func_type MODULE ID add_module OPEN_PAREN funcs_params CLOSE_PAREN add_parameter_amount vars count_local_vars block end_funcs funcs','funcs',13,'p_funcs','parser.py',111),
  ('funcs -> empty','funcs',1,'p_funcs','parser.py',112),
  ('end_funcs -> <empty>','end_funcs',0,'p_end_funcs','parser.py',116),
  ('count_local_vars -> <empty>','count_local_vars',0,'p_count_local_vars','parser.py',127),
  ('add_module -> <empty>','add_module',0,'p_add_module','parser.py',137),
  ('funcs_comp -> ID add_module OPEN_PAREN funcs_params CLOSE_PAREN add_parameter_amount vars count_local_vars block end_funcs funcs','funcs_comp',11,'p_funcs_comp','parser.py',167),
  ('add_parameter_amount -> <empty>','add_parameter_amount',0,'p_add_parameter_amount','parser.py',170),
  ('funcs_params -> var_type variable_params funcs_params_comp','funcs_params',3,'p_funcs_params','parser.py',177),
  ('funcs_params -> empty','funcs_params',1,'p_funcs_params','parser.py',178),
  ('funcs_params_comp -> COMMA var_type variable_params funcs_params_comp','funcs_params_comp',4,'p_funcs_params_comp','parser.py',183),
  ('funcs_params_comp -> empty','funcs_params_comp',1,'p_funcs_params_comp','parser.py',184),
  ('variable_params -> ID','variable_params',1,'p_variable_params','parser.py',189),
  ('variable_params -> ID dim','variable_params',2,'p_variable_params','parser.py',190),
  ('block -> OPEN_BRACES statements CLOSE_BRACES','block',3,'p_block','parser.py',202),
  ('func_type -> var_type','func_type',1,'p_func_type','parser.py',206),
  ('func_type -> VOID','func_type',1,'p_func_type','parser.py',207),
  ('var_type -> INT','var_type',1,'p_var_type','parser.py',215),
  ('var_type -> FLOAT','var_type',1,'p_var_type','parser.py',216),
  ('var_type -> CHAR','var_type',1,'p_var_type','parser.py',217),
  ('vars -> VARS var_comp','vars',2,'p_vars','parser.py',225),
  ('vars -> empty','vars',1,'p_vars','parser.py',226),
  ('var_comp -> var_type ids_dec var_comp_2 var_comp_final','var_comp',4,'p_var_comp','parser.py',231),
  ('var_comp -> var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive','var_comp',5,'p_var_comp','parser.py',232),
  ('var_comp_2 -> COMMA ids_dec var_comp_3','var_comp_2',3,'p_var_comp_2','parser.py',236),
  ('var_comp_2 -> empty','var_comp_2',1,'p_var_comp_2','parser.py',237),
  ('var_comp_3 -> var_comp_2','var_comp_3',1,'p_var_comp_3','parser.py',241),
  ('var_comp_recursive -> var_type ids_dec var_comp_2 var_comp_final','var_comp_recursive',4,'p_var_comp_recursive','parser.py',244),
  ('var_comp_recursive -> var_type ids_dec var_comp_2 SEMICOLON var_comp_recursive','var_comp_recursive',5,'p_var_comp_recursive','parser.py',245),
  ('var_comp_final -> SEMICOLON','var_comp_final',1,'p_var_comp_final','parser.py',249),
  ('var_comp_final -> var_module_trans','var_comp_final',1,'p_var_comp_final','parser.py',250),
  ('var_module_trans -> SEMICOLON var_type MODULE funcs_comp','var_module_trans',4,'p_var_module_trans','parser.py',255),
  ('ids_dec -> ids_dec_matrix','ids_dec',1,'p_ids_dec','parser.py',260),
  ('ids_dec -> ids_dec_array','ids_dec',1,'p_ids_dec','parser.py',261),
  ('ids_dec -> ids_dec_single','ids_dec',1,'p_ids_dec','parser.py',262),
  ('ids_dec_matrix -> ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS OPEN_BRACKETS CT_INT CLOSE_BRACKETS','ids_dec_matrix',7,'p_ids_dec_matrix','parser.py',266),
  ('ids_dec_array -> ID OPEN_BRACKETS CT_INT CLOSE_BRACKETS','ids_dec_array',4,'p_ids_dec_array','parser.py',281),
  ('ids_dec_single -> ID','ids_dec_single',1,'p_ids_dec_single','parser.py',295),
  ('ids -> ids_matrix','ids',1,'p_ids','parser.py',308),
  ('ids -> ids_array','ids',1,'p_ids','parser.py',309),
  ('ids -> ids_single','ids',1,'p_ids','parser.py',310),
  ('ids_matrix -> ID OPEN_BRACKETS exp CLOSE_BRACKETS OPEN_BRACKETS exp CLOSE_BRACKETS','ids_matrix',7,'p_ids_matrix','parser.py',314),
  ('ids_array -> ID OPEN_BRACKETS exp CLOSE_BRACKETS','ids_array',4,'p_ids_array','parser.py',319),
  ('ids_single -> ID','ids_single',1,'p_ids_single','parser.py',324),
  ('statements -> assignment SEMICOLON statements','statements',3,'p_statements','parser.py',330),
  ('statements -> read SEMICOLON statements','statements',3,'p_statements','parser.py',331),
  ('statements -> write SEMICOLON statements','statements',3,'p_statements','parser.py',332),
  ('statements -> condition statements','statements',2,'p_statements','parser.py',333),
  ('statements -> return SEMICOLON statements','statements',3,'p_statements','parser.py',334),
  ('statements -> func_call SEMICOLON statements','statements',3,'p_statements','parser.py',335),
  ('statements -> empty','statements',1,'p_statements','parser.py',336),
  ('assignment -> ids ASSIGN expressions','assignment',3,'p_assignment','parser.py',341),
  ('read -> READ OPEN_PAREN ids g_quad_read read_comp CLOSE_PAREN','read',6,'p_read','parser.py',393),
  ('read_comp -> COMMA ids g_quad_read read_comp','read_comp',4,'p_read_comp','parser.py',398),
  ('read_comp -> empty','read_comp',1,'p_read_comp','parser.py',399),
  ('g_quad_read -> <empty>','g_quad_read',0,'p_g_quad_read','parser.py',404),
  ('write -> WRITE OPEN_PAREN CT_STRING g_quad_write_str write_comp CLOSE_PAREN','write',6,'p_write','parser.py',418),
  ('write -> WRITE OPEN_PAREN expressions g_quad_write write_comp CLOSE_PAREN','write',6,'p_write','parser.py',419),
  ('write_comp -> COMMA CT_STRING g_quad_write_str write_comp','write_comp',4,'p_write_comp','parser.py',424),
  ('write_comp -> COMMA expressions g_quad_write write_comp','write_comp',4,'p_write_comp','parser.py',425),
  ('write_comp -> empty','write_comp',1,'p_write_comp','parser.py',426),
  ('g_quad_write_str -> <empty>','g_quad_write_str',0,'p_g_quad_write_str','parser.py',431),
  ('g_quad_write -> <empty>','g_quad_write',0,'p_g_quad_write','parser.py',438),
  ('end_if -> <empty>','end_if',0,'p_end_if','parser.py',445),
  ('condition -> IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block end_if','condition',8,'p_condition','parser.py',451),
  ('condition -> IF OPEN_PAREN expressions CLOSE_PAREN g_if_quad THEN block ELSE g_else_quad block end_if','condition',11,'p_condition','parser.py',452),
  ('condition -> WHILE while_jump OPEN_PAREN expressions CLOSE_PAREN g_while_quad DO block end_while','condition',9,'p_condition','parser.py',453),
  ('condition -> FOR ids validate_for ASSIGN expressions for_counter_control TO expressions for_counter_end DO block end_for','condition',12,'p_condition','parser.py',454),
  ('g_if_quad -> <empty>','g_if_quad',0,'p_g_if_quad','parser.py',459),
  ('g_else_quad -> <empty>','g_else_quad',0,'p_g_else_quad','parser.py',472),
  ('while_jump -> <empty>','while_jump',0,'p_while_jump','parser.py',485),
  ('g_while_quad -> <empty>','g_while_quad',0,'p_g_while_quad','parser.py',490),
  ('end_while -> <empty>','end_while',0,'p_end_while','parser.py',501),
  ('validate_for -> <empty>','validate_for',0,'p_validate_for','parser.py',509),
  ('for_counter_control -> <empty>','for_counter_control',0,'p_for_counter_control','parser.py',532),
  ('for_counter_end -> <empty>','for_counter_end',0,'p_for_counter_end','parser.py',556),
  ('end_for -> <empty>','end_for',0,'p_end_for','parser.py',580),
  ('return -> RETURN OPEN_PAREN expressions CLOSE_PAREN g_quad_return','return',5,'p_return','parser.py',596),
  ('g_quad_return -> <empty>','g_quad_return',0,'p_g_quad_return','parser.py',599),
  ('func_call -> ID verify_function_exists OPEN_PAREN era_activation func_call_comp CLOSE_PAREN g_gosub_quad function_call_end','func_call',8,'p_func_call','parser.py',611),
  ('function_call_end -> <empty>','function_call_end',0,'p_function_call_end','parser.py',615),
  ('g_gosub_quad -> <empty>','g_gosub_quad',0,'p_g_gosub_quad','parser.py',629),
  ('change_to_global -> <empty>','change_to_global',0,'p_change_to_global','parser.py',634),
  ('verify_function_exists -> <empty>','verify_function_exists',0,'p_verify_function_exists','parser.py',639),
  ('era_activation -> <empty>','era_activation',0,'p_era_activation','parser.py',648),
  ('func_call_comp -> expressions g_parameter_quad func_call_comp','func_call_comp',3,'p_func_call_comp','parser.py',655),
  ('func_call_comp -> COMMA expressions g_parameter_quad func_call_comp','func_call_comp',4,'p_func_call_comp','parser.py',656),
  ('func_call_comp -> empty','func_call_comp',1,'p_func_call_comp','parser.py',657),
  ('g_parameter_quad -> <empty>','g_parameter_quad',0,'p_g_parameter_quad','parser.py',661),
  ('expressions -> expressions_comp','expressions',1,'p_expressions','parser.py',695),
  ('expressions_comp -> expression_comp_2','expressions_comp',1,'p_expressions_comp','parser.py',699),
  ('expressions_comp -> expression_comp_2 OR expressions_comp','expressions_comp',3,'p_expressions_comp','parser.py',700),
  ('expression_comp_2 -> expression_comp_3','expression_comp_2',1,'p_expression_comp_2','parser.py',705),
  ('expression_comp_2 -> expression_comp_3 AND expression_comp_2','expression_comp_2',3,'p_expression_comp_2','parser.py',706),
  ('expression_comp_3 -> exp expressions_op exp g_quad_logic','expression_comp_3',4,'p_expression_comp_3','parser.py',711),
  ('expression_comp_3 -> exp','expression_comp_3',1,'p_expression_comp_3','parser.py',712),
  ('g_quad_logic -> <empty>','g_quad_logic',0,'p_g_quad_logic','parser.py',716),
  ('expressions_op -> LESS_THAN add_op','expressions_op',2,'p_expressions_op','parser.py',721),
  ('expressions_op -> LESS_THAN_EQUAL add_op','expressions_op',2,'p_expressions_op','parser.py',722),
  ('expressions_op -> MORE_THAN add_op','expressions_op',2,'p_expressions_op','parser.py',723),
  ('expressions_op -> MORE_THAN_EQUAL add_op','expressions_op',2,'p_expressions_op','parser.py',724),
  ('expressions_op -> EQUALS add_op','expressions_op',2,'p_expressions_op','parser.py',725),
  ('expressions_op -> NOT_EQUALS add_op','expressions_op',2,'p_expressions_op','parser.py',726),
  ('exp -> term g_quad_exp_as_alone','exp',2,'p_exp','parser.py',732),
  ('exp -> term g_quad_exp_as exp_comp','exp',3,'p_exp','parser.py',733),
  ('g_quad_exp_as -> <empty>','g_quad_exp_as',0,'p_g_quad_exp_as','parser.py',738),
  ('g_quad_exp_as_alone -> <empty>','g_quad_exp_as_alone',0,'p_g_quad_exp_as_alone','parser.py',742),
  ('exp_comp -> PLUS add_op exp','exp_comp',3,'p_exp_comp','parser.py',747),
  ('exp_comp -> MINUS add_op exp','exp_comp',3,'p_exp_comp','parser.py',748),
  ('term -> factor g_quad_exp_md_alone','term',2,'p_term','parser.py',753),
  ('term -> factor g_quad_exp_md term_comp','term',3,'p_term','parser.py',754),
  ('g_quad_exp_md -> <empty>','g_quad_exp_md',0,'p_g_quad_exp_md','parser.py',759),
  ('g_quad_exp_md_alone -> <empty>','g_quad_exp_md_alone',0,'p_g_quad_exp_md_alone','parser.py',764),
  ('term_comp -> MULTIPLIES add_op term','term_comp',3,'p_term_comp','parser.py',769),
  ('term_comp -> DIVIDE add_op term','term_comp',3,'p_term_comp','parser.py',770),
  ('add_op -> <empty>','add_op',0,'p_add_op','parser.py',774),
  ('factor -> OPEN_PAREN add_fake expressions CLOSE_PAREN rem_fake','factor',5,'p_factor','parser.py',951),
  ('factor -> variable','factor',1,'p_factor','parser.py',952),
  ('factor -> func_call','factor',1,'p_factor','parser.py',953),
  ('factor -> CT_INT add_ct_int','factor',2,'p_factor','parser.py',954),
  ('factor -> CT_FLOAT add_ct_float','factor',2,'p_factor','parser.py',955),
  ('factor -> CT_CHAR add_ct_char','factor',2,'p_factor','parser.py',956),
  ('add_fake -> <empty>','add_fake',0,'p_add_fake','parser.py',960),
  ('rem_fake -> <empty>','rem_fake',0,'p_rem_fake','parser.py',964),
  ('add_ct_int -> <empty>','add_ct_int',0,'p_add_ct_int','parser.py',969),
  ('add_ct_float -> <empty>','add_ct_float',0,'p_add_ct_float','parser.py',976),
  ('add_ct_char -> <empty>','add_ct_char',0,'p_add_ct_char','parser.py',983),
  ('variable -> ID add_id','variable',2,'p_variable','parser.py',991),
  ('variable -> ID dim','variable',2,'p_variable','parser.py',992),
  ('add_id -> <empty>','add_id',0,'p_add_id','parser.py',997),
  ('dim -> OPEN_BRACKETS exp CLOSE_BRACKETS','dim',3,'p_dim','parser.py',1018),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',1023),
]
