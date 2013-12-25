#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lucas
#
# Created:     24.12.2013
# Copyright:   (c) Lucas 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


def est_premier(n):
    import math as ma
    prem = True
    for i in range(2,ma.floor(ma.sqrt(n))+1):
        if n%i == 0:
            prem = False
            break
    return prem



def listepremiers(n):
    bar = open('liste de nombres premiers.txt','w')
    for i in range(1,n+1):
        if est_premier(i):
            bar.write('\n'+str(i))
    bar.close()



def fichiermaj(a):
    obj = open(a+'.txt','r')
    lignes = obj.readlines()
    obj.close()
    obj = open(str(a)+'MAJ'+'.txt','w')
    for L in lignes:
        obj.write(L.upper())
    obj.close()


def fichierandletttres(a,n):
    import random as rd
    obj = open(a+'.txt','w')
    A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','\s','\n']
    for i in range(1,n):
        b = rd.randint(0,1)
        c = rd.randint(0,27)
        if b == 0:
            obj.write(A[c])
        else:
            obj.write(A[c].upper())
    obj.close()



def criblerath(n):
    t1 = [True]*(n+1)
    t1[:2]=[False,False]
    for i in range(4,n+1,2):
        t1[i] = False
    for i in range(3, n+1,2):
        if i and i*i<n+1:
            for j in range(2,(n+1)//2):
                try:
                    t1[i*j]= False
                except:
                    continue
    s = [2]
    for i in range(3,n):
        if t1[i]:
            s.append(i)
    return s

def prob4():
    return(max(x*y for x in range(900,999) for y in range(900,999) if str(y*x) == str(x*y)[::-1]))

def prob8():
    obj = open('prob8.txt','r')
    nombre = ''.join(obj.readlines())
    nombre = nombre.replace('\n','')
    obj.close()
    maxprod = 0
    for i in range(0,len(nombre)-5):
        prod = 1
        for j in range(0,5):
            prod *= int(nombre[i+j])
            if prod > maxprod:
                maxprod = prod
    return maxprod


def prob9():
    t = [i for i in range(2,2000001) if est_premier(i)]
    return sum(j for j in t)

def prob11():
    obj = open('prob11.txt','r')
    t=[]
    for L in obj.readlines():
        L = str(L)
        L = L.strip().split(' ')
        t.append(L)
    obj.close()
    s = []
    for i in range(0,20):
        for j in range(0,20):
            if j < 17 :
                s.append(int(t[i][j])*int(t[i][j+1])*int(t[i][j+2])*int(t[i][j+3]))
            if j > 2 :
                s.append(int(t[i][j])*int(t[i][j-1])*int(t[i][j-2])*int(t[i][j-3]))
            if i < 17:
                s.append(int(t[i][j])*int(t[i+1][j])*int(t[i+2][j])*int(t[i+3][j]))
            if i > 2:
                s.append(int(t[i][j])*int(t[i-1][j])*int(t[i-2][j])*int(t[i-3][j]))
            if j > 2 and i > 2:
                s.append(int(t[i][j])*int(t[i-1][j-1])*int(t[i-2][j-2])*int(t[i-3][j-3]))
            if j > 2 and i < 17:
                s.append(int(t[i][j])*int(t[i+1][j-1])*int(t[i+2][j-2])*int(t[i+3][j-3]))
            if j < 17 and i > 2:
                s.append(int(t[i][j])*int(t[i-1][j+1])*int(t[i-2][j+2])*int(t[i-3][j+3]))
            if j < 17 and i < 17:
                s.append(int(t[i][j])*int(t[i+1][j+1])*int(t[i+2][j+2])*int(t[i+3][j+3]))
    return max(s)


def prob13():
    obj = open('prob13.txt','r')
    t=[]
    for L in obj.readlines():
        L = str(L)
        L = L.strip()
        t.append(L)
    obj.close()
    return sum(int(i) for i in t)

def prob14():
    s = 0
    for i in str(2**1000):
        s += int(i)
    return s

def prob18():
    obj= open('prob18.txt','r')
    t =[]
    for L in obj.readlines():
        L = L.strip()
        t = t.append(L)
    obj.close
    for i in ranf



