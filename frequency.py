from collections import Counter
f= open ("words.txt","r")
string = ""
newlist=[]
for each in f:
    x=each.strip()
    x=x.replace(" ","")
    string=string+x
count=Counter(string)
print(count)    
eng={"E":12.7 ,"T":	9.1 ,"A":	8.2 ,"O":	7.5 ,
"I":	7.0 ,	"N":	6.7 ,	"S":	6.3 ,	"H":	6.1 ,
"R":	6.0 ,	"L":	4.0 ,	"D":	4.3 ,	"C":	2.8 ,
"U":	2.8 ,	"M":	2.4 ,	"W":	2.4 ,	"F":	2.2 ,
"G":	2.0 ,	"Y":	2.0 ,	"P":	1.9 ,	"B":	1.5 ,
"V":	1.0 ,	"K":	0.8 ,	"J":	0.2 ,	"X":	0.2 ,
"Q":	0.1 ,	"Z":	0.1 }
print(eng)