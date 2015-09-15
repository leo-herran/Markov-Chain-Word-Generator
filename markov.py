import random, pickle, sys

#a markov chain-based text generator. 
class Markov:

    def __init__(self, file, wordDataFile=None):
        if(wordDataFile == None):
            self.chains = self.processRawData(file.read().split());
        else:
            self.chains = pickle.load(open(wordDataFile, 'rb')); 
    
    def processRawData(self, wordArray):
        result = {};

        for i in range(len(wordArray)):
            wordArray[i] = wordArray[i].lower();

        for i in range(len(wordArray)-2):
            tuple = (wordArray[i], wordArray[i+1]);
            newWord = wordArray[i+2];
            if tuple not in result:
                result[tuple] = [newWord];
            else:
                if(newWord not in result[tuple]):
                    result[tuple].append(newWord);

        return result;

    def getGeneratedWords(self, number):

        
        def getRandomWords():
            return random.choice(list(self.chains.keys()));
        
        def getNextTuple(first, second):
            possibleWords = self.chains[(first, second)];
            if(len(possibleWords) == 0):
                first, second = getRandomWords();
                possibleWords = self.chains[(first, second)];

            return (first, second, random.choice(possibleWords));

        first, second = getRandomWords(); 
        result = first + " " + second + " "; 
        for i in range(number):
            #first, second, newWord = getNextTuple(first, second);
            if((first, second) not in self.chains):
                break;
            else:
                newWord = random.choice(self.chains[(first, second)]);

            result = result + newWord + " "
            first, second = second, newWord; 

        return result;
        
def main(dataFile, numWords):
    if('.txt' in dataFile):
        m = Markov(open(dataFile, 'r'));
    else:
        m = Markov('', dataFile);

    words = m.getGeneratedWords(numWords);
    print(words);

if __name__ == "__main__":

    #first argument is the .py file, so exclude it. 
    args = sys.argv[1:];

    if(len(args) != 2):
        print('Usage: python markov.py (dataFile) (number of words to output)');
	
    else:

        dataFile = args[0];
        numWords = int(args[1]);
 
        main(dataFile, numWords);

