import os
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    a_sentence = Sentence("hi there")
    message = {}
    return render_template('index.html', message=message)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    # os.system("./scripts/sentimentAnalyser.py " + str(request.data))
    message = {}
    # message['text'] = str(request.POST.get("inputText"))
    message['text'] = str(request.form['inputText'])
    return render_template('index.html', message=message)


class Sentence():
    def __init__(self, text):
        self.text = text
        self.sentiment = 100  # -1 for negative, 0 for neutral, 1 for positive, 100 for default

        self.category = ''  # empty string by default

    def set_sentiment(self, sentiment):
        this.sentiment = sentiment

    def set_category(self, category):
        this.category = category

    def __repr__(self):
        return '<Sentence: %r >' % (self.text)


if __name__ == '__main__':
    app.run()
