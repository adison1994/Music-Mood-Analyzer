class Mapper(object) :
    def __init__(self, vectorizer) :
        self.map = { 
            "TF-IDF [Uni-Gram]": ("unigram.tfidf","model-unigram.svm"), 
            "TF-IDF [Bi-Gram]": ("bigram.tfidf", "model-bigram.svm"),
            "TF-IDF [Tri-Gram]": ("trigram.tfidf","model-trigram.svm"),
            "TF-IDF [ngram(1-5]": ("ngram-v1.tfidf","model-ngram-v1.svm")
        }
        return self.map[vectorizer];