fr = open("./bill.txt",'r',encoding='utf8')
fw = open("D:/bill_2.txt",'w',encoding='utf8')
for i in fr:
    i = i.strip()
    if i.split(",")[4] == "测试":
        continue
    fw.write(i)
    fw.write('\n')
print(fw)
fr.close()
fw.close()



