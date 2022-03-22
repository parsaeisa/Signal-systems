from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.signal as sig

F = open("data2.txt")
x1 = F.readlines()
################################ functions needed ############################################
def h(n , x):
    ans = 0
    I = 2
    for m in range(0 , len(x)):
        ans = ans +( x[m] * np.sinc( np.pi *((n/I) - m) ) )
    return ans

def show(G):
    plt.stem(G)
    plt.show()
################################ A ##################################    
x2 =[]
xTrash = []

for i in range(0,len(x1)):
    x1[i] = float(x1[i])

for i in range(0,len(x1)):
    if(i%2 ==1):
        x2.append(x1[i])
    else :
        xTrash.append(x1[i])
################################ B ##################################
x3 = []

for i in range(0 , len(x2)):
    x3.append(x2[i])
    x3.append(0)

bazsazi_B = [-0.15]

for n in range(0,99):
    bazsazi_B.append( h(n , x2) )

show(x1)

################################# C ##################################
xp = sig.decimate(x1 , 2)
################################# D ##################################
bazsazi_D = []

for n in range(0,100):
    bazsazi_D.append( h(n , xp) )

# show(bazsazi_D)
################################# E for B #################################
print "bakhshe b "
Bazsazi_shode_B = []
Bazsazi_nashode_B = []

for i in range(0 , len(bazsazi_B)):
    if( i%2 == 1 ):
        Bazsazi_nashode_B.append(bazsazi_B[i])
    else :
        Bazsazi_shode_B.append(bazsazi_B[i])

Bazsazi_shode_B = np.array(Bazsazi_shode_B)
Bazsazi_nashode_B = np.array(Bazsazi_nashode_B)
show(bazsazi_B)
bazsazi_B = np.array(bazsazi_B)
# a
print "Whole singal :"
print np.sqrt(np.mean((bazsazi_B - x1)**2))
# b
print "Destroyed part of signal"
print np.sqrt(np.mean((Bazsazi_shode_B - xTrash)**2))
# c
print "Rest part of signal"
print np.sqrt(np.mean((Bazsazi_nashode_B - x2)**2))
################################# E for D #################################
print "-------------------------------------------------------"
print "bakhshe t "
Bazsazi_shode_D = []
Bazsazi_nashode_D = []

for i in range(0 , len(bazsazi_D)):
    if( i%2 == 0 ):
        Bazsazi_nashode_D.append(bazsazi_D[i])
    else :
        Bazsazi_shode_D.append(bazsazi_D[i])

Bazsazi_shode_D = np.array(Bazsazi_shode_D)
Bazsazi_nashode_D = np.array(Bazsazi_nashode_D)
show(bazsazi_D)
bazsazi_D = np.array(bazsazi_D)
# a
print "Whole singal :"
print np.sqrt(np.mean((bazsazi_D - x1)**2))
# b
print "Destroyed part of signal"
print np.sqrt(np.mean((Bazsazi_shode_D - xTrash)**2))
# c
print "Rest part of signal"
print np.sqrt(np.mean((Bazsazi_nashode_D - x2)**2))
