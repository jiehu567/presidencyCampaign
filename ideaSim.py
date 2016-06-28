# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:28:00 2016

@author: cshep04
"""

from os import listdir
from gensim import models
from gensim.models.doc2vec import LabeledSentence


class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
       self.labels_list = labels_list
       self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            yield LabeledSentence(words=doc.split() ,tags=[self.labels_list[idx]])


def ideaSim(DIR, words = [], N= 10):
    """str, list of str, int --> Doc2Vec
    DIR the directory where the corpus of text documents is saved, should be a sub directory of your working directry.
    words is a list of key-words or phrases that we wish to compare within the model.
    N is the number of trainig iterations to run, defaults to 10.
    
    ideaSim takes as input a directory with a corpus of documents to train on and a list of key ideas to include in the model and outputs a Doc2Vec object using the Gensim Doc2Vec class.
    
    """
    #read in file names as list of labels.
    docLabels = []
    docLabels = [f for f in listdir(DIR) if f.endswith('.txt')]
    
    #create an array of the files we wish to train on.
    data = []
    for doc in docLabels:
        with open(DIR + doc, 'r') as d:
            text = d.read()
            data.append(text)
    
    #include a list of key concepts in the model
    for w in words:
        docLabels.append(w)
        data.append(w)
    
    #create a LabeledLineSentence object to train on.
    sentences = LabeledLineSentence(data, docLabels)
    
    #set up model
    model = models.Doc2Vec(size=300, window=10, min_count=5, workers=11,alpha=0.025, min_alpha=0.025) # use fixed learning rate
    
    #build vocab
    model.build_vocab(sentences)
    
    #training the model over 10 iterations with fixed decrease in learning rate for each iteration.
    for epoch in range(N):
        model.train(sentences)
        model.alpha -= 0.002 # decrease the learning rate
        model.min_alpha = model.alpha # fix the learning rate, no deca
        model.train(sentences)
    
    return model
    
