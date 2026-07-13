import numpy as np

# 1. Dizi oluşturma
dizi = np.array([1, 2, 3, 4, 5])
print("Dizi:", dizi)

# 2. Matematiksel işlemler — tek satırda!
print("x2:", dizi * 2)
print("Karesi:", dizi ** 2)
print("Karekök:", np.sqrt(dizi))

# 3. İstatistik
print("Ortalama:", np.mean(dizi))
print("Toplam:", np.sum(dizi))
print("Max:", np.max(dizi))
print("Min:", np.min(dizi))
print("Std Sapma:", np.std(dizi))

# 4. 2 boyutlu dizi (matris)
matris = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\nMatris:\n", matris)
print("Satır x Sütun:", matris.shape)

# 5. Hızlı dizi oluşturma
sifirlar = np.zeros(5)
birler = np.ones(5)
aralik = np.arange(0, 10, 2)  # 0'dan 10'a, 2'şer 2'şer
print("\nSıfırlar:", sifirlar)
print("Birler:", birler)
print("Aralık:", aralik)