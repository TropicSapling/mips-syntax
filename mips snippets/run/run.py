from __future__ import print_function
import os
import glob
import re

with open('MIPS.txt') as file:
    linhas = file.readlines()

# for arquivo in glob.glob('../*.sublime-snippet'):
#     print('Removendo:', arquivo)
#     os.remove(arquivo)

for linha in linhas:
    pedacos = re.split(r'\s{2,}', linha)
    
    length = 0
    for c in pedacos[1]:
        if c == ' ':
            break
        
        length += 1
    
    if length < 4:
        tabs = "\t\t"
    else:
        tabs = "\t"

    funcName = pedacos[0]
    CDATA = pedacos[1][0:length]+tabs+pedacos[1][length+1:]
    comentario = pedacos[2].strip()

    content = '''<!-- THIS WAS AUTOMATED GENERATED -->
<snippet>
    <description>'''+comentario+'''</description>
    <content><![CDATA['''+CDATA+''']]></content>
    <tabTrigger>'''+funcName+'''</tabTrigger>
    <scope>source.mips</scope>
</snippet>\n'''

    fileDest = '../'+funcName+'.sublime-snippet'
    with open(fileDest, 'w') as file:
        file.write(content)
