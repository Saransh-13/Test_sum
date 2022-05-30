# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


# Input text - to summarize
def hardcoded():
    text = """Today various organizations, be it online shopping, government and private sector organizations, 
    catering and tourism industry or other institutions that offer customer services are concerned about their customers 
    and ask for feedback every single time we use their services. Consider the fact, that these companies may be 
    receiving enormous amounts of user feedback every single day. And it would become quite tedious for the management to 
    sit and analyze each of those. """

    # nltk.download()

    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the
    # score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score
    # of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text

    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    print(summary)
