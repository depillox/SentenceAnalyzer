#main.py
#    Package                Module                    * = all the functions in the module
from sentenceAnalyzerPackage.sentenceAnalyzer import *
import matplotlib.pyplot as plt    #import the library

myLetters = sentence_analyzer("Eagles will dominate the Chiefs in the Super Bowl")
print(myLetters) #to see if it works
#What key occurs the most times? Print that letter.
maxValue = -1000
letter = ""
for key in myLetters.keys():
    if maxValue < myLetters[key]:
        maxValue = myLetters[key]
        letter = key
print(letter, "appears", maxValue, "times.")

#Generate a histogram of letters and frequencies
#Use matplotlib 
plt.bar(myLetters.keys(), myLetters.values(), color='r')
plt.show()