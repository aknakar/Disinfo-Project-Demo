from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
import pickle
import pandas as pd
import sys

pd.set_option('display.max_colwidth', 100) # To extend column width

data = pd.read_csv('/Users/user1/Desktop/IFT401/FakeNews/pyml/clean_train.csv')
data.loc[(data['label']==1),['label']] = 'FAKE'
data.loc[(data['label']==0),['label']] = 'REAL'
labels = data.label

from sklearn.linear_model import LogisticRegression
pipe = Pipeline([('vect', CountVectorizer()),
                 ('tfidf', TfidfTransformer()),
                 ('model', LogisticRegression())])

X = data['text'].values.astype(str)
y = labels

model = pipe.fit(X,y)

with open('ml_model.pkl', 'wb') as f:
    pickle.dump(model, f)