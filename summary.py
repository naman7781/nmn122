import sys
import urllib
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from googlesearch import search
import re
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


def remove_blanks(para):
  lines = para.split("\n")
  non_blank = [line for line in lines if line.strip() != ""]
  targeted_para = ""
  for line in non_blank:
        targeted_para += line + "\n"
  return targeted_para

j = 0
def scrape(query,start=0,end=10):
  global j
  temp = 0
  try:
    for res in search(query,tld="com",lang='en', num=10, start=start, stop=end, pause=2.0):
      req = Request(res, headers={'User-Agent': 'Mozilla/5.0'})
      html = urlopen(req).read()
      soup = BeautifulSoup(html, 'html.parser')
      text = soup.find_all(text = True)
      
      output =""
      
      for t in text:
              if t.parent.name in ['p','h1','h2','h3','h4','h5','h6','title']:
                  output += '{} '.format(t)
      
      output = remove_blanks(output)
        
      try:
        name = soup.title.text
      except:
        name = "Untitled"+ str(temp)
        temp+=1
      
      fname = str(j)+".txt"
      print(fname)

      f = open(fname, 'w')
      f.write(output)
      f = open("summary"+".txt",'a+')
      f.write(output)
      j+=1
  except:
    print("Run again for more documents")    





input = sys.argv[1];

scrape(input)


file = open("summary.txt", "r")
filedata = file.read()
# print(filedata)

cleanr = re.compile('\\n')
data = re.sub(cleanr,"",filedata)

file.close()

file = open("summary.txt",'w')
file.write(data)
file.close()

def read_article(file_name):
    text = open(file_name, "r")
    filedata = text.readlines()
    paras = filedata[0].split(". ")
    sentences = []

    for sentence in paras:
        #print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    
    return sentences

def sentence_similarity(para_1, para_2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    para_1 = [w.lower() for w in para_1]
    para_2 = [w.lower() for w in para_2]
 
    complete_words = list(set(para_1 + para_2))
 
    vector_1 = [0] * len(complete_words)
    vector_2 = [0] * len(complete_words)
 
    #Building vector for the first sentence
    for w in para_1:
        if w in stopwords:
            continue
        vector_1[complete_words.index(w)] += 1
 
    #Building vector for the second sentence
    for w in para_2:
        if w in stopwords:
            continue
        vector_2[complete_words.index(w)] += 1
 
    return 1 - cosine_distance(vector_1, vector_2)
 
def build_similarity_matrix(sentences, stop_words):
    #Creating an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for i1 in range(len(sentences)):
        for i2 in range(len(sentences)):
            if i1 == i2: #ignore if both are same sentences
                continue 
            similarity_matrix[i1][i2] = sentence_similarity(sentences[i1], sentences[i2], stop_words)

    return similarity_matrix


def print_summary(file_name, top_n=5):
    nltk.download("stopwords")
    stop_words = stopwords.words('english')
    summarized_text = []

    #Reading text and splitting it
    sentences =  read_article(file_name)

    #Generating Similarity Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    #Ranking sentences in Similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    counts = nx.pagerank(sentence_similarity_graph)

    #Sorting the rank and picking top sentences
    ordered_sentences = sorted(((counts[j],t) for j,t in enumerate(sentences)), reverse=True)    
        

    for i in range(top_n):
      summarized_text.append(" ".join(ordered_sentences[i][1]))

    #Printing the summarized text
    with open('summary1.txt', 'w') as f:
      for sentence in summarized_text:
        f.write("%s\n" % sentence)
    f.close()

print_summary("summary.txt", 15)