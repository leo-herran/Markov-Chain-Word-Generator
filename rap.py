import markov, pickle;
from flask import Flask, render_template

filePath = '/home/leo/public_html/markov/'

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('default.html');


@app.route('/<explicitness>')
def getLyrics(explicitness):

    #words = markov.main('', filePath + str(explicitness) + '.p', 100); 

    m = markov.Markov('', filePath + str(explicitness) + '.p');
    rap = m.getGeneratedWords(100);
    #return words; 
    return render_template(str(explicitness) + "rap.html", words=rap);


if __name__=='__main__':
    #app.debug = True;
    app.run();
