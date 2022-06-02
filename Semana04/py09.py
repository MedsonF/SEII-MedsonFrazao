
import sys
sys.path.append('/Users/medson/Desktop/My-Modules')

from my_module import find_index, test

materias = ['His', 'Mat', 'Fis', 'Comp']

index = find_index(materias, 'Mat')

print(sys.path)

import random
materias = ['His', 'Mat', 'Fis', 'Comp']
random_course = random.choice(materias)
print(random_course)


import math
materias = ['His', 'Mat', 'Fis', 'Comp']
rads = math.radians(90)
print(rads)


import math
materias = ['His', 'Mat', 'Fis', 'Comp']
rads = math.radians(90)
print(math.sin(rads))


import datetime
import calendario
materias = ['His', 'Mat', 'Fis', 'Comp']
today = datetime.date.today()
print(today)


import datetime
import calendario
materias = ['His', 'Mat', 'Fis', 'Comp']
today = datetime.date.today()
print(today)
print(calendario.isleap(2017))


import datetime
import calendario
materias = ['His', 'Mat', 'Fis', 'Comp']
today = datetime.date.today()
print(today)
print(calendario.isleap(2020))


import os
materias = ['His', 'Mat', 'Fis', 'Comp']
print(os.getcwd())


import os
materias = ['His', 'Mat', 'Fis', 'Comp']
print(os.__file__)


import antigravity