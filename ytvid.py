from pytube import YouTube
from youtube_search import YoutubeSearch
import sys

query=sys.argv[1]

#query = input("Enter the name of disease")
results = YoutubeSearch(query, max_results=1).to_dict()

j = 0
for i in results:
  link =("https://www.youtube.com"+results[j]['url_suffix'])                #getting the link of the particular video to be downloaded.
  yt = YouTube(link)                                                              #object creation using YouTube.
                                                                                  
  # To print title
  print("Title :", yt.title)
  # To get number of views
  print("Views :", yt.views)
  # To get the length of video
  print("Duration :", yt.length)
  # To get description
  print("Description :", yt.description)
  # To get ratings
  print("Ratings :", yt.rating)

  stream = yt.streams.get_highest_resolution()
  stream.download()
  print("Download completed!!")
  j+=1