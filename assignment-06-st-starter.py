# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# show the title
st.title('Titanic App by Ziyi Zhao')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
plt.style.use('seaborn')
fig, ax = plt.subplots(1, 3, figsize = (15, 5))
i = 0
for name, d in df.groupby('Pclass'):
    d.Fare.plot.box(ax=ax[i])
    ax[i].set_xlabel(f'Pclass = {name}')
    ax[0].set_ylabel('Fare')
    i += 1

st.pyplot(fig)

