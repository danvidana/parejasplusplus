# Cubo Semantico
# El cubo semantico es un dictionary de python

from collections import defaultdict

#Retornos no acepatados regruesan None
semantic_cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

# +
# -
# *
# /
# =
# ==
# !=
# >
# >=
# <
# <=
# &&
# ||

#INT
semantic_cube['int']['+']['int'] = 'int'
semantic_cube['int']['-']['int'] = 'int'
semantic_cube['int']['*']['int'] = 'int'
semantic_cube['int']['/']['int'] = 'int'
semantic_cube['int']['=']['int'] = 'int'
semantic_cube['int']['==']['int'] = 'bool'
semantic_cube['int']['!=']['int'] = 'bool'
semantic_cube['int']['>']['int'] = 'bool'
semantic_cube['int']['>=']['int'] = 'bool'
semantic_cube['int']['<']['int'] = 'bool'
semantic_cube['int']['<=']['int'] = 'bool'
#semantic_cube['int']['&&']['int'] = 'bool'
#semantic_cube['int']['||']['int'] = 'bool'

#INT - FLOAT
semantic_cube['int']['+']['float'] = 'float'
semantic_cube['int']['-']['float'] = 'float'
semantic_cube['int']['*']['float'] = 'float'
semantic_cube['int']['/']['float'] = 'float'
semantic_cube['int']['=']['float'] = 'int'
#semantic_cube['int']['==']['float'] = 'bool'
#semantic_cube['int']['!=']['float'] = 'int'
semantic_cube['int']['>']['float'] = 'bool'
semantic_cube['int']['>=']['float'] = 'bool'
semantic_cube['int']['<']['float'] = 'bool'
semantic_cube['int']['<=']['float'] = 'bool'
#semantic_cube['int']['&&']['float'] = 'bool'
#semantic_cube['int']['||']['float'] = 'bool'

#FLOAT
semantic_cube['float']['+']['float'] = 'float'
semantic_cube['float']['-']['float'] = 'float'
semantic_cube['float']['*']['float'] = 'float'
semantic_cube['float']['/']['float'] = 'float'
semantic_cube['float']['=']['float'] = 'float'
semantic_cube['float']['==']['float'] = 'bool'
semantic_cube['float']['!=']['float'] = 'bool'
semantic_cube['float']['>']['float'] = 'bool'
semantic_cube['float']['>=']['float'] = 'bool'
semantic_cube['float']['<']['float'] = 'bool'
semantic_cube['float']['<=']['float'] = 'bool'
#semantic_cube['float']['&&']['float'] = 'bool'
#semantic_cube['float']['||']['float'] = 'bool'

#FLOAT - INT
semantic_cube['float']['+']['int'] = 'float'
semantic_cube['float']['-']['int'] = 'float'
semantic_cube['float']['*']['int'] = 'float'
semantic_cube['float']['/']['int'] = 'float'
semantic_cube['float']['=']['int'] = 'float'
#semantic_cube['float']['==']['int'] = 'int'
#semantic_cube['float']['!=']['int'] = 'int'
semantic_cube['float']['>']['int'] = 'bool'
semantic_cube['float']['>=']['int'] = 'bool'
semantic_cube['float']['<']['int'] = 'bool'
semantic_cube['float']['<=']['int'] = 'bool'
#semantic_cube['float']['&&']['int'] = 'bool'
#semantic_cube['float']['||']['int'] = 'bool'

#CHAR
semantic_cube['char']['=']['char'] = 'char'
semantic_cube['char']['==']['char'] = 'bool'
semantic_cube['char']['!=']['char'] = 'bool'


