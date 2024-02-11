# Imports
from datetime import date
import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
import pickle

def predict(text):
    with open('ml_model.pkl','rb') as f:
        model = pickle.load(f)

    in_text = []
    in_text.append(text)

    return model.predict(in_text)

content = input("Enter content:\n")
print("################################################################################################################\n############# Our 3-year-old ML model is deciding whether you should trust this information ... ################\n################################################################################################################")
if (predict(content)[0]) == 'FAKE':
    print("Our 3-year-old ML model has decided that this content is likely disinformation.")
else: 
    print("Our 3-year-old ML model has decided that this is likely reliable content.")
 





"""    with open('/Users/user1/Desktop/IFT401/FakeNews/pyml/ml_model.pkl','rb') as f:
    model = pickle.load(f)

sample_text = []
sample_text.append(input("Enter a claim: "))

print(model.predict(sample_text)) """