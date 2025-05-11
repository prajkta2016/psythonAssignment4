try:
    f1=open('sample.txt','r')
    a=f1.read()
    print(a)
    f1.close()
except:
    print("the file does not exist")