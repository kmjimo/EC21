a=[]
for i in range(2,100):
    flag = 0
    for j in range(2,i//2+1):
        if(i%j==0):
            flag=1
            break
    if flag==0:
         a.append(i)
print("1から１００までの素数")
print(a)

#print(sum(a))

line = sum(a)//2

#print(line)

a.reverse()
            
#print(a)

b=[]

for i in range(0,len(a)):
    b.append(a[i])
    a[i]=0
    if sum(b) > line:
        a[i]=b[i]
        b[i] = 0
        
        
#print(a)
#print(b)
#print(sum(b))
            
target = 0

a = [item for item in a if item != target]
b = [item for item in b if item != target]
#print(a)
#print(b)

#print(sum(a))
#print(sum(b))        
    
sa = sum(a)-sum(b)

#print(sa)
frag = 0

goukei = 0
koukan = 0

bmin = min(b)
#print(min(b))

for i in range(0,len(a)):
     for j in range(0,len(a)):
        if i!=j:
            goukei = a[i]+a[j]
            koukan = bmin + sa//2
            
            if goukei == koukan:
               frag = 1
               
        if frag==1:
            target = bmin

            
            a.append(bmin)
            b.append(a[i])
            b.append(a[j])
            b = [item for item in b if item != target]
            frag = 0
            a[i] = 0 
            a[j] = 0
              
            
            
target = 0

a = [item for item in a if item != target]
b = [item for item in b if item != target]

print("要素a")
print(a)
#print(sum(a))
print("要素b")
print(b)
#print(sum(b))

print("100までの素数で要素2つに分けたときの差の最小値")
print(sum(a)-sum(b))
print("")
