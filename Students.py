#import modules needed
import Tkinter
import os
import random
import Signals
import Features
import Compare
import time
import Alert

#student class for enrolment and taking assessments
class Student(object):

    #check if student file exists otherwise create student file
    if os.path.exists("students.csv"):
        fout = open('students.csv', 'r')
        fout.close()

    else:
        fout = open('students.csv', 'w')
        fout.write("ID" ',' "First name"  ',' "Last name\n")
        fout.close()

    #method that enrols a student
    def enrol(self):

        #generate a rendom number between 1 and 1000 and assign it to id
        id = random.randrange(1, 1000)

        #prompt user for first name and store it in fname
        fname = raw_input("Enter first name: ")

        #prompt user for last name and store it in lname
        lname = raw_input("Enter last name: ")

        #open file student.csv
        fout = open('students.csv', 'a+')

        #convert the id to string and assign it along side the first name and last name to output
        output = str(id) + "," + fname + "," + lname + "\n"

        #store output to file
        fout.write(output)

        #close file
        fout.close()

        #print first name
        print 'First name:', fname

        #print last name
        print 'Last name:', lname

        #print identification number
        print 'ID number:',id

        #create an object of the Signal class and call it sig
        sig = Signals.Signal()

        #call the startSignal method in the Signal class to load the signal measurements from the files in the files folder
        sig.startSignal()

        #call the signal method in the Signal class to extract a portion of the signal for enrolment and assign the returned signal to a
        a = sig.signal()

        #create an object of the Features class and call it feat
        feat = Features.FeatureExtraction()

        #call the feature method of the Feature class and pass the id, signal-for analysis and value 1-indicating 'enrolment' as arguments
        feat.feature(id, a, 1)

    #method that allows a student take an assessment
    def takeTest(self):

        #prompt user for id and store it in no
        no = raw_input("Please enter your id: ")

        #create an object of the Signal class and call it sig
        sig = Signals.Signal()

        #call the startSignal method in the Signal class to load the signal measurements from the files in the files folder
        sig.startSignal()

        #create an object of the Compare class and call it com
        com = Compare.CompareFeatures()

        #call the compareCheck method of the Compare class so that important varibles can be initialized
        com.compareCheck()

        #create an object of the Alert class and call it alert
        alert = Alert.Alert()

        #call the checkAlert method of the Alert class so that important varibles can be initialized
        alert.checkAlert()

        #while the signal parameter is available, extract portions of signal and extract the features
        while True:

            #create an object of the Signal class and call it sig
            sig = Signals.Signal()

            #call the signal method in the Signal class to extract a portion of the signal loaded earlier for enrolment and assign the returned signal to a
            a = sig.signal()

            #create an object of the Features class and call it feat
            feat = Features.FeatureExtraction()

            #call the feature method of the Feature class and pass the id, signal-for analysis and value 1-indicating 'enrolment' as arguments
            feat.feature(no, a, 2)

            #repeat the process every second while the data is available
            time.sleep(1)

#create an object of the Tk class to create a dialog box
top = Tkinter.Tk()

#create an object of the student class
stu = Student()

#link the enrol method of the Student class to the enrol button
B1 = Tkinter.Button(top, text="Enrol", command=stu.enrol)
B1.pack()

#link the takeTest method in the Student class to the take test button
B2 = Tkinter.Button(top, text="Take Test", command=stu.takeTest)
B2.pack()

top.mainloop()



