#horizontal square method
#keywords are fixed based on the cipher text change
alpha=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key1="example"
key2="keyword"
length1=len(key1)
length2=len(key2)
rows,cols = (5,5)
list1= []
list2= []
for i in range(0,length1):
    if(key1[i] not in list1):
        list1.append(key1[i])
for j in range(0,length2):
    if(key2[j] not in list2):
        list2.append(key2[j])
length1=len(list1)
length2=len(list2)
a = [[0 for i in range(cols)] for j in range(rows)] 
b = [[0 for i in range(cols)] for j in range(rows)] 
k=0
l=0
m=0
alpha11=[]
alpha12=[]
print(list1)
print(list2)
for n in range(0,25):
    if(alpha[n] not in list1 ):
        alpha11.append(alpha[n])
    if(alpha[n] not in list2 ):
        alpha12.append(alpha[n])
for i in range(0,5):
    for j in range (0,5):
        if(k < length1):
            a[i][j]=list1[k]
            k=k+1
        else:
            a[i][j]=alpha11[m]
            m=m+1

m=0

for i in range(0,5):
    for j in range (0,5):
        if(l < length2):
            b[i][j]=list2[l]
            l=l+1
        else:
            b[i][j]=alpha12[m]
            m=m+1
print(a)
print(b)
rows1,cols1=5,10
c = [[0 for i in range(cols1)] for j in range(rows1)] 
k,l=0,0
for i in range(0,5):
    for j in range(0,10):
        if(j<5):
            c[i][j]=a[i][j]
        else:
            c[i][j]=b[i][j-5]
for i in range(0,5):
    for j in range(0,10):
        if(j==5):
            print("|"+c[i][j],end=" ")
        else: 
            print(c[i][j],end=" ")
    print("\n")

f=open("words_twosquare.txt","r")
string=""
for each in f:
    each=each.strip()
    each=each.replace(" ","")
    string=string+each
strlen=len(string)
string=string.lower()
print(string)

if(strlen % 2 != 0):
    string=string + "x"
strlist=[]
encry=""
'''
for i in range(0,strlen,2):
    strlist.append(string[i])
    strlist.append(string[i+1])
'''
for j in range(0,strlen,2):
    for k in range(0,5):
        for l in range(0,5):
            if(string[j]==c[k][l]):
                posr,posc=k,l
        for n in range(5,10):
            if(string[j+1]==c[k][n]):
                pos1r,pos1c=k,n
    if(posr==pos1r):
        print(c[posr][posc]+"->"+c[posr][posc])
        print(c[pos1r][pos1c]+"->"+c[pos1r][pos1c])
        encry=encry+c[posr][posc]
        encry=encry+c[pos1r][pos1c]
    else:
        print(c[posr][posc]+"->"+c[pos1r][posc])
        print(c[pos1r][pos1c]+"->"+c[posr][pos1c])
        encry=encry+c[pos1r][posc]
        encry=encry+c[posr][pos1c]
print(encry)


