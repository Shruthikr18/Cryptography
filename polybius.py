alpha=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key1=input("eneter the key word")
length1=len(key1)
rows,cols = (5,5)
list1= []
for i in range(0,length1):
    if(key1[i] not in list1):
        list1.append(key1[i])
length1=len(list1)

a = [[0 for i in range(cols)] for j in range(rows)] 
b = [[0 for i in range(cols)] for j in range(rows)] 
k=0
l=0
m=0
alpha11=[]
alpha12=[]
print(list1)
for n in range(0,25):
    if(alpha[n] not in list1 ):
        alpha11.append(alpha[n])
for i in range(0,5):
    for j in range (0,5):
        if(k < length1):
            a[i][j]=list1[k]
            k=k+1
        else:
            a[i][j]=alpha11[m]
            m=m+1
for i in range(0,5):
    for j in range(0,5):
        print(a[i][j],end=" ")
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
encryt=""
x=0
for k in range(0,strlen):
    for i in range(0,5):
        for j in range(0,5):
            if(string[k]==a[i][j]):
                posc,posr = j,i
                encryt=encryt+str(j+1)+str(i+1)
                print(a[i][j]+"->"+str(j+1)+str(i+1))
print(encryt)
decrypt=""
strlen=len(encryt)
for k in range(0,strlen,2):
    if(k < strlen):
        j,i = encryt[k],encryt[k+1]
        j,i=int(j)-1,int(i)-1
        decrypt=decrypt+a[i][j]
print(decrypt)


