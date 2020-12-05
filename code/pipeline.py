# Models
from sklearn.svm import SVC, LinearSVC

# Feature Extractors
from sklearn.feature_extraction.text import TfidfVectorizer

# Loader
import pickle;

class Pipeline(object) :
    def __init__(self, lyrics) :
        # Store lyrics object
        self.lyrics = lyrics;

    # Convert text into numeric vectors
    # @param path = Path of the vectorizer. Default is V1 [Check Readme Description]
    def vectorize(self, path = "vectorizer.tfidf") :
        # Load the Vectorizer
        vectorizer = pickle.load(open(path, "rb"));

        # Send the vectorized array to predict function.
        return self.predict(vectorizer.transform(self.lyrics));

    # Predict Function. Loads the model and predicts on the array.
    # @param x = The vectorized array of lyrics/text provided
    # @param path = Path of the model to be loaded. Default is V1 [Check Readme Description]
    def predict(self, x, path = "model.svm") :
        # Load the Model
        model = pickle.load(open(path,"rb"))
        
        # Predict
        y = model.predict(x)[0];

        # Return the respected Class name.
        return "Happy :)" if y == 1 else "Sad :("
        #emojis give unicode error 😎 😞