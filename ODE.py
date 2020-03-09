import matplotlib
import matplotlib.pyplot as pl
import numpy as np

A = float(input("Mass?"))
B = float(input("Damping?"))
C = float(input("Spring?"))
Low = float(input("Lower frequency?"))
High = float(input("Upper frequency?"))
Samples = float(input("Samples?"))

class ODE2:
    "A second-order linear ODE, driven with angular frequencies between wo and wf."
    def __init__(self,a=100,b=10000,c=1000000,wo=0,wf=100):
        self.a = a
        self.b = b
        self.c = c
        self.w = np.linspace(wo, wf, num=Samples)

    def getCoeff(self):
        print ("{0}D2+{1}D1+{2}".format(self.a, self.b, self.c))
    def getFreq(self):
        print ("Driving frequency: " + self.w)

    def AmpGain(self, wcurrent):
        self.wcurrent = wcurrent
        PzRe = self.c - self.a*(wcurrent**2)
        PzIm = self.b*wcurrent
        r = np.sqrt(PzRe**2 + PzIm**2)
        return 1/r

# Instantiate ODE2
RLC = ODE2(A,B,C,Low,High)

# Calculate AmpGain for each driving frequency in w
gains = [RLC.AmpGain(w) for w in RLC.w]
print(gains)

# Plot results
pl.plot(RLC.w, gains)
pl.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
pl.show()
