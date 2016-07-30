from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing how to remove stop words from a sentence."

#nltk package contains a stop words corpus that can be imported
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)


#removing stop words from the sentence.

filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)
