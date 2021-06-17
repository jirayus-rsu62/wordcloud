import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import wordcloud

text = ""
with open('./data.txt', encoding='utf-8') as f :
  text = "" .join(f.readlines())


wc = WordCloud(max_font_size=42, background_color='white')
wc.generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()