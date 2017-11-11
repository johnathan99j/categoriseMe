import nltk
from nltk.classify import NaiveBayesClassifier

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

def trim_line(line):
    return (line.strip())

def check_sentiment(line):
    return (line[-1])

# get extract teh positive and negative data
positive = []
negative = []
with open("./amazon_cells_labelled.txt", "r") as file:
    for line in file: 
        line = trim_line(line)
        sentiment = check_sentiment(line)
        line = line[:-1]
        if sentiment == "1":
            positive.append([format_sentence(line), 'pos'])
        else:
            negative.append([format_sentence(line), 'neg'])

# building training data
training = positive[:int((.8)*len(positive))] + negative[:int((.8)*len(negative))]
test = positive[int((.8)*len(positive)):] + negative[int((.8)*len(negative)):]

classifier = NaiveBayesClassifier.train(training)

userInput = "Needless to say, I wasted my money"
classifier.show_most_informative_features()
print(classifier.classify(format_sentence(userInput)))

