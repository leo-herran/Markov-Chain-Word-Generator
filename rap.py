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
def getCrowdLyrics():
    rap = request.form['text']
    f = open(filePath + 'crowdRap.txt', 'w');
    f.write(rap + '\n');
    f.close();
    return redirect('/');


@app.route('/clean')
def cleanLyrics():
    return getLyrics('clean');

@app.route('/regular')
def regularLyrics():
    return getLyrics('regular');

@app.route('/dirty')
def dirtyLyrics():
    return getLyrics('dirty');


#@app.route('/<explicitness>')
def getLyrics(explicitness):

    m = markov.Markov('', filePath + str(explicitness) + '.p');
    rap = m.getGeneratedWords(100);
    #return words; 
    return render_template(str(explicitness) + "rap.html", words=rap);


if __name__=='__main__':
    #app.debug = True;
    app.run();
