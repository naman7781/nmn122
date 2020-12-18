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

