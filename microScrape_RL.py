import requests
from bs4 import BeautifulSoup

class wordCounter:
    def __init__(self, textList, exclusions = []):
        self.textList = textList
        self.words = []
        self.processedWords = []
        self.exclusionList = exclusions
        self.finalWordList = []
        for i in range(len(self.textList)):
            self.words.append(self.textList[i].split())
        self.countWords()
        

    def countWords(self):
        for i in range(len(self.words)):
            for x in range(len(self.words[i])):
                currWord = self.words[i][x]
                currCount = 0
                if(not self.processedWords.__contains__(currWord)):
                    if(not self.exclusionList.__contains__(currWord)):
                        for y in range(len(self.words)):
                            for r in range(len(self.words[y])):
                                if (self.words[y][r] == currWord):
                                    currCount = currCount + 1
                        self.processedWords.append(currWord)
                        self.finalWordList.append((currWord, currCount))                
        # sort them for ease of access
        self.finalWordList.sort(key=lambda a: a[1])
#############
    def printNumber(self):
        if not ( len(self.finalWordList) >= self.maxNumWords):
            for i in range(len(self.finalWordList)):
                print(self.finalWordList[i])
        else: 
            for i in range(len(self.maxNumWords)):
                print(self.finalWordList[i])

    def printAll(self):
        for i in range(len(self.finalWordList)):
            print(self.finalWordList[i])    
##############

class reader:
    
    def __init__(self, website, maxNumWords = 10):
        self.commonWords = []
        self.commonWordCount = []
        self.website = website
        self.maxNumWords = maxNumWords
        self.getContent(website)
        self.targetContentOfHistory()
        

    def getContent(self, website):
        self.page = requests.get(website)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def targetContentOfHistory(self):
        self.pData = self.soup.find_all("p")
        self.keyData = []
        for i in range(8, 42):
            self.keyData.append(self.pData[i].text)

    def printResults(self, counter):
        if(counter != None):
            endValidation = len(counter.finalWordList) - self.maxNumWords
            for i in range(len(counter.finalWordList)-1, endValidation-1, -1):
                print(counter.finalWordList[i])

if __name__ == "__main__":
    exclusions = []
    maxNumberOfWords = 10
    content = reader("https://en.wikipedia.org/wiki/Microsoft", maxNumberOfWords)
    counterObj = wordCounter(content.keyData, exclusions)
    content.printResults(counterObj)