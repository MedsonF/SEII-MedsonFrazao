import os

print(dir(os))

print(os.getcwd())

os.chdir('A:\Users\medson\Documents\1FACULDADE\11º sem\SEMB2')
print(os.getcwd())

import os
os.chdir('A:\Users\medson\Documents\1FACULDADE\11º sem\SEMB2')
os.makedirs('OS-Demo-2/Sub-Dir-1')
print(os.listdir())


import os
os.chdir('A:\Users\medson\Documents\1FACULDADE\11º sem\SEMB2')
os.removedirs('OS-Demo-2/Sub-Dir-1')
print(os.listdir())



import os
os.chdir('A:\Users\medson\Documents\1FACULDADE\11º sem\SEMB2')
os.rename('OS-Demo-2', 'OS-Demo-1')
print(os.listdir())


import os
os.chdir('A:\Users\medson\Documents\1FACULDADE\11º sem\SEMB2')
os.stat('OS-Demo-1')
print(os.listdir())