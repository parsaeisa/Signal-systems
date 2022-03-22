import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.io
from scipy.io import wavfile

def system(x , n , N , a):
    if (n-N <= 0):
        return 0
    else:
        return (a) * system(x , n - N , N , a) + x[n]

audio = scipy.io.wavfile.read("D:\\Uni\\Signal & Systems\\HW\\5th Practice\\input_Q4.wav" , mmap =False)
# picking first element of each element of audio data
N = audio[0] /2 
Data = []
for i in range (0 , len(audio[1]) ):        
    Data.append(audio[1][i][0])

y = []

for i in range(0,len(Data)):
    y.append(system(Data , i , N , 0.5))
outData = np.array(y)
scipy.io.wavfile.write("D:\\Uni\\Signal & Systems\\HW\\5th Practice\\output_Q4_a_Positive.wav" , audio[0] ,outData )

for i in range(0,len(Data)):
    y.append(system(Data , i , N , -0.5))
outData = np.array(y)
scipy.io.wavfile.write("D:\\Uni\\Signal & Systems\\HW\\5th Practice\\output_Q4_a_Negative.wav" , audio[0] ,outData )