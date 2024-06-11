'''s='AWSswa'
s=s.upper()
count=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        count+=1 
print(count)'''

d={'a':['efg','ghi'],'b':['cde','ijk'],'c':['abc','klo']}
#tickets={'a':'a','b':'b','c':'c','ab':['a','b'],'bc':['b','c'],'abc':['a','c']}
src=['abc','efg']
dest=['klo','ijk']
si=[]
di=[]
for i in src:
    for j in d:
        if i in d[j]:
            si.append(j)
for i in dest:
    for j in d:
        if i in d[j]:
            di.append(j)
for i in range(len(si)):
    if di[i]==si[i]:
        pass
    else:
        si[i]=si[i]+di[i]
print(si)
    









