import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.io
from scipy.io import wavfile

audio = scipy.io.wavfile.read("input.wav" , mmap =False)

N = 0.5 * audio[0]
Data = []
h=[]

for i in range (0 , len(audio[1]) ):
    if(i==0):
        h.append(1)
    elif(i==N):
        h.append( 0.5 )
    elif(i==2*N):
        h.append( 0.25 )
    elif(i==3*N):
        h.append( 0.125 )
    else:
        h.append( 0.0 )
        
for i in range (0 , len(audio[1]) ):        
    Data.append(audio[1][i][0])
        
y = np.convolve(Data , h)

scipy.io.wavfile.write("output.wav",2*N , y)

print ("done")