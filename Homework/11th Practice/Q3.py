import matplotlib.pyplot as plt
import numpy as np 
import scipy as sc
import scipy.io.wavfile as wav

# n is array like ##########################################################################

#Rectangular
def RactangularWindow(dw):
    M = (1.8 * np.pi / dw) -1
    M = int(M)
    return (np.ones( M+1 ) , M )

# Triangle
def TriangleWindow (dw):
    M = (6.1 * np.pi / dw) -1
    M = int(M)
    out = []
    for i in range(0,M/2):
        out.append(2*i / M)
    for i in range(M/2 , M+1):
        out.append( 2 - (2*i/M) )
    return (out , M)

# Hann 
def HannWindow (dw):
    M = (6.2 * np.pi / dw) -1
    M = int(M)
    n = np.arange(M+1)
    return ( 0.5*( 1 - np.cos(2*np.pi * n / M) ) , M )

#Hamming 
def HaammingWindow(dw):
    M = (6.6 * np.pi / dw) -1    
    M = int(M)
    n = np.arange(M+1)
    return (0.54 - 0.46 * np.cos( 2 * np.pi * n / M ) , M)    

# Blackman
def BlackmanWinddow (dw):
    M = (11 * np.pi / dw) -1
    M = int(M)
    n = np.arange(M+1)
    return (0.42 - 0.5 * np.cos(2 * np.pi * n / M) + 0.08 * np.cos(4 * np.pi * n / M) , M)        

##########################################################################################################

def FilterAndLength(ws , wp , deltas , deltap):
    delta = min(deltap , deltas)
    dw = ws - wp    
    wc = (ws + wp) /2
    M = 0
    w = []

    if (delta < 0.09 and delta > 0.05):
        w , M = RactangularWindow(dw)
    elif ( delta> 0.0063 and delta < 0.05):
        w , M = TriangleWindow(dw)
    if( delta < 0.0063 and delta > 0.0022 ):
        w , M = HannWindow(dw)
    elif(delta < 0.0022 and delta > 0.0002):    
        w , M = HaammingWindow(dw)
    elif (delta < 0.0002): 
        w , M = BlackmanWinddow(dw)
    M = 329

    n = np.arange(0,M+1)
    w = 0.54 - 0.46 * np.cos( 2 * np.pi * n / M )

    hd = np.sinc(wc / np.pi *(n- M/2) ) / np.pi * wc
    h = hd * w

    return ( h , M )

isHighPass = False
h , M = FilterAndLength(np.pi/50 , np.pi/25 , 0.001 , 0.001 )
audio = wav.read("voice.wav")

buffer = np.zeros(M)

y = np.convolve( np.concatenate((buffer , audio[1])) , h , mode='valid')

# wav.write("LowPass.wav" , audio[0] , y.astype(np.int16) )
# z = audio[1] - y
# wav.write("HighPass.wav" , audio[0] , z.astype(np.int16) )

if(isHighPass == False):
    wav.write("out.wav" , audio[0] , y.astype(np.int16) )
else :
    z = audio[1] - y
    wav.write("out.wav" , audio[0] , z.astype(np.int16) )