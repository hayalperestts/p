from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Veriyi yükle
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["tur"] = iris.target

print("İlk 5 satır:")
print(df.head())
print("\nÇiçek türleri:", iris.target_names)
print("Veri boyutu:", df.shape)

# X ve y ayır
X = iris.data
y = iris.target

# Eğitim/test böl
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model kur ve eğit
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)

# Doğruluk
print("\nDoğruluk (Accuracy):", accuracy_score(y_test, y_pred))
print("\nDetaylı Rapor:")
print(classification_report(y_test, y_pred, 
      target_names=iris.target_names))

# Yeni çiçek tahmini
yeni_cicek = [[5.1, 3.5, 1.4, 0.2]]
tahmin = model.predict(yeni_cicek)
print("Yeni çiçeğin türü:", iris.target_names[tahmin[0]])