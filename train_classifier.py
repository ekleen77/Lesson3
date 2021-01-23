# import libraries
import sys
import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import nltk, re, string
nltk.download(['punkt', 'wordnet', 'stopwords'])
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import pickle


def load_data(database_filepath):
    """Loads data from defined sqlite database file.
    
    Positional arguments:
    database_filepath - string of location of sqlite database file
        
    Returns:
    X - dataframe containing the messages
    Y - dataframe containing the categories as columns and boolean values
    category_names - list of category names
    """
    # Read 'Messages' table from specified sqlite file.
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table("Messages", engine)
    
    # Store 'message' column as X for model feature.
    X = df['message'].copy()
    
    # Store columns 5 to end as Y for model results.
    Y = df.iloc[:, 4:].copy()
    
    # Get list of category names from Y column headers.
    category_names = Y.columns
    
    return X, Y, category_names


def tokenize(text):
    """Create tokenizing function used by the CountVectorizer transform
    in the ML pipeline.  The function normalizes a text string for case and
    punctuation, deconstructs it into individual words (tokens), removes
    commonly used words (stop words), and lemmatizes each token.
    
    Positional arguments:
    text - string containing text to be tokenized
        
    Returns:
    clean_tokens - list of lemmatized tokens
    """
    #Normalize to remove punctuation and make all words lower case
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    text = regex.sub(" ", text).lower()
    
    #Tokenize string.
    tokens = word_tokenize(text)
    
    #Remove stopwords
    tokens = [t for t in tokens if t not in stopwords.words("english")]
    
    #Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [lemmatizer.lemmatize(t).strip() for t in tokens]

    return clean_tokens


def build_model():
    """Construct Machine Learning pipeline consisting of CountVectorizer and 
    TfidfTransformer transformers and the RandomForestClassifier estimator.
    
    Positional arguments:
    nothing
        
    Returns:
    pipeline - pipeline object used to create machine learning model
    """
    #classifier parameters determined by GridSearch: n_estimators=100 and
    #min_samples_split=3.  Using lower values here
    #due to size limitations when uploading pickle file to GitHub.
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(estimator=RandomForestClassifier(
                n_estimators=1, min_samples_split=2)))
        ])
    
    return pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    """Use model to predict categorical values based on test data. Compare 
    the results to the actual values in the dataset and score the performance
    of the model and print the classification report.
    
    Positional arguments:
    model - pipeline object fit to training data
    X_test - subset of dataset used to generate predicted values
    Y_test - subset of dataset used to compare to predicted values
    category_names - list of category names
    
    Returns:
    nothing
    """
    Y_pred = pd.DataFrame(model.predict(X_test), columns=category_names)
    print(classification_report(Y_test, Y_pred, target_names=category_names, digits=2, zero_division=1))


def save_model(model, model_filepath):
    """Exports model object to pickle file at specified location.
    
    Positional arguments:
    model - pipeline object used to create machine learning model
    model_filepath - string of path used to save pickle file
        
    Returns:
    nothing
    """
    pickle.dump(model, open("{}".format(model_filepath), 'wb'))


def main():
    """Main method executes operations to load data, build and train the model,
    evaluate the model, and save the model to a pickle file.
    
    Positional arguments:
    nothing
        
    Returns:
    nothing
    """
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()