import random

#a markov chain-based text generator. 
class Markov:

    def __init__(self, file):
        self.chains = self.processRawData(file.read().split());

    def processRawData(self, wordArray):
        result = {};
        for i in range(len(wordArray)-2):
            tuple = (wordArray[i], wordArray[i+1]);
            if tuple not in result:
                result[tuple] = [wordArray[i+2]];
            else:
                result[tuple].append(wordArray[i+2]);

        return result;

    def printWords(self, number):

        def getRandomWords():
            return random.choice(list(self.chains.keys()));
        
        def getNextTuple(first, second):
            possibleWords = self.chains[(first, second)];
            if(len(possibleWords) == 0):
                first, second = getRandomWords();
                possibleWords = self.chains[(first, second)];

            return (first, second, random.choice(possibleWords));

        first, second = getRandomWords(); 
        print(first + " ", end=''); 
        for i in range(number):
            first, second, newWord = getNextTuple(first, second);
            print(second + " " + newWord + " ", end='');
            first = second; 
            second = newWord;
            

f = open('file.txt');
m = Markov(f);
m.printWords(5);
