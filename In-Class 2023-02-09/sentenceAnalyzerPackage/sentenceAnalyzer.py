#sentenceAnalyzer.py

def sentence_analyzer(text):
    myLetters = dict()  #empty dictionary
    #I need to iterate over the string
    for letter in text:
        #print(letter)
        #Check if letter is already in myLetters(the dictionary)
        #If so, increment the value
        #Else, add it to the dictionary and set the value to 1
        if letter in myLetters:
            myLetters[letter] = myLetters[letter] + 1
        else:
            myLetters[letter] = 1
    return myLetters
        