f1=open('output.txt','a')
p=input("enter the text to be written in file ")
r=input("enter the text to be written in addition ")

a=f1.writelines(p+"\n")

b=f1.writelines(r+"\n")
f1.close()

f1.close()
f1=open('output.txt','r')
q=f1.read()
print(q)
f1.close()
