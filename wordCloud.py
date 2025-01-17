import nltk

from nltk.tokenize import word_tokenize
from nltk import ne_chunk

sent = 'The US president stays in WHITEHOUSE'

ne_tokens = word_tokenize(sent)

ne_tags = nltk.pos_tag(ne_tokens)

ner = ne_chunk(ne_tags)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")

# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()