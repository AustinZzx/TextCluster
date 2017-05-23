import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

from DPSParser import *

def tokenize(text):
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    no_punctuation = lowers.translate(str.maketrans('','',string.punctuation))
    tokens = nltk.word_tokenize(no_punctuation)
    filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
    return filtered_tokens

def get_similarity(lhs, rhs):
	try:
		tfidf = TfidfVectorizer(min_df=1, tokenizer=tokenize, stop_words=None)
		tfs_matrix = tfidf.fit_transform([lhs, rhs])
		similarity = cosine_similarity(tfs_matrix)
	except:
		return -1;
	return similarity[0][1]

def get_similarity_matrix(mylist):
	tfidf = TfidfVectorizer(min_df=1, tokenizer=tokenize, stop_words=None)
	tfs_matrix = tfidf.fit_transform(mylist)
	similarity = cosine_similarity(tfs_matrix)
	return similarity

"""tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
dpsc = DPSParser()
dpsinfo = []
for x in xrange(10):
	dpsinfo.append(dpsc[x].information)
tfs = tfidf.fit_transform(dpsinfo)
print(cosine_similarity(tfs))"""
