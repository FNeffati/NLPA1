"""

Given the training corpus,
a) Conduct preprocessing (cleaning, tokenization, lemmatization, punctuation removal, etc.)
b) Create unigram, bigram, trigram, and 4-gram dictionary.
c) Record the statistics with and without smoothing (you may use Laplace-k smoothing).
d) Write necessary methods (with comments if needed) to calculate the probability (likelihood) of a given sentence(s)/phrase.
e) Test your code.

"""




import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
import os

# Opening the directory and iterating over the files in the corpus

stop_words = set(stopwords.words('english'))
# assign directory
directory = 'TrainingSet'

A_VERY_BIG_STRING_CONTAING_ALL_TEXT = " "

# iterate over files in  that directory
for filename in os.scandir(directory):
    # checking if it is a file
    if os.path.isdir(filename):
        for minifilename in os.scandir(filename):
            if os.path.isfile(minifilename):
                TextfileContent = open(minifilename, "r").read()
                # Now since I have access to the text of that specific file, I am going to iterate through it to extract the text between the <Text> tags.
                sub1 = "<TEXT>"
                sub2 = "</TEXT>"
                try:
                    idx1 = TextfileContent.index(sub1)
                    idx2 = TextfileContent.index(sub2)
                    for idx in range(idx1 + len(sub1) + 1, idx2):
                        A_VERY_BIG_STRING_CONTAING_ALL_TEXT = A_VERY_BIG_STRING_CONTAING_ALL_TEXT + TextfileContent[idx]
                except:
                    print("Something didn't go well with this file: " + str(minifilename))


# Conduct preprocessing (cleaning, tokenization, lemmatization, punctuation removal, etc.)
    # I am starting with regular expressions to remove all the items that follow the tag "<>" format

pattern = r'<\w*>'
# Replace all occurrences of character s with an empty string
EDITED_BIG_STRING = re.sub(pattern, '', A_VERY_BIG_STRING_CONTAING_ALL_TEXT)
# print(EDITED_BIG_STRING)

# Apply case-folding to the text.
Lower_Case_File = EDITED_BIG_STRING.lower()

# Cleaning the punctuation
removed_punctuation = Lower_Case_File.translate(str.maketrans('', '', string.punctuation))
# tokenizing text
tokenzied_file = word_tokenize(removed_punctuation)
# lemmatization
lemmatizer = WordNetLemmatizer()

lemmatized_words = []
for word in tokenzied_file:
    if word not in stop_words:
        lemmatized_words.append(lemmatizer.lemmatize(word))

# Create unigram, bigram, trigram, and 4-gram dictionary.


uni = lemmatized_words
bi = list(nltk.bigrams(lemmatized_words))
tri = list(nltk.trigrams(lemmatized_words))
quad = list(nltk.ngrams(lemmatized_words, 4))


# Record the statistics with and without smoothing (you may use Laplace-k smoothing).
# Without smoothing
frequency_uni = {}
for word in uni:
    # if the word does not exist
    if frequency_uni.get(word):
        frequency_uni[word] = frequency_uni.get(word) + 1
    else:
        frequency_uni[word] = 1

sorted_unis = sorted(frequency_uni.items(), key=lambda x: x[1], reverse=True)[:20]
print(sorted_unis)

frequency_bigrams = {}
for word in bi:
    # if the word does not exist
    if frequency_bigrams.get(word):
        frequency_bigrams[word] = frequency_bigrams.get(word) + 1
    else:
        frequency_bigrams[word] = 1

sorted_bi = sorted(frequency_bigrams.items(), key=lambda x: x[1], reverse=True)[:20]
print(sorted_bi)

frequency_trigrams = {}
for word in tri:
    # if the word does not exist
    if frequency_trigrams.get(word):
        frequency_trigrams[word] = frequency_trigrams.get(word) + 1
    else:
        frequency_trigrams[word] = 1

sorted_tri = sorted(frequency_trigrams.items(), key=lambda x: x[1], reverse=True)[:20]
print(sorted_tri)

frequency_quads = {}
for word in quad:
    # if the word does not exist
    if frequency_quads.get(word):
        frequency_quads[word] = frequency_quads.get(word) + 1
    else:
        frequency_quads[word] = 1

sorted_quad = sorted(frequency_quads.items(), key=lambda x: x[1], reverse=True)[:20]
print(sorted_quad)

# Without smoothing
# how many times did this word happen / over / how many words in total

# Here I used the sorted bigram list instead of the entire Bigram dictionary
for word in sorted_bi:
    probabilityWithoutSmoothing = word[1] / len(frequency_uni)
    print(probabilityWithoutSmoothing)

# With smoothing
# How many times did word 1 happen before word 2, over how many times did word 1 happen
for word in frequency_bigrams:
    word1 = word[0]
    word2 = word[1]
    probability = frequency_bigrams[word] / frequency_uni[word1]
    # print(probability)

# I am not sure if I did already answer these?

# Write necessary methods (with comments if needed) to calculate the probability


# Write necessary methods (with comments if needed) to calculate the probability (likelihood) of a given sentence(s)/phrase



# Test your code.

