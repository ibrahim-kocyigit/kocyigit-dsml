# WordCloud

```python
from wordcloud import WordCloud, STOPWORDS

stopwords = set(STOPWORDS)
stopwords.update(["some", "also", "this"])

# Create a word cloud object	
alice_wc = WordCloud(background_color='white', max_words=2000, mask=mask_image, stopwords=stopwords, font_path='path/to/font_file', colormap='Blues')

# Generate the word cloud based on the text data.	
alice_wc.generate(alice_novel)

plt.imshow(alice_wc, interpolation='bilinear')
plt.axis("off")
plt.show()
```

