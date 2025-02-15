import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.write('## Авто-визуализация')
st.write('Загрузи файл .csv и получи авто-визуализацию (результат не гарантирован 😂)')

your_csv = st.file_uploader(label='Загрузи файл .csv')

if your_csv:
    df = pd.read_csv(your_csv)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=400)
    sns.lineplot(data=df, ax=ax)
    st.pyplot(fig)