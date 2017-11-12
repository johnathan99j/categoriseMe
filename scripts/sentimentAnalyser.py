import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
import sys


def main():
        if len(sys.argv) != 2:
            exit("Error: Must pass a string as the first and only arguemnt")
        userInput = sys.argv[1]
        analyse(userInput)


def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})


def trim_line(line):
    return (line.strip())


def check_sentiment(line):
    return (line[-1])


def analyse(userInput):
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

    # classifier.show_most_informative_features()

    # it says the sentence is positive or negative
    print(classifier.classify(format_sentence(userInput)))

    # tells the accuracy
    print(accuracy(classifier, test) * 100)


if __name__ == "__main__":
    main()
