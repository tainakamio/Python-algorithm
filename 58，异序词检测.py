# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:34:01 2021

@author: Administrator
"""

#异序词检测的四种方法

s1='heart'
s2='earth'

s3='heart'
s4='heartt'

s5='ass'
s6='sas'

#1.清点法
#教材上的清点法不能判别单词长度不同的情况，如heart和heartt

#自创的，结果总是false，不知道错在哪了
def checkfunction1wrong(s1,s2):
    
    l1=list(s1)
    l2=list(s2)
    
    stillOK=True
    
    while len(l2)>0 and stillOK:
        for j in range(len(l1)):
            if l1[j] in l2:
                l2[l2.index(l1[j])]=None
                j+=1
            else:
                stillOK=False
                
    return stillOK

wrongresult=checkfunction1wrong(s1,s2)



#教材上的写法，但是作了一行改进

def checkfunction1(s1,s2):
    
    l2=list(s2)
    stillOK = len(s1)==len(s2)#两词长度不同，直接否定，返回false
    pos1=0
    
    while pos1<len(s1) and stillOK:
        found=False
        pos2=0
        while pos2<len(s2) and not found:
            if s1[pos1]==l2[pos2]:
                found=True
            else:
                found=False
                pos2+=1       
        if found:
            l2[pos2]=None
        else:
            stillOK=False
       
        pos1+=1
        
        print(l2)#显示逐步清点的过程
        
    return stillOK
       

print(checkfunction1(s1,s2))
print(checkfunction1(s3,s4))
print(checkfunction1(s5,s6))

#排序法

def checkfunction2(s1,s2):
    
    l1=list(s1)
    l1.sort()
    l2=list(s2)
    l2.sort()
    
    stillOK = l1==l2
    
    return stillOK

print(checkfunction2(s1,s2))
print(checkfunction2(s3,s4))
print(checkfunction2(s5,s6))    


#穷举法。书上无代码。关键在于列举其中任一个字串元素的全排列。日后补充。


#计数法

def checkfunction4(s1,s2):
    
    c1=[0]*26
    c2=[0]*26
    
    stillOK= len(s1)==len(s2)
    
    pos1=0
    pos2=0
    
    while pos1<len(s1):
        i=ord(s1[pos1])-ord('a')
        c1[i]+=1
        pos1+=1
    while pos2<len(s2):
        j=ord(s2[pos2])-ord('a')
        c2[j]+=1
        pos2+=1
    
    stillOK = c1==c2
    
    return stillOK

print(checkfunction4(s1,s2))
print(checkfunction4(s3,s4))
print(checkfunction4(s5,s6))    

#比较三种方法各自运行1000次所需时间

     


