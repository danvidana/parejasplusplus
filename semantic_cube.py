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
