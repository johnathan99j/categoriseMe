from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    a_sentence = Sentence("hi there")
    message = {}
    message['text'] = a_sentence.text
    return render_template('index.html', message=message)

class Sentence():
    def __init__(self, text):
        self.text = text
        self.sentiment = 100 # -1 for negative, 0 for neutral, 1 for positive,
                            # 100 for default
        self.category = '' # empty string by default

    def set_sentiment(self, sentiment):
        this.sentiment = sentiment

    def set_category(self, category):
        this.category = category

    def __repr__(self):
        return '<Sentence: %r >' % (self.text)
if __name__ == '__main__':
    app.run()
