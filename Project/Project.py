import pyaudio
import numpy as np
import scipy as sc
import scipy.special

CHUNK = 96000

def extractor( channel ):
    omega = 0

    if(channel == "ava"):
        omega = 0.4 * np.pi
    elif(channel== "farhang"):
        omega = np.pi
    elif ( channel == "eqtesad"):
        omega = 0.6 * np.pi
    elif (channel == "goftogo"):
        omega = 0.8 * np.pi

    # h , M = f.Filter(np.pi/30 , np.pi/6)
    #Filters func#################################################    
    wc = np.pi /20
    M = 0
    w = []
        
    #kaiser filter ______________________________________________
    B = 4.583710898939595
    
    M = 46
    a = 23
    n = np.arange(M+1)
    w = (scipy.special.i0(B*np.sqrt(1-((n-a)/a)**2)))/(scipy.special.i0(B))
    #______________________________________________________________________

    n = np.arange(0,M+1)

    hd = np.sinc(wc / np.pi *(n- M/2) ) / np.pi * wc
    h = hd * w    
    ##############################################################

    n = np.arange(0 , CHUNK)
    shift = np.cos( omega *n)
    
    return (shift , h , M , omega)    

path = input("File Path: ")

p = pyaudio.PyAudio()
player = p.open(format=pyaudio.paInt16, channels=1, rate=240000, output=True, frames_per_buffer=CHUNK)


while True:
    
    Choice = int(input("\n1.Ava\n2.Farhang\n3.Eqtesad\n4.Goftogu\n5.Exit\n"))
    Station=""
    if Choice==1:
        Station="ava"
    elif Choice==2:
        Station="farhang"
    elif Choice==3:
        Station="eqtesad"
    elif Choice==4:
        Station="goftogo"
    elif Choice==5:
        break
        
    File = open(path)

    shift , h , M , omega = extractor(Station)
    M = int(M)
    buffer = np.zeros(M)
    while True:

        #data = [int(i) for i in (File.readlines(CHUNK))]
        data = []
        for i in range(CHUNK):
            line = File.readline()
            if line=='':
                break
            data.append(int(line))

        if(len(data) == 0):
            break 

        if(len(data) < CHUNK):        
            n = np.arange(0 , len(data))
            shift = np.cos( omega * n)

        data = data * shift
        x = np.concatenate([buffer , data])

        y = np.convolve( x , h , 'valid')
        y = y[::2]
        y = 5*y
        player.write(y.astype(np.int16), len(y))
        
        buffer = x[-M:]

player.stop_stream()
player.close()
p.terminate()
File.close()