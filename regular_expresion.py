# metacaracteres = . ^ $ * + ? { } [ ] \ | ( )
# | == OU
# . == qualquer caractere (com exeção da quebra de linha)
# [] == um conjunto de caracteres
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

"""print(re.findall(r'João|Maria|adultos', texto))
print(re.findall(r'João|Maria|adu.tos', texto))
print(re.findall(r'[Jj]oão|[Mm]aria|adutos', texto))
print(re.findall(r'[a-zA-Z]aria', texto))
print(re.findall(r'jOão|MaRia', texto, flags=re.IGNORECASE))
"""
# Quantificadores
# * == 0 ou n vezes
# + == 1 ou n vezes
# ? == 0 ou 1 vez
# {n} == n vezes
# {min, max}

#print(re.findall(r'jO+ão', texto, flags=re.IGNORECASE))
#print(re.findall(r'jO?ão', texto, flags=re.IGNORECASE))
#print(re.findall(r'jO{1,}ão{1,}', texto, flags=re.IGNORECASE))
#print(re.findall(r'j[a-zA-Z]+ão', texto, flags=re.IGNORECASE))

text1 = """
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>1</div> 
"""

#print(re.findall(r'<[pdiv]{1,3}>', text1))
#print(re.findall(r'<[pdiv]{1,3}>.*', text1)) # greedy
#print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', text1))
#print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text1)) # non-greedy
#print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', text1)) # non-greedy

# GRUPOS E RETROVISORES

# grupo = ()
# retrovisoroes \1...
# () \1
# ()() \1 \2
# (()) \1 \2 

#print(re.findall(r'<([dpiv]{1,3})>.+?<\/\1>', text1))
#print(re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', text1))
print(re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', text1))
print(re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', text1))

cpf = '147.852.963-12         anything'

# ^ == começa com
# $ == termina com
# [^a-z] == Negação

#print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
#print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))

#print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 "\3" \4', text1))

# \w+ == [a-zA-ZÀ-ù]+ e mais outras coisas
# \W == Negação [^a-zA-ZÀ-ù]+
# \d == [0-9]
# \D == [^0-9]
# \s == [ \r\n\f\v\t]
# \S == Negação
# \b == bordas
# \B == Negação

#print(re.findall(r'[a-zA-ZÀ-ù]+', texto))
#print(re.findall(r'\w+', texto))
#print(re.findall(r'\d+', texto))
#print(re.findall(r'\S+', texto))
#print(re.findall(r'\be\w+', texto, flags=re.I))