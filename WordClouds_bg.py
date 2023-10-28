# Requirement : pip install wordcloud
# command : python3 WordClouds_bg.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

#open the text file
with open('wordcloudtext.txt', 'r') as t:
    text = t.read()

# Generate word cloud 
wc = WordCloud(width=3920, height=2080, background_color='white').generate(text)

# Display the word cloud
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud.jpg', dpi = 300)
# plt.show()