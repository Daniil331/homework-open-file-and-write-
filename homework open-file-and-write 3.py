def file(append,filenames):
 filenames=[]
 with open('file4','a', encoding="utf-8")as outfile:
  for fname in filenames:
   with open(fname, encoding="utf-8")as infile:
    for line in infile:
        text = outfile.write(line)
 li =[]
 with open('file.txt3', encoding="utf-8") as myfile3:
     count2 = sum(1 for line2 in myfile3)
     li.append(count2)
 with open('file2.txt', encoding="utf-8") as myfile2:
     count1 = sum(1 for line1 in myfile2)
     li.append(count1)
 with open('file.txt', encoding="utf-8") as myfile:
     count = sum(1 for line in myfile)
     li.append(count)
 with open('file4', encoding="utf-8") as myfile4:
         count3 = sum(1 for line3 in myfile4)
         li.append(count3)

 sorted_li = sorted(li)
 print('file2.txt')
 for s in range(1,(sorted_li[0])+1):
        print(f'строка номер {s} файла номер 2')
 print('file.txt')
 for n in range(1,(sorted_li[1])+1):
        print(f'строка номер {n} файла номер 1')
 print('file.txt3')
 for m in range(1,sorted_li[2]+1):
        print(f'строка номер {m} файла номер 3')


file('file4',['file2.txt','file.txt','file.txt3'])