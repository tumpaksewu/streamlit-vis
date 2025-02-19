import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.write('## Визуализация чаевых')

@st.cache_data
def display_graphs(tips):
    st.write('По приему пищи (Lunch/Dinner):')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=400)
    bins = np.arange(1, tips.tip.max(), 1)
    sns.histplot(data=tips, x='tip', bins=bins, hue='time', palette={'Lunch': 'orange', 'Dinner': 'darkblue'})
    ax.set_title('Гистограмма размера чаевых по признаку Lunch/Dinner')
    ax.set_xlabel('Размер чаевых')
    ax.set_ylabel('Количество посетителей')

    plt.savefig('lunchdinner.png', dpi=400)
    st.pyplot(fig)


    st.write('По полу и курильщикам:')
    fig, ax = plt.subplots(ncols=2, figsize=(12, 5), dpi=400, sharey=True, sharex=True)
    sns.scatterplot(data=tips[tips['sex'] == 'Female'], x='total_bill', y='tip', hue='smoker', palette={'No': 'darkgreen', 'Yes': 'maroon'}, ax=ax[0])
    ax[0].set_title("Стоимость заказа и размер чаевых (Женщины)")
    ax[0].set_xlabel('Стоимость заказа')
    ax[0].set_ylabel('Размер чаевых')

    sns.scatterplot(data=tips[tips['sex'] == 'Male'], x='total_bill', y='tip', hue='smoker', palette={'No': 'darkgreen', 'Yes': 'maroon'}, ax=ax[1])
    ax[1].set_title("Стоимость заказа и размер чаевых (Мужчины)")
    ax[1].set_xlabel('Стоимость заказа')

    plt.savefig('sexsmokerocknroll.png', dpi=400)
    plt.tight_layout()
    st.pyplot(fig)

tips = pd.read_csv('./data/tips.csv')
display_graphs(tips)

with open("lunchdinner.png", "rb") as file:
    btn = st.sidebar.download_button(
        label="Скачать гистограмму Lunch/Dinner",
        data=file,
        file_name="lunchdinner.png",
        mime="image/png")
    
with open("sexsmokerocknroll.png", "rb") as file:
    btn = st.sidebar.download_button(
        label="Скачать графики по полу и курильщикам",
        data=file,
        file_name="sexsmokerocknroll.png",
        mime="image/png")