#untuk run dashboard.py streamlit run dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Kuesioner",
    layout="wide"
)

st.title("📊 Dashboard Analisis Data Kuesioner")

df = pd.read_excel("data_kuesioner.xlsx")

pertanyaan = [f"Q{i}" for i in range(1, 18)]
all_answers = df[pertanyaan].stack().reset_index(drop=True)

st.subheader("1️⃣ Distribusi Jawaban Kuesioner (Keseluruhan)")

dist = all_answers.value_counts().reset_index()
dist.columns = ["Skala", "Jumlah"]

fig1 = px.bar(
    dist,
    x="Skala",
    y="Jumlah",
    text="Jumlah",
    title="Distribusi Jawaban Keseluruhan"
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("2️⃣ Proporsi Jawaban Kuesioner")

fig2 = px.pie(
    dist,
    names="Skala",
    values="Jumlah",
    title="Proporsi Jawaban"
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("3️⃣ Distribusi Jawaban per Pertanyaan")

stacked = (
    df[pertanyaan]
    .melt(var_name="Pertanyaan", value_name="Skala")
    .groupby(["Pertanyaan", "Skala"])
    .size()
    .reset_index(name="Jumlah")
)

fig3 = px.bar(
    stacked,
    x="Pertanyaan",
    y="Jumlah",
    color="Skala",
    title="Distribusi Jawaban per Pertanyaan"
)
st.plotly_chart(fig3, use_container_width=True)

st.subheader("4️⃣ Rata-Rata Skor per Pertanyaan")

skor_map = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

skor_df = df[pertanyaan].replace(skor_map)
avg_skor = skor_df.mean().reset_index()
avg_skor.columns = ["Pertanyaan", "Rata-rata Skor"]

fig4 = px.bar(
    avg_skor,
    x="Pertanyaan",
    y="Rata-rata Skor",
    text="Rata-rata Skor",
    title="Rata-rata Skor per Pertanyaan"
)
st.plotly_chart(fig4, use_container_width=True)

st.subheader("5️⃣ Distribusi Kategori Jawaban")

kategori_map = {
    "SS": "Positif",
    "S": "Positif",
    "CS": "Netral",
    "CTS": "Negatif",
    "TS": "Negatif",
    "STS": "Negatif"
}

kategori = df[pertanyaan].replace(kategori_map)
kategori_count = kategori.stack().value_counts().reset_index()
kategori_count.columns = ["Kategori", "Jumlah"]

fig5 = px.bar(
    kategori_count,
    x="Kategori",
    y="Jumlah",
    text="Jumlah",
    title="Distribusi Kategori Jawaban"
)
st.plotly_chart(fig5, use_container_width=True)

st.subheader("Heatmap (Bonus)")

heatmap_data = (
    df[pertanyaan]
    .replace(skor_map)
    .corr()
)

fig6 = px.imshow(
    heatmap_data,
    title="Korelasi Antar Pertanyaan"
)
st.plotly_chart(fig6, use_container_width=True)
