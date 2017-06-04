import nltk
import string
import collections
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from sklearn.cluster import KMeans

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

def cluster_classes(mylist, nb_of_clusters=5):
    tfidf = TfidfVectorizer(min_df=1, tokenizer=tokenize, stop_words=None)
    tfs_matrix = tfidf.fit_transform(mylist)
    kmeans = KMeans(n_clusters=nb_of_clusters)
    kmeans.fit(tfs_matrix)
    clusters = collections.defaultdict(list)
    for i, label in enumerate(kmeans.labels_):
        clusters[label].append(i)
    return dict(clusters)

def classify(case, cclist, num):
    my_list = []
    for cc in cclist:
        score = get_similarity(case, cc)
        my_list.append(score)
    resultlist = sorted(range(len(my_list)), key=lambda i: my_list[i], reverse=True)[:num]
    return resultlist