import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.io.wavfile as wav
import filters as f

def approximationError(Hd , H):
    r = 0
    for i in range(0,len(Hd)):        
        a = 0
        if( (Hd[i]-H[i]) < 0 ):
            a = H[i]-Hd[i]
        else :
            a = Hd[i]-H[i]
        if(a>r):
            r = a
    return r

def Filter ( iterations ):
    Rmin = 0
    w,N = f.HaammingWindow(np.pi/2)
    #iteration
    M = iterations

    h = []
    FrequencyResponse = np.array
    n = np.arange(N+1)

    hd = np.ones(N+1)
    Hd = np.fft.fft(hd)

    h.append( hd * w )

    for i in range(1 , M+1):            
        H = np.fft.fft( h[i-1] )
        Dbar = Hd - H
        dbar = np.fft.ifft(Dbar)
        d = dbar * w 
        h.append( h[i-1] + d )        
        if(i==1):
            Rmin = approximationError(Hd , np.fft.fft(h[1]))
            FrequencyResponse = np.fft.fft(h[1])
        elif( approximationError(Hd , np.fft.fft(h[i])) < Rmin ):
            Rmin = approximationError(Hd , np.fft.fft(h[i]))
            FrequencyResponse = np.fft.fft(h[i])

    for i in range(0 , len(FrequencyResponse)):
        if ( FrequencyResponse[i] < 0 ):
            FrequencyResponse[i] = -1 *  FrequencyResponse[i]
    return FrequencyResponse

plt.subplot(4 , 1 , 1)
plt.plot(Filter(1))
plt.title("M = 1")

plt.subplot(4 , 1 , 2)
plt.plot(Filter(10))
plt.title("M = 10")

plt.subplot(4 ,1 , 3)
plt.plot(Filter(100))
plt.title("M = 100")

plt.subplot(4,1 , 4)
plt.plot(Filter(10000))
plt.title("M = 10000")

plt.show()