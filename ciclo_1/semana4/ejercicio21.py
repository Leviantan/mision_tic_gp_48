# libreria pandas
import pandas as pd

'''
s = pd.Series([7,6,5], index=['Ene','Feb','Mar'])
print(s)
'''

# Utilizando diccionarios

'''
d = { 'Ene': 7, 'Feb': 5, 'Mar':4}
s = pd.Series(d, index=['Abr','Mar','Feb','Ene'], dtype=int)
print(s)
'''

# Utilizar un escalar

s = pd.Series(9,index=['Ene','Feb','Mar'])
print(s)