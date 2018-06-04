import xlsxwriter
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()
f = open('tiengViet.txt','r',encoding='utf-8')
data1 = f.read()
list1 = data1.split('.')
f.close()
f = open('list_ru.txt','r',encoding='utf-8')
data2 = f.read()
list2 = data2.split('.')
f.close()
col_o = 0
col_t = 1
row = -1
for x,y in zip(list1,list2) :
        row += 1
        print (row)
        worksheet.write(row,col_o,x)
        worksheet.write(row,col_t,y)
workbook.close()
