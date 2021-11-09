## The cleaned files have been loaded through another code


## This app is used for data exploration, EDA and showcasing some work

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.write("""
# Visualization of Text Data Processing
Wordcloud and LDA based Topic Modeling
""")


st.sidebar.header("Configuration Options")


#Read Data

#df = pd.read_csv('./data/cleaned/SF_CFA_INCREMENTAL_20210825_cleaned.txt')


word_cloud_data = df['Reason_to_Visit_Cleaned']


word_list = list(word_cloud_data.values)

text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()

