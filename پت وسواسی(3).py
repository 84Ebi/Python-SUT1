#by ebi
import re

a = input()
a = re.sub(r' +',' ',a.strip())
a = re.sub(r"\\n","\n",a)

result=''

a=list(a)

finalres=[]
tmp = 0

for i in a:

    if i=='@':
        finalres.append('@')
        tmp+=1

    elif i =='#' and tmp>0:
        tmp-=1

    else:
        finalres.append(i)

for item in finalres:
     result+=item

print('Formatted Text: '+result)