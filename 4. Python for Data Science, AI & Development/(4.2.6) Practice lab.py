givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

### Part A: Creating the class

class TextAnalyzer(object):
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()
        self.fmtText = formattedText
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        return freqMap
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
### Part B: Allowing the functions to execute and generate output

# Create an instance of TextAnalyzer Class.
analyzed = TextAnalyzer(givenstring)
# Call the function that converts the data into lowercase
print("Formatted Text:", analyzed.fmtText)
# Call the function that counts the frequency of all unique words from the data.
freqMap = analyzed.freqAll()
print(freqMap)
# Call the function that counts the frequency of specific word.
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")