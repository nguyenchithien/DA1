# -*- coding: utf-8 -*-
f = open('tiengnga.txt','r',encoding='utf-8')
str = f.read();
f.close()
# b = str.replace('...','')
# b = str.replace('..','')
b = str.replace('"','')
b = str.replace('v.','')
a = b.split('.')
print (a)
f = open('list_ru.txt','w',encoding='utf-8')
for c in a:
    if c == '' or c == ' ':
        continue
    else:
        f.write(c+'.\n')
