d={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
        }

s="III"
n=0

for i in range(len(s)):

    n=n+d[s[i]]

    if i+1<len(s):

        if s[i]=="I" and (s[i+1]=="V" or s[i+1]=="X"):
            n=n+d[s[i]]+d[s[i+1]]-(2*d[s[i]])

        if s[i]=="X" and (s[i+1]=="L" or s[i+1]=="C"):
            n=n+d[s[i]]+d[s[i+1]]-(2*d[s[i]])

        if s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M"):
            n=n+d[s[i]]+d[s[i+1]]-(2*d[s[i]])

        
        
    print(n)
