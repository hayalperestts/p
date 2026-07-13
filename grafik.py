import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ogrenciler.csv")

# 1. Çubuk grafik — her öğrencinin notu
plt.figure(figsize=(10, 5))
plt.bar(df["isim"], df["not"], color="coral")
plt.title("Öğrenci Notları")
plt.xlabel("İsim")
plt.ylabel("Not")
plt.savefig("notlar.png")
plt.close()
print("notlar.png kaydedildi!")

# 2. Dağılım grafiği — yaş ve not ilişkisi
plt.figure(figsize=(8, 5))
plt.scatter(df["yas"], df["not"], color="blue", s=100)
for i, row in df.iterrows():
    plt.annotate(row["isim"], (row["yas"], row["not"]))
plt.title("Yaş - Not İlişkisi")
plt.xlabel("Yaş")
plt.ylabel("Not")
plt.savefig("yas_not.png")
plt.close()
print("yas_not.png kaydedildi!")

# 3. Pasta grafik — bölüm dağılımı
plt.figure(figsize=(8, 8))
plt.pie(df["not"], labels=df["isim"], autopct="%1.1f%%")
plt.title("Not Dağılımı")
plt.savefig("pasta.png")
plt.close()
print("pasta.png kaydedildi!")