
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



f = open('file.txt');
m = Markov(f);
print(m.chains);
