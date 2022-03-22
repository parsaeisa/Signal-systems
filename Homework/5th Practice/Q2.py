from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.io
from scipy.io import wavfile
import soundfile as sf

audio = scipy.io.wavfile.read("D:\\Uni\\Signal & Systems\\HW\\5th Practice\\signal.wav" , mmap =False)

N = 0.5 * audio[0]
Data = audio[1]
np.random.seed(seed = None)
Data = Data + (np.random.randn(Data.shape[0]) * 0.025)

fdfd = []
for i in range(0,200):
    fdfd.append(Data[i])

scipy.io.wavfile.write("D:\\Uni\\Signal & Systems\\HW\\5th Practice\\output_Q2.wav" , audio[0] , Data)
###########################################################################################################

audio = scipy.io.wavfile.read("D:\\Uni\\Signal & Systems\\HW\\5th Practice\\output_Q2.wav" , mmap=False)

M =2000
h = np.zeros(audio[1].size)
for i in range(0 , M):    
   h[i] = 1/M

y = np.convolve(audio[1] , h)

scipy.io.wavfile.write("D:\\Uni\\Signal & Systems\\HW\\5th Practice\\output_Q2_M2000.wav" , audio[0] , y )