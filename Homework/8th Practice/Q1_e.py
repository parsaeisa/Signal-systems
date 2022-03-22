from __future__ import division
import numpy as np
import soundfile as sf

def play_audio(m, p, fs , path):
    # Combine magnitude and phase parts
    f = m * np.exp(1j * p)

    # Computer inverse fft
    y = np.fft.ifft(f)
    y = np.real(y)

    # Convert to 16-bit data
    audio = y * (2 ** 15 - 1)
    audio = audio.astype(np.int16)

    sf.write(path , y , fs)

def average (avg , a , n):
    avg = avg * n 
    avg = avg + a
    avg = avg / (n+1)
    return avg 


# Read signal
signal, fs = sf.read('D:\Uni\Signal & Systems\HW\8th Practice\Record.wav')
signal = signal[:, 0]

# Compute fft
f = np.fft.fft(signal)

# Convert to polar (magnitude and phase)
m = np.abs(f)
p = np.angle(f)

# Change magnitude and/or phase
# Type your code here!

ave = 0 
n = 0 
for M in m:
    ave = average(ave , M, n)
    n= n+1

for i in range(0,len(m)):
    m[i] = ave
    
# Play the modified audio
play_audio(m, p, fs , 'D:\Uni\Signal & Systems\HW\8th Practice\Q1_e.wav')
