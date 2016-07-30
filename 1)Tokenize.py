from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing - word tokenizers.... sentence tokenizers
# lexicon and corporas
# corpora - body of text. ex: medical journals, presidential speeches, English language
# lexicon - words and their means

example_text = "In lexical analysis, tokenization is the process of breaking a stream of text up into words, phrases, symbols, or other meaningful elements called tokens."


for i in word_tokenize(example_text):
    print(i)
