# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:12:46 2021

@author: やん
"""

def sosu():
    a=[]
    for i in range(2,100):
        f=False
        for j in range(2,i//2+1):
            if(i%j==0):
                f=True
                break
        if f==False:
            a.append(i)
    return a
        
S=sosu()
minimam=1000000000000000
for i in range(len(S)):
    SA=[]
    SB=[]
    SA=S[0:i]
    SB=S[i+1:len(S)]
    total=abs(sum(SA)-sum(SB))
    if(minimam>total):
       minimam_SA=[]
       minimam_SB=[]
       minimam=total
       minimam_SA=SA
       minimam_SB=SB
        
print("min:"+str(minimam))
print("SA:"+str(minimam_SA))
print("SB:"+str(minimam_SB))