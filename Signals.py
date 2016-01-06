#import necessary modules
import pylab
import numpy as np
from scipy import signal
import sys

#create class Signal to extract signal and preprocess it
class Signal(object):

    #create method to load pressure measurements from file
    def startSignal(self):

        #define global variable r
        global r

        #initialize variable r with an empty array
        r = []

        #define global variable a
        global a

        #load csv file containing the pressure measurements and save them in global variable a
        a=np.loadtxt(r'files\1\E3.csv',dtype=str,delimiter=',',skiprows=1,usecols=(0,))

        #convert all measurements into floating points and save them in global variable r
        for i in a:
            r.append(float(i))

    #define method signal to extract portions of the measurements and filter them.
    def signal(self):

        #define global variable data
        global data

        #initialize data with an empty array for later use
        data = []


        try:

            #perform the operations within the if function if the condition is true
            if len(r) >= 1000:

                #for the first 1000 measurements in the array r
                for i in range(1000):

                    #assign the measurements to variable data
                    data.append(r[0])

                    #remove each measurement assigned to data from the array r
                    r.pop(0)

                #create an object of the signal class and call it z
                z = Signal()

                #call the sig method passing the data array as arguments for filtering and return the result to n
                n=z.sig(data)

                #return n to the method that called the signal method
                return n

            #if the condition fails, perform the operations beneath the elif function
            elif len(r) >= 500:

                #for the first 500 elements in the array r
                for i in range(500):

                    #assign the measurements to the array data
                    data.append(r[0])

                    #remove each measurement assigned to data
                    r.pop(0)

                #create an object of the Signal class and call it z
                z = Signal()

                #call the sig method passing the data array as arguments for filtering and return the result to n
                n=z.sig(data)

                #return n to the method that called the signal method
                return n
        except:
            #exit the program if the instructions un
            sys.exit()

    #define method to filter data
    def sig(self, data):

        #number of points
        Fs = 250.0

        #lenght of the signal
        L = len(data)

        #sampling space
        T = 1/Fs

        #initialize the variable v with an empty array
        v = []

        #assign a value of range L to z
        z = range(L)

        for i in z:

            #multiply each value in z with the sampling space
            t = (i * T)

            #multipy each time t with the sampling rate
            w = Fs*t

            #append wach value of w to v
            v.append(w)

        #define the x-axis
        pylab.xlabel('time (milliseconds)')

        #define the y-axis
        pylab.ylabel('pressure (Pa)')

        #plot the signal measurements against time
        pylab.plot(v,data)
        #pylab.show()

        #creat a butterworth filter of magnitude 2 and cut-off frequency of 0.1
        [b, a] = signal.butter(2, 0.1, 'high')

        #pass the data through the filter
        filtered_data = signal.filtfilt(b,a,data)

        #return the filtered data to the method that called the sig method
        return filtered_data









