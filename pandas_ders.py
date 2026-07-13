import pandas as pd
import numpy as np

# 1. DataFrame oluştur — Excel tablosu gibi!
veri = {
    "isim": ["Selin", "Kerime", "Kenan", "Mümine", "Şenol"],
    "yas": [19, 21, 25, 22, 28],
    "bolum": ["Çalışma Eko", "CEO", "Mühendislik", "Tıp", "Hukuk"],
    "not": [85, 92, 78, 95, 70]
}

df = pd.DataFrame(veri)
print("--- Tüm Tablo ---")
print(df)

# 2. Temel bilgiler
print("\n--- Tablo Bilgisi ---")
print("Boyut:", df.shape)
print("Sütunlar:", df.columns.tolist())

# 3. İstatistik — tek satırda!
print("\n--- İstatistik ---")
print(df.describe())

# 4. Filtreleme
print("\n--- Yaşı 21'den Büyük ---")
print(df[df["yas"] > 21])

# 5. Sıralama
print("\n--- Nota Göre Sıralı ---")
print(df.sort_values("not", ascending=False))

# 6. Belirli sütun
print("\n--- Sadece İsim ve Not ---")
print(df[["isim", "not"]])

# 7. Ortalama not
print("\nOrtalama not:", df["not"].mean())
print("En yüksek not:", df["not"].max())