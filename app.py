## The cleaned files have been loaded through another code


## This app is used for data exploration, EDA and showcasing some work

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
st.set_option('deprecation.showPyplotGlobalUse', False)


st.write("""
# Visualization of Text Data Processing
Wordcloud and LDA based Topic Modeling
""")


st.sidebar.header("Configuration Options")



df = pd.read_csv('data.csv')
df['Reason_to_Visit_Cleaned'].fillna(" ",inplace=True)




word_cloud_data = df['Reason_to_Visit_Cleaned']

long_string = ','.join(list(word_cloud_data.values))
long_string=long_string.replace('nan', '')

# WordCloud object
wordcloud2 = WordCloud(background_color="black", max_words=5000,  width=1600, height=800, max_font_size=200)
# Generate a word cloud
wordcloud2.generate(long_string)

plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()


#st.write(df.head())









# text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# # Create and generate a word cloud image:
# wordcloud = WordCloud().generate(text)

# # Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# st.pyplot()