#CT_INT
semantic_cube['ct_int']['+']['ct_int'] = 'int'
semantic_cube['ct_int']['-']['ct_int'] = 'int'
semantic_cube['ct_int']['*']['ct_int'] = 'int'
semantic_cube['ct_int']['/']['ct_int'] = 'int'
semantic_cube['ct_int']['=']['ct_int'] = 'int'
semantic_cube['ct_int']['==']['ct_int'] = 'bool'
semantic_cube['ct_int']['!=']['ct_int'] = 'bool'
semantic_cube['ct_int']['>']['ct_int'] = 'bool'
semantic_cube['ct_int']['>=']['ct_int'] = 'bool'
semantic_cube['ct_int']['<']['ct_int'] = 'bool'
semantic_cube['ct_int']['<=']['ct_int'] = 'bool'
#semantic_cube['int']['&&']['int'] = 'bool'
#semantic_cube['int']['||']['int'] = 'bool'

semantic_cube['ct_int']['+']['int'] = 'int'
semantic_cube['ct_int']['-']['int'] = 'int'
semantic_cube['ct_int']['*']['int'] = 'int'
semantic_cube['ct_int']['/']['int'] = 'int'
semantic_cube['ct_int']['=']['int'] = 'int'
semantic_cube['ct_int']['==']['int'] = 'bool'
semantic_cube['ct_int']['!=']['int'] = 'bool'
semantic_cube['ct_int']['>']['int'] = 'bool'
semantic_cube['ct_int']['>=']['int'] = 'bool'
semantic_cube['ct_int']['<']['int'] = 'bool'
semantic_cube['ct_int']['<=']['int'] = 'bool'
#semantic_cube['int']['&&']['int'] = 'bool'
#semantic_cube['int']['||']['int'] = 'bool'

semantic_cube['int']['+']['ct_int'] = 'int'
semantic_cube['int']['-']['ct_int'] = 'int'
semantic_cube['int']['*']['ct_int'] = 'int'
semantic_cube['int']['/']['ct_int'] = 'int'
semantic_cube['int']['=']['ct_int'] = 'int'
semantic_cube['int']['==']['ct_int'] = 'bool'
semantic_cube['int']['!=']['ct_int'] = 'bool'
semantic_cube['int']['>']['ct_int'] = 'bool'
semantic_cube['int']['>=']['ct_int'] = 'bool'
semantic_cube['int']['<']['ct_int'] = 'bool'
semantic_cube['int']['<=']['ct_int'] = 'bool'
#semantic_cube['int']['&&']['int'] = 'bool'
#semantic_cube['int']['||']['int'] = 'bool'

#INT - FLOAT
semantic_cube['ct_int']['+']['ct_float'] = 'float'
semantic_cube['ct_int']['-']['ct_float'] = 'float'
semantic_cube['ct_int']['*']['ct_float'] = 'float'
semantic_cube['ct_int']['/']['ct_float'] = 'float'
semantic_cube['ct_int']['=']['ct_float'] = 'int'
#semantic_cube['int']['==']['float'] = 'bool'
#semantic_cube['int']['!=']['float'] = 'int'
semantic_cube['ct_int']['>']['ct_float'] = 'bool'
semantic_cube['ct_int']['>=']['ct_float'] = 'bool'
semantic_cube['ct_int']['<']['ct_float'] = 'bool'
semantic_cube['ct_int']['<=']['ct_float'] = 'bool'
#semantic_cube['int']['&&']['float'] = 'bool'
#semantic_cube['int']['||']['float'] = 'bool'

#FLOAT
semantic_cube['ct_float']['+']['ct_float'] = 'float'
semantic_cube['ct_float']['-']['ct_float'] = 'float'
semantic_cube['ct_float']['*']['ct_float'] = 'float'
semantic_cube['ct_float']['/']['ct_float'] = 'float'
semantic_cube['ct_float']['=']['ct_float'] = 'float'
semantic_cube['ct_float']['==']['ct_float'] = 'bool'
semantic_cube['ct_float']['!=']['ct_float'] = 'bool'
semantic_cube['ct_float']['>']['ct_float'] = 'bool'
semantic_cube['ct_float']['>=']['ct_float'] = 'bool'
semantic_cube['ct_float']['<']['ct_float'] = 'bool'
semantic_cube['ct_float']['<=']['ct_float'] = 'bool'
#semantic_cube['float']['&&']['float'] = 'bool'
#semantic_cube['float']['||']['float'] = 'bool'

semantic_cube['float']['+']['ct_float'] = 'float'
semantic_cube['float']['-']['ct_float'] = 'float'
semantic_cube['float']['*']['ct_float'] = 'float'
semantic_cube['float']['/']['ct_float'] = 'float'
semantic_cube['float']['=']['ct_float'] = 'float'
semantic_cube['float']['==']['ct_float'] = 'bool'
semantic_cube['float']['!=']['ct_float'] = 'bool'
semantic_cube['float']['>']['ct_float'] = 'bool'
semantic_cube['float']['>=']['ct_float'] = 'bool'
semantic_cube['float']['<']['ct_float'] = 'bool'
semantic_cube['float']['<=']['ct_float'] = 'bool'
#semantic_cube['float']['&&']['float'] = 'bool'
#semantic_cube['float']['||']['float'] = 'bool'

semantic_cube['ct_float']['+']['float'] = 'float'
semantic_cube['ct_float']['-']['float'] = 'float'
semantic_cube['ct_float']['*']['float'] = 'float'
semantic_cube['ct_float']['/']['float'] = 'float'
semantic_cube['ct_float']['=']['float'] = 'float'
semantic_cube['ct_float']['==']['float'] = 'bool'
semantic_cube['ct_float']['!=']['float'] = 'bool'
semantic_cube['ct_float']['>']['float'] = 'bool'
semantic_cube['ct_float']['>=']['float'] = 'bool'
semantic_cube['ct_float']['<']['float'] = 'bool'
semantic_cube['ct_float']['<=']['float'] = 'bool'
#semantic_cube['float']['&&']['float'] = 'bool'
#semantic_cube['float']['||']['float'] = 'bool'

#FLOAT - INT
semantic_cube['ct_float']['+']['ct_int'] = 'float'
semantic_cube['ct_float']['-']['ct_int'] = 'float'
semantic_cube['ct_float']['*']['ct_int'] = 'float'
semantic_cube['ct_float']['/']['ct_int'] = 'float'
semantic_cube['ct_float']['=']['ct_int'] = 'float'
#semantic_cube['float']['==']['int'] = 'int'
#semantic_cube['float']['!=']['int'] = 'int'
semantic_cube['ct_float']['>']['ct_int'] = 'bool'
semantic_cube['ct_float']['>=']['ct_int'] = 'bool'
semantic_cube['ct_float']['<']['ct_int'] = 'bool'
semantic_cube['ct_float']['<=']['ct_int'] = 'bool'
#semantic_cube['float']['&&']['int'] = 'bool'
#semantic_cube['float']['||']['int'] = 'bool'

semantic_cube['ct_float']['+']['int'] = 'float'
semantic_cube['ct_float']['-']['int'] = 'float'
semantic_cube['ct_float']['*']['int'] = 'float'
semantic_cube['ct_float']['/']['int'] = 'float'
semantic_cube['ct_float']['=']['int'] = 'float'
#semantic_cube['float']['==']['int'] = 'int'
#semantic_cube['float']['!=']['int'] = 'int'
semantic_cube['ct_float']['>']['int'] = 'bool'
semantic_cube['ct_float']['>=']['int'] = 'bool'
semantic_cube['ct_float']['<']['int'] = 'bool'
semantic_cube['ct_float']['<=']['int'] = 'bool'
#semantic_cube['float']['&&']['int'] = 'bool'
#semantic_cube['float']['||']['int'] = 'bool'

#CHAR
semantic_cube['ct_char']['=']['ct_char'] = 'char'
semantic_cube['ct_char']['==']['ct_char'] = 'bool'
semantic_cube['ct_char']['!=']['ct_char'] = 'bool'

semantic_cube['ct_char']['=']['char'] = 'char'
semantic_cube['ct_char']['==']['char'] = 'bool'
semantic_cube['ct_char']['!=']['char'] = 'bool'

semantic_cube['char']['=']['ct_char'] = 'char'
semantic_cube['char']['==']['ct_char'] = 'bool'
semantic_cube['char']['!=']['ct_char'] = 'bool'