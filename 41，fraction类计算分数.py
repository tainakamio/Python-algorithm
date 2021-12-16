# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:08:01 2021

@author: Administrator
"""

#创建一个用于计算分数的类，Fraction


#用Euclid算法求最大公因数（GCD)

def gcd(m,n):
    while m%n != 0:
        n = m%n
    return n

class Fraction():
    
    def __init__(self,top,buttom):
        self.num = top
        self.den = buttom
    
    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    
    def show(self):
        print(self.num,'/',self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den +\
            self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
 
#示例    
    
myf = Fraction(3,5)

myf.show()

yourf = Fraction(4,7)

myf.__add__(yourf)

myf.__add__(yourf).show()

        
        