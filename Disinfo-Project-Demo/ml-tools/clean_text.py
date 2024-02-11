import pandas as pd
import re
import string
import nltk
import unidecode
from sklearn.feature_extraction.text import CountVectorizer
pd.set_option('display.max_colwidth',100)

stopwords = nltk.corpus.stopwords.words('english')
lem = nltk.WordNetLemmatizer()

data = pd.read_csv('train.csv')

def clean_text(text):
    text = re.sub('^[1-9a-zA-Z]','',text)
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    text = unidecode.unidecode(text)
    tokens = re.split('\W+',text)
    text = " ".join([lem.lemmatize(word) for word in tokens if word not in stopwords])
    return text

data_final = data[['text','label']]
data_final['text'] = data_final['text'].values.astype(str)
data_final['text'] = data_final['text'].apply(lambda x: clean_text(x))
data_final.to_csv('clean_text')