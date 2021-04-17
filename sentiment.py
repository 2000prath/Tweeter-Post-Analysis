from textblob import TextBlob
import math
text=TextBlob("this is not very good")
a=math.floor(text.sentiment.polarity)
if(a<0):
    print("negative")
else:
    print("positive")