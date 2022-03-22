import numpy as np
import scipy.special
import matplotlib.pyplot as plt

def kaiser(Dw , S ):    # s = 0.003
    A = -20*np.log10(S) # A = 50.45

    B = 0.5842*((A-21)**0.4) + 0.07886*(A-21)

    # Dw = np.fabs(ws - wp)

    M = (A-8)/(2.285*Dw) # Dw = 0.0002

    M = np.ceil(M)

    if M%2==1:
        M = M+1

    a = M/2 #Takhiir

    n = np.arange(M+1)
    w = (scipy.special.i0(B*np.sqrt(1-((n-a)/a)**2)))/(scipy.special.i0(B))

    return (w , M)
