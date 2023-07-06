import sqlite3
import streamlit as st
import plotly.express as px
import pandas as pd

connection = sqlite3.connect("data1.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temperature")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temp FROM temperature")
temp = cursor.fetchall()
temp = [item[0] for item in temp]

figure = px.line(x=date, y=temp,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)