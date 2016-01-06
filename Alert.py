#import required modules
import sys

#create class to issue alert
class Alert(object):

    #define a method to  initialize variables
    def checkAlert(self):

        #define global variable counter
        global counter

        #initialize counter
        counter = []

    #define a method to issue an alert
    def alert(self, a, b, c):

        #check if the alert type
        if len(counter) == 0:

            counter.append(1)

        elif len(counter) == 1:

            counter.append(2)

        #if alert is warning type, issue warning alert
        if len(counter) == 1:
            print "WARNING",

        #if alert is termination type, issue termination alert and end the program
        elif len(counter) >= 2:
            print "CODE RED"

            #end the program
            sys.exit()





