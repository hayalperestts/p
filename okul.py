import sqlite3

baglanti = sqlite3.connect("okul.db")
cursor = baglanti.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ogrenciler (
        id INTEGER PRIMARY KEY,
        isim TEXT,
        yas INTEGER,
        bolum TEXT
    )
""")

cursor.execute("INSERT INTO ogrenciler VALUES (1, 'Selin', 19, 'Çalışma Ekonomisi')")
cursor.execute("INSERT INTO ogrenciler VALUES (2, 'Kerime', 21, 'CEO')")
cursor.execute("INSERT INTO ogrenciler VALUES (3, 'Kenan', 25, 'Mühendislik')")

baglanti.commit()

cursor.execute("SELECT * FROM ogrenciler")
sonuclar = cursor.fetchall()

print("--- Tüm Öğrenciler ---")
for satir in sonuclar:
    print(satir)

cursor.execute("SELECT * FROM ogrenciler WHERE yas > 20")
sonuclar = cursor.fetchall()

print("--- Yasi 20den Buyuk ---")
for satir in sonuclar:
    print(satir)

baglanti.close()