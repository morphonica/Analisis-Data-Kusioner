import pandas as pd

# =============================
# LOAD DATA
# =============================
df = pd.read_excel("data_kuesioner.xlsx")

pertanyaan = [f"Q{i}" for i in range(1, 18)]
jumlah_responden = len(df)
total_respon = jumlah_responden * len(pertanyaan)

# =============================
# MAP SKALA & KATEGORI
# =============================
skor_map = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

kategori_map = {
    "SS": "positif",
    "S": "positif",
    "CS": "netral",
    "CTS": "negatif",
    "TS": "negatif",
    "STS": "negatif"
}

target_question = input().strip()

# =============================
# q1: skala terbanyak
# =============================
if target_question == "q1":
    counts = df[pertanyaan].stack().value_counts()
    skala = counts.idxmax()
    jumlah = counts.max()
    persen = round(jumlah / total_respon * 100, 1)
    print(f"{skala}|{jumlah}|{persen}")

# =============================
# q2: skala tersedikit
# =============================
elif target_question == "q2":
    counts = df[pertanyaan].stack().value_counts()
    skala = counts.idxmin()
    jumlah = counts.min()
    persen = round(jumlah / total_respon * 100, 1)
    print(f"{skala}|{jumlah}|{persen}")

# =============================
# q3: SS terbanyak
# =============================
elif target_question == "q3":
    hasil = []
    for q in pertanyaan:
        jumlah = (df[q] == "SS").sum()
        hasil.append((q, jumlah))
    hasil.sort(key=lambda x: (-x[1], int(x[0][1:])))
    q, jumlah = hasil[0]
    persen = round(jumlah / jumlah_responden * 100, 1)
    print(f"{q}|{jumlah}|{persen}")

# =============================
# q4: S terbanyak
# =============================
elif target_question == "q4":
    hasil = []
    for q in pertanyaan:
        jumlah = (df[q] == "S").sum()
        hasil.append((q, jumlah))
    hasil.sort(key=lambda x: (-x[1], int(x[0][1:])))
    q, jumlah = hasil[0]
    persen = round(jumlah / jumlah_responden * 100, 1)
    print(f"{q}|{jumlah}|{persen}")

# =============================
# q5: CS terbanyak
# =============================
elif target_question == "q5":
    hasil = []
    for q in pertanyaan:
        jumlah = (df[q] == "CS").sum()
        hasil.append((q, jumlah))
    hasil.sort(key=lambda x: (-x[1], int(x[0][1:])))
    q, jumlah = hasil[0]
    persen = round(jumlah / jumlah_responden * 100, 1)
    print(f"{q}|{jumlah}|{persen}")

# =============================
# q6: CTS terbanyak
# =============================
elif target_question == "q6":
    hasil = []
    for q in pertanyaan:
        jumlah = (df[q] == "CTS").sum()
        hasil.append((q, jumlah))
    hasil.sort(key=lambda x: (-x[1], int(x[0][1:])))
    q, jumlah = hasil[0]
    persen = round(jumlah / jumlah_responden * 100, 1)
    print(f"{q}|{jumlah}|{persen}")

# =============================
# q7: TS terbanyak (2 DESIMAL)
# =============================
elif target_question == "q7":
    hasil = []
    for q in pertanyaan:
        jumlah = (df[q] == "TS").sum()
        hasil.append((q, jumlah))
    hasil.sort(key=lambda x: (-x[1], int(x[0][1:])))
    q, jumlah = hasil[0]
    persen = jumlah / jumlah_responden * 100
    print(f"{q}|{jumlah}|{persen:.1f}")

# =============================
# q8: TS terbanyak (2 DESIMAL)
# =============================
elif target_question == "q8":
    hasil = []
    for q in pertanyaan:
        jumlah = (df[q] == "TS").sum()
        hasil.append((q, jumlah))
    hasil.sort(key=lambda x: (-x[1], int(x[0][1:])))
    q, jumlah = hasil[0]
    persen = jumlah / jumlah_responden * 100
    print(f"{q}|{jumlah}|{persen:.1f}")

# =============================
# q9: pertanyaan yang memiliki STS
# =============================
elif target_question == "q9":
    out = []
    for q in pertanyaan:
        jumlah = (df[q] == "STS").sum()
        if jumlah > 0:
            persen = round(jumlah / jumlah_responden * 100, 1)
            out.append(f"{q}:{persen}")
    print("|".join(out))

# =============================
# q10: rata-rata skor keseluruhan
# =============================
elif target_question == "q10":
    skor = df[pertanyaan].replace(skor_map)
    print(f"{skor.stack().mean():.2f}")

# =============================
# q11: skor rata-rata tertinggi
# =============================
elif target_question == "q11":
    skor = df[pertanyaan].replace(skor_map)
    avg = skor.mean()
    q = avg.idxmax()
    print(f"{q}:{avg[q]:.2f}")

# =============================
# q12: skor rata-rata terendah
# =============================
elif target_question == "q12":
    skor = df[pertanyaan].replace(skor_map)
    avg = skor.mean()
    q = avg.idxmin()
    print(f"{q}:{avg[q]:.2f}")

# =============================
# q13: kategori jawaban
# =============================
elif target_question == "q13":
    kategori = df[pertanyaan].replace(kategori_map)
    counts = kategori.stack().value_counts()

    hasil = []
    for k in ["positif", "netral", "negatif"]:
        jumlah = counts.get(k, 0)
        persen = round(jumlah / total_respon * 100, 1)
        hasil.append(f"{k}={jumlah}:{persen}")

    print("|".join(hasil))
