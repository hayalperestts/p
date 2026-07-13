import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Veriyi yükle
df = pd.read_csv("ogrenciler.csv")

# X = özellik (yaş), y = hedef (not)
X = df[["yas"]]
y = df["not"]

# Eğitim ve test verisi olarak böl
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Eğitim verisi:", len(X_train), "satır")
print("Test verisi:", len(X_test), "satır")

# Model oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

# Model katsayıları
print("\nModel katsayısı (eğim):", model.coef_[0])
print("Sabit (intercept):", model.intercept_)

# Tahmin yap
y_pred = model.predict(X_test)

print("\n--- Tahminler vs Gerçek ---")
for gercek, tahmin in zip(y_test, y_pred):
    print(f"Gerçek: {gercek} | Tahmin: {tahmin:.1f}")

# Hata ölçümü
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"\nRMSE (Hata): {rmse:.2f}")

# Yeni tahmin
yeni_yas = [[20]]
tahmin = model.predict(yeni_yas)
print(f"\n20 yaşındaki öğrencinin tahmini notu: {tahmin[0]:.1f}")