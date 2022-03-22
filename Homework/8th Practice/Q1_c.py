from __future__ import division
import numpy as np
import soundfile as sf


def play_audio(m, p, fs , path ):
    # Combine magnitude and phase parts
    f = m * np.exp(1j * p )

    # Computer inverse fft
    y = np.fft.ifft(f)
    y = np.real(y)

    # Convert to 16-bit data
    audio = y * (2 ** 15 - 1)
    audio = audio.astype(np.int16)

    sf.write(path , y , fs )


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

p1 = np.zeros( len (p) )
p2 = np.zeros( len (p) )
p3 = np.zeros( len (p) )

for i in range(0 , len(p) ):
    p1[i] = p[i] + (2 * np.pi * i * 0.25 )
    p2[i] = p[i] + (2 * np.pi * i * 0.5 )
    p3[i] = p[i] + (2 * np.pi * i * 0.25 * -1   )


# Play the modified audio
play_audio(m, p1, fs , 'D:\Uni\Signal & Systems\HW\8th Practice\Q1_c_N_0.25.wav')
play_audio(m, p2, fs , 'D:\Uni\Signal & Systems\HW\8th Practice\Q1_c_N_0.5.wav')
play_audio(m, p3, fs , 'D:\Uni\Signal & Systems\HW\8th Practice\Q1_c_N_0-.25.wav')
