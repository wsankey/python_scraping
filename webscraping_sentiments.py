'''
Your task
is to scrape N (You decide but generally, the higher the sample, the
more accurate) number of comments from a YouTube video of your choice
and then analyse their sentiments based on a short list of happy/sad
keywords

Analysis will be done by seeing how many Happy/Sad keywords are in
each comment. If a comment contains more sad keywords than happy, then
it can be deemed sad.

Here's a basic list of keywords for you to test against. I've ommited
expletives to please all readers...

happy = ['love','loved','like','liked','awesome','amazing','good','gre
at','excellent']

sad = ['hate','hated','dislike','disliked','awful','terrible','bad','p
ainful','worst']

Feel free to share a bigger list of keywords if you find one. A larger
one would be much appreciated if you can find one. 
'''
import sys
 
#Data source
youtube_path = ("https://plus.googleapis.com/u/0/_/widget/render/"
	"comments?first_party_property=YOUTUBE&href="
	"https://www.youtube.com/watch?v=UEuOpxOrA_0")
 
#Bring the comments into python using standard library: urllib2
import urllib2
import re
import xml.etree.ElementTree as ET
 
#Store our youtube comments into a variable
youtube_comments = urllib2.urlopen(youtube_path)
 
print youtube_comments
 
return_code = youtube_comments.getcode()
if return_code != 200:
	print "Uh-oh! There was an error retrieving the URL!"
	sys.exit(1)
# else:
# 	print "Great! You retrieved the URL! Here's some meta-data:"
# 	print youtube_comments.info()
 
comments_data = youtube_comments.read()
print re.findall(r"<script>(.*?)<\/script>", comments_data)
comments_data = re.sub(r"<script>.*?<\/script>", "", comments_data)
print comments_data[:845]
 
element_tree = ET.fromstring(comments_data)
comments = element_tree.findall(".//div[class='Ct']")
print comments[:3]

