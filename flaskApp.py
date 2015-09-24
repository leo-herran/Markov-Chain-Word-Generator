import markov, pickle;
from flask import Flask, render_template, request, redirect

filePath = '/home/leo/public_html/markov/'

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('default.html');

@app.route('/crowdsourced')
def crowd():
    return render_template('crowd.html');

@app.route('/crowdform', methods = ['POST'])
def crowdForm():
    rap = request.form['text']
    f = open(filePath + 'crowdRap.txt', 'a');
    f.write(rap + '\n');

    return redirect('/crowdrap');

@app.route('/crowdrap')
def getCrowdLyrics():
    f = open(filePath + 'crowdRap.txt', 'r');
    m = markov.Markov(f);
    rap = m.getGeneratedWords(100);
    return render_template("crowdrap.html", words=rap);

@app.route('/clean')
def cleanLyrics():
    return getLyrics('clean');

@app.route('/regular')
def regularLyrics():
    return getLyrics('regular');

@app.route('/dirty')
def dirtyLyrics():
    return getLyrics('dirty');

#gets lyrics for explicitness versions. 
def getLyrics(explicitness):

    m = markov.Markov('', filePath + str(explicitness) + '.p');
    rap = m.getGeneratedWords(100);
    #return words; 
    return render_template(str(explicitness) + "rap.html", words=rap);


if __name__=='__main__':
    #app.debug = True;
    app.run();
