f=open("D://23bca283//sqlite3//csv//python.txt","w")
line=[]
while True:
    l=input()
    if l:
        line.append(l+'\n')
    else:
        break
python='\n'.join(line)
f.writelines(line)
f.close()
f=open("D://23bca283//sqlite3//csv//python.txt","r")
for line in reversed(python):
    print(line)
f.close()
