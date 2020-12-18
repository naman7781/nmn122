from pytube import YouTube
from youtube_search import YoutubeSearch
from youtube_transcript_api import YouTubeTranscriptApi
import sys


query = sys.argv[1]
results = YoutubeSearch(query, max_results=10).to_dict()

j=0
for vid in results:
    #print(results[j]);
    

    #try:
    sub = YouTubeTranscriptApi.get_transcript(vid['id'])
    #getting transcript/subtitles for the video using get_transcript method
    fname = str(j)+".txt"
    print(fname)

    f = open(fname, 'a+')
    for i in sub:
        
        f.write(i["text"])
      
    j+=1
      
    #except:
        #pass  
