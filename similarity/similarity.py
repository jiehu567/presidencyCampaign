# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 12:49:55 2016

@author: cshep04
"""

"""Comparing similarity of words/documents from trained model

"""

import numpy as np
from gensim import models

def keyMat(model, words):
    """ Doc2Vec, list of str --> NumPy Array
    Create a matrix of cosine similarities between a list of keywords using a previously trained Doc2Vec model.
    Input:
    model is a Doc2Vec object
    words is a list of strings of length n, the n keywords to be analyzed.
    Output:
    sim is an nxn numpy array
    """
    n = len(words)
    sim = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1, n):
            sim[i,j] = model.similarity(words[i], words[j])
    return np.maximum(sim, sim.T)

