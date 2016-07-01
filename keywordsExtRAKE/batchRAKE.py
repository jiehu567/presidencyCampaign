# Extract keywords from bunch of files in as directory

import os
import six
import rake
import operator
import io

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# RAKE method
def keywordExtract(filename):
    
    # EXAMPLE ONE - SIMPLE
    stoppath = "SmartStoplist.txt"
    
    
    print("---------------------------------------------")
    # EXAMPLE TWO - BEHIND THE SCENES (from https://github.com/aneesha/RAKE/rake.py)
    
    # 1. initialize RAKE by providing a path to a stopwords file
    # rake_object = rake.Rake(stoppath)
    
    sample_file = io.open(filename, 'r',encoding="iso-8859-1")
    text = sample_file.read()
    
    # 1. Split text into sentences
    sentenceList = rake.split_sentences(text)
    
    # generate candidate keywords
    stopwordpattern = rake.build_stop_word_regex(stoppath)
    phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
    # print("Phrases:", phraseList)
    # print("---------------------------------------------")
    
    # calculate individual word scores
    wordscores = rake.calculate_word_scores(phraseList)
    
    # generate candidate keyword scores
    keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
    
    # sort candidates by score to determine top-scoring keywords
    sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
    # totalKeywords = len(sortedKeywords)
    return sortedKeywords
    # print("---------------------------------------------")
    # for example, you could just take the top third as the final keywords
    # for keyword in sortedKeywords[0:int(totalKeywords / 3)]:
    #    print "Keyword: %s\tscore: %s" % (keyword[0], keyword[1])
    
    # print(rake_object.run(text))


dir = os.getcwd() + "/" + "HillarySpeeches"

for filename in os.listdir(dir):
    if filename.startswith("1") == False: continue

    dir_file = dir + '/' + filename
    sortedkeywords = keywordExtract(dir_file)
    totalKeywords = len(sortedkeywords)
    
    save_path = dir + '/keywordLists/'
    completeName = os.path.join(save_path, "keywords_"+filename)
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    with open(completeName, 'wb') as target:
         target.write("\n")        
         for keyword in sortedkeywords[0:int(totalKeywords / 3)]:
             keyword_0 = keyword[0]
             keyword_1 = keyword[1]
             target.write("Keyword: %s\tscore: %s" % (keyword_0, keyword_1))
             target.write("\n")
        
       