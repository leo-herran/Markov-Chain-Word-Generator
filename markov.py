import random

#a markov chain-based text generator. 
class Markov:

    def __init__(self, file):
        self.chains = self.processRawData(file.read().split());

    def processRawData(self, wordArray):
        result = {};
        for i in range(len(wordArray)-2):
            tuple = (wordArray[i], wordArray[i+1]);
            newWord = wordArray[i+2];
            if tuple not in result:
                result[tuple] = [newWord];
            else:
                if(newWord not in result[tuple]):
                    result[tuple].append(newWord);

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
        print(first + " " + second + " ", end=''); 
        for i in range(number):
            #first, second, newWord = getNextTuple(first, second);
            if((first, second) not in self.chains):
                break;
            else:
                newWord = random.choice(self.chains[(first, second)]);

            print(newWord + " ", end='');
            first, second = second, newWord; 
        
        print();

f = open(input());
m = Markov(f);
m.printWords(int(input()));
