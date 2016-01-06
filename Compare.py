#import modules required
import csv
import Alert
import scipy
from scipy import stats

#create class to coompare the features
class CompareFeatures(object):

    #define method to initialize necessary variables
    def compareCheck(self):

        #define global variable to store all variances for comparison
        global ListOfVariances

        #initialize the variable
        ListOfVariances = []

    #define method to retrive the features for comparison
    def compare(self, no, number, newvariance):

        #assign no to id
        id = no

        #open features.csv
        with open("features.csv",'r') as f:

            #create an object of the csv class
            reader = csv.reader(f, delimiter=',')

            for row in reader:
                #retrieve the features of a particilar student with given id
                if id in row:

                    #define global variable variance
                    global variance

                    #extract the value in row 1
                    variance = float(row[1])

                    #define global variable num
                    global num

                    #extract the value in row 2
                    num = float(row[2])

            #close the file
            f.close()

        #check if the array of variances is empty
        if len(ListOfVariances) == 0:

            #append the variance to the array
            ListOfVariances.append(float(variance))

            #define global variable latest variance to store the latest retrieved variance
            global latestVariance

            #retrieve the latest retrieved variance from the list of variances and assign it to latest variance
            latestVariance = ListOfVariances[len(ListOfVariances)-1]

            #asign the current variance into new variance
            newVariance = newvariance

            #create an object of the compare features class
            a = CompareFeatures()

            #call the check variance method to compare the variances
            a.checkVariance(number, latestVariance, newVariance)

        #if the list of variances is not empty
        elif len(ListOfVariances) != 0:

           #retrieve the latest variance in the array
           latestVariance = ListOfVariances[len(ListOfVariances)-1]

           #assign the current variance to new variance
           newVariance = newvariance

           #create an object of the compare features class
           a = CompareFeatures()

           #call the check variance method to compare the variances
           a.checkVariance(number, latestVariance, newVariance)


    #define method to check the variances and compare them
    def checkVariance(self, number, lastVariance, newVariance):

        #create a object of the alert class
        alert = Alert.Alert()

        #check for the greater variance
        if lastVariance > newVariance:

            #assign bigger value to varX
            varX = lastVariance

            #assign smaller variable to varY
            varY = newVariance
        else:

            varX = newVariance

            varY = lastVariance

        #calculate the F value for the F test
        F = varX/varY

        #compute the degrees of freedom
        df1 = number - 1

        df2 = number - 1

        #assign the significance level to alpha value
        alpha = 0.05

        #compute the P value
        p_value = scipy.stats.f.sf(F, df1, df2)

        #if the p value is greater than alpha then pass
        if p_value > alpha:

            print "PASS"

        #if the p value is less than or equal to alpha, issue alert
        else:

            #call the alert method to issue an alert
            alert.alert(newVariance, lastVariance, p_value)

        if p_value > alpha:

            #add new variance to the list of variances
            ListOfVariances.append(newVariance)

