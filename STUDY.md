class Ogrenci:
    def __init__(self, isim, yas, bolum):
        self.isim = isim
        self.yas = yas
        self.bolum = bolum

    def bilgi_goster(self):
        return f"{self.isim} | {self.yas} | {self.bolum}"


ogrenciler = []


def ogrenci_ekle():
    isim = input("İsim: ")
    yas = input("Yaş: ")
    bolum = input("Bölüm: ")

    ogrenci_bilgileri = {
        "isim": isim,
        "yas": yas,
        "bolum": bolum
    }

    yeni_ogrenci = Ogrenci(
        ogrenci_bilgileri["isim"],
        ogrenci_bilgileri["yas"],
        ogrenci_bilgileri["bolum"]
    )

    ogrenciler.append(yeni_ogrenci)

    print("Öğrenci eklendi!")


def ogrencileri_listele():
    print("--- Öğrenciler ---")

    if len(ogrenciler) == 0:
        print("Henüz öğrenci eklenmedi.")
    else:
        for sira, ogrenci in enumerate(ogrenciler, start=1):
            print(f"{sira}. {ogrenci.bilgi_goster()}")


def ogrenci_ara():
    aranacak_isim = input("Aranacak isim: ")

    bulundu = False

    for ogrenci in ogrenciler:
        if ogrenci.isim.lower() == aranacak_isim.lower():
            print(f"Bulundu! {ogrenci.bilgi_goster()}")
            bulundu = True
            break

    if bulundu == False:
        print("Öğrenci bulunamadı.")


while True:
    print()
    print("1. Öğrenci ekle")
    print("2. Öğrencileri listele")
    print("3. Öğrenci ara")
    print("4. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        ogrenci_ara()

    elif secim == "4":
        print("Güle güle!")
        break

    else:
        print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 girin.")
        