import nltk
 
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

pos = []
with open("./pos_tweets.txt", "r") as file:
    for i in file: 
        pos.append([format_sentence(i), 'pos'])