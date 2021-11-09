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
### Wordcloud 
""")


st.sidebar.header("Configuration Options")



df = pd.read_csv('data.csv')
df['Reason_to_Visit_Cleaned'].fillna(" ",inplace=True)


column_dict = {'Reason  to  Visit':'Reason_to_Visit_Cleaned',
'Savings  Goal':'Savings_Goal_Cleaned',
'Purchase  Rewards  Preference':'Purchase_Rewards_Preference_Cleaned',
'Payments  Challenges':'Payments_Challenges_Cleaned',
'Expense  Types':'Expense_Types_Cleaned',
'Expansion  Plans':'Expansion_Plans_Cleaned',
'Fut  Large  Equipment  Purchase':'Fut_Large_Equipment_Purchase_Cleaned',
'Debt  Consolidation':'Debt_Consolidation_Cleaned',
'Investment  Plans':'Investment_Plans_Cleaned',
'Borrow  Unexpected  Expense':'Borrow_Unexpected_Expense_Cleaned',
'Home  Improvement  Purchase  Plans':'Home_Improvement_Purchase_Plans_Cleaned',
'Refinance  Outstanding  Debt':'Refinance_Outstanding_Debt_Cleaned',
'Refinance  Current  Mortgage  Rate':'Refinance_Current_Mortgage_Rate_Cleaned',
'Invest  Comfort  Level':'Invest_Comfort_Level_Cleaned',
'Invest  Investment  Review':'Invest_Investment_Review_Cleaned',
'Invest  Retirement  College  Other':'Invest_Retirement_College_Other_Cleaned'}


option = st.sidebar.selectbox(
'Select One',
('Reason  to  Visit','Savings  Goal','Purchase  Rewards  Preference','Payments  Challenges','Expense  Types','Expansion  Plans','Fut  Large  Equipment  Purchase','Debt  Consolidation','Investment  Plans','Borrow  Unexpected  Expense','Home  Improvement  Purchase  Plans','Refinance  Outstanding  Debt','Refinance  Current  Mortgage  Rate','Invest  Comfort  Level','Invest  Investment  Review','Invest  Retirement  College  Other'))

st.write('You selected:', option)
st.write("Mapped",column_dict[option])


word_cloud_data = df[column_dict[option]]

long_string = ','.join(list(word_cloud_data.values))
long_string=long_string.replace('nan', '')





def generate_wordcloud(data, title, mask=None):
    cloud = WordCloud(scale=3,
                      max_words=150,
                      colormap='RdYlGn',
                      mask=None,
                      background_color='white',
                      collocations=True).generate_from_text(data)
    plt.figure(figsize=(10,8))
    plt.imshow(cloud)
    plt.axis('off')
    plt.title(title)
    plt.show()
    st.pyplot()

generate_wordcloud(long_string, 'WordCloud', mask=None)


#st.write(df.head())









# text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# # Create and generate a word cloud image:
# wordcloud = WordCloud().generate(text)

# # Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# st.pyplot()

