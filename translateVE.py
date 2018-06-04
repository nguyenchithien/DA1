# -*- coding: utf-8 -*-
from googletrans import Translator
f = open('tiengViet.txt','r',encoding='utf-8')
str = f.read()
f.close()
a = str.split('.')
f = open('list_ru.txt','w',encoding='utf-8')
for c in a:
    translator = Translator()
    s = translator.translate(c,dest='ru',src='vi')
    s.text = s.text.encode('utf-8', 'ignore').decode('utf-8')
    f.write(s.text+'.\n')
    # print s.text
f.close()
