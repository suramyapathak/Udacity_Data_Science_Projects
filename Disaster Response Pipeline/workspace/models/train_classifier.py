import sys
# import libraries
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download(['punkt', 'wordnet'])
import pickle
import joblib

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
import sklearn.metrics as skm
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier 





def load_data(database_filepath):
    '''
    Load databse from the given filepath
    Returns the input variable, output variable and names of categories
    '''
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql('SELECT * FROM RESPONSE',engine)
    df.drop(df[df['related']==2].index, axis=0, inplace=True)
    df['related'].value_counts()
    X=df["message"]
    y = df.iloc[:,4:]
    
    category_names = y.columns.tolist()
    return X, y, category_names
    


def tokenize(text):
    '''
   Normalize, toknnize, lemmatize and lower case each word and return an array of each word in 'message'.
    '''
    text=re.sub(r"[^a-zA-Z0-9 ]","",text)
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    
    return clean_tokens 
    


def build_model():
    '''
    Build a machine learning pipeline model. 
    We are using the best model, we get from running on our local system
    It uses Grid Search to find the best parameters
    '''
    pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer=tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    
    parameters = {    
    'vect__ngram_range': ((1, 1), (1, 2)),
    'vect__max_df': (0.5, 0.75, 1.0),
    'vect__max_features': (None, 5000, 10000),
    'tfidf__use_idf': (True, False),
    'clf__estimator__n_estimators': [50, 100, 200],
    'clf__estimator__min_samples_split': [2, 3, 4],
    }
    cv = GridSearchCV(pipeline, param_grid=parameters, cv=2, n_jobs=-1)
    
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    '''
    Evaluate the model on the metrices
    Precision, Recall, f1-score and accuracy for each of the category names
    '''
     
    y_pred=model.predict(X_test)
    labels=np.unique(y_pred)
    cm=skm.multilabel_confusion_matrix(Y_test, y_pred, labels=labels)
    print(cm)
    print(skm.classification_report(Y_test, y_pred))
    print("Labels:", labels)
    #print("Confusion Matrix:\n", confusion_mat)
    accuracy=(y_pred==Y_test).mean()
    print("Accuracy:", accuracy)
    
      

def save_model(model, model_filepath):
    joblib.dump(model, model_filepath, compress = 1)
         
  
def main():
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