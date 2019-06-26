#val = input("enter the text")
val=""
f = open("words.txt","r")
for each in f:
    each = each.strip()
    val  = val+each
f.close()
length =len(val)
print(length)
l = []
for m in range(0,length):
    l.append(ord(val[m]))
for i in range(0,26):
    string=""
    for j in range(0,length):
        if(l[j]==32):
            string = string+" "
        else:
            inter= l[j]+i
            value=chr(l[j]+i)
            if(inter > 90):
                value=chr((l[j]-26)+i)
            string = string + value
    print(string+"\n")
    print(i)