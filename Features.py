#import all modules required
import numpy as np
import pylab
import os
import sys
import Compare
import Signals

#create class to extracts features from a signal
class FeatureExtraction(object):

    #define method to break signal into chunk, perform Fast Fourier Transform and calculate variance
    def feature(self, no, signals, a):

        #sampling frequency
        Fs = 250.0

        #sampling space
        T = 1/Fs

        #function to calculate next power of 2
        def nextpow2(x):

            #return the result of the calculation to the function that called it
            return 2**(x-1).bit_length()

        try:

            #assign a to z
            self.z = a

            #assign no to id
            self.id = no

            #split signal into parts for processing
            k = len(signals)/4

        except:

            #exit program
            sys.exit()

        #create ranges for each signal portion
        a = range(0,k)

        b = range(k,k*2)

        c = range(k*2, k*3)

        d = range(k*3, k*4)

        #create arrays to store the signal portions
        signal1=[]

        signal2=[]

        signal3=[]

        signal4=[]

        for i in a:

            #append the first range of measurements to the first signal array
            signal1.append(signals[i])

        for i in b:

            #append the second range of measurement to the second signal array
            signal2.append(signals[i])

        for i in c:

            #append the third range of measurements to the third signal array
            signal3.append(signals[i])

        for i in d:

            #append the fourth range of measurements to the final signal array
            signal4.append(signals[i])

        #define a function to perform an FFT on the signals and extract the dominant frequency
        def fastfouriertransform(Signal):

            #lenght of the signal
            L = len(Signal)

            #compute the next power of 2 from lenght of array and assign it to NFFT
            NFFT = 2^nextpow2(L)

            #create a range of numbers from 1 to half of the length of the signal
            ind = np.arange(1,NFFT/2+1)

            #define the global variable psd
            global psd

            #perform an FFT on the signal and assign the result to Y
            Y = np.fft.fft(Signal,NFFT)/L

            #calculate the power spectral density and assign it to psd
            psd = (abs(Y[ind])**2 + abs(Y[-ind])**2)

            #compute the corresponding range of frequencies
            f = Fs/2*np.linspace(0,1,NFFT/2+1)

            #define global variable freqs
            global freqs

            #extract the range of frequencies bins required
            freqs = f[ind]

            #merge the fft output with the corresponding frequency bins
            mergedData = np.vstack((freqs,psd)).T

            for i in range(len(psd)):

                #check for the maximum value on the psd array
                if psd[i] == max(psd):

                    #define global variable peakID
                    global peakID

                    #assign the maximum psd value to peakID
                    peakID = i

            #extract the the pair with the highest magnitude and store it in DomFreq
            DomFreq = mergedData[peakID]

            #extract the frequency value from the pair with the highest magnitude
            domFreq = DomFreq[0]

            #return the dominant frequency
            return domFreq


        #define variable chunk to store the dominant frequencies
        chunks = []

        #perform an FFT on the first signal and assign the returned dominant frequency to chunk
        chunks.append(fastfouriertransform(signal1))

        #perform an FFT on the second signal and assign the returned dominant frequency to chunk
        chunks.append(fastfouriertransform(signal2))

        #perform an FFT on the third signal and assign the returned dominant frequency to chunk
        chunks.append(fastfouriertransform(signal3))

        #perform an FFT on the final signal and assign the returned dominant frequency to chunk
        chunks.append(fastfouriertransform(signal4))

        #calcuate the variance of the dominant frequencies
        variance = (np.std(chunks))**2

        #calculate the lenght of the chunk
        number = len(chunks)

        #check if the file features.csv exist. if it does open it otherwise, create the file and append the headers
        if os.path.exists("features.csv"):

            fout = open('features.csv', 'r')

            fout.close()
        else:

            fout = open('features.csv', 'w')

            fout.write("ID" ',' "Variance"  ','  "Number\n")

            fout.close()

        # check if the feature extraction request if for enrolment.
        if self.z == 1:

            #check if the variance is 0
            if variance != 0:

                #open the features file
                fout = open('features.csv', 'a+')

                #assign the id, variance and number of dominant frequencies to the variable output
                output = str(self.id) + "," + str(variance) + "," + str(number) + "\n"

                #append the output to the file
                fout.write(output)

                #close the file
                fout.close()

                #plot the frequencies against the psd
                pylab.plot(freqs, psd)

                pylab.title('Single-Sided Amplitude Spectrum')

                pylab.xlabel('Frequency (Hz)')

                pylab.ylabel('Magnitude (V)')

                #pylab.show()

                #exit the system
                sys.exit()

            #otherwise skip the signal and request for another one
            else:

                #create an object of the signal class
                sig = Signals.Signal()

                #call the signal method in the signal class and assign the returned signal to a
                a = sig.signal()

                #call the feature extraction method to extract the features and store them
                FeatureExtraction().feature(no, a, 1)

        #else if the variance is not zero
        elif variance != 0:

            #create an object of the Compare features class
            com = Compare.CompareFeatures()

            #call the compare method to compare the features of the signal
            com.compare(no, number, variance)

        #else if the feature extraction request is for assessment
        else:
            #create an object of the signal class
            sig = Signals.Signal()
            #call the signal method to extract another signal if the variance is 0
            a = sig.signal()
            #call the feature extraction method to extract the features
            FeatureExtraction().feature(no, a, 2)










