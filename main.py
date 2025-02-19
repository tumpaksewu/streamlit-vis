import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, date


st.write("""
         ## Apple Stock Price Tracker
         Графики отображают цену закрытия и объем торгов (период — 1 день).

         Вы можете скачать графики, нажав кнопку в левой панели.
""")

# st.write('Выберите даты начала и конца отслеживаемого периода:')
start_date = st.date_input("Начало периода", date(2024, 1, 1))
end_date = st.date_input("Конец периода", datetime.now())

tickerData = yf.Ticker('AAPL')
aaplDf = tickerData.history(period='1d', start=start_date, end=end_date)

plt.style.use("dark_background")
fig, ax = plt.subplots(nrows=2, figsize=(10, 8), dpi=400)

sns.lineplot(data=aaplDf, x='Date', y='Close', ax=ax[0])
ax[0].set_title("Apple Stock Price (Close Price)")
ax[0].set_xlabel('Дата')
ax[0].set_ylabel('Стоимость, USD')


sns.lineplot(data=aaplDf, x='Date', y='Volume', ax=ax[1], color="red")
ax[1].set_title("Apple Stock Trading (Volume)")
ax[1].set_xlabel('Дата')
ax[1].set_ylabel('Объем сделок, млн')

plt.tight_layout()
plt.savefig('aapl.png', dpi=400)
st.pyplot(fig)

with open("aapl.png", "rb") as file:
    btn = st.sidebar.download_button(
        label="Скачать графики",
        data=file,
        file_name="aapl.png",
        mime="image/png")
