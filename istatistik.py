import pandas as pd
import numpy as np

df = pd.read_csv("ogrenciler.csv")

notlar = df["not"]

print("=== BETİMSEL İSTATİSTİK ===")
print("Ortalama (Mean):", notlar.mean())
print("Medyan (Median):", notlar.median())
print("Mod (Mode):", notlar.mode()[0])
print("Standart Sapma:", notlar.std())
print("Varyans:", notlar.var())
print("Min:", notlar.min())
print("Max:", notlar.max())
print("Ranj:", notlar.max() - notlar.min())

print("\n=== ÇEYREK DEĞERLERİ ===")
print("Q1 (25%):", notlar.quantile(0.25))
print("Q2 (50%):", notlar.quantile(0.50))
print("Q3 (75%):", notlar.quantile(0.75))

print("\n=== KORELASYON ===")
print("Yaş-Not korelasyonu:", df["yas"].corr(df["not"]))