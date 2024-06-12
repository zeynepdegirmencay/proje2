from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd

def main():
    try:
        # Personel sınıfının nesneleri oluşturuyoruz
        personel1 = Personel(1, "Zeynep", "Değirmençay", "İdari", 5000)
        personel2 = Personel(2, "Duru", "Ayas", "Finansal", 7000)
        print("Personel1:", personel1)
        print("Personel2:", personel2)

        # Doktor sınıfının nesnelerini oluşturuyoruz.
        doktor1 = Doktor(3, "Eren", "Ayas", "Nöroloji", 10000, "Nörolog", 9, " Bayraklı Şehir Hastanesi")
        doktor2 = Doktor(4, "Ahmet", "Yılmaz", "Dahiliye", 9800, "Dahiliye Uzmanı", 11, "Özel Hastane")
        doktor3 = Doktor(5, "Ceren", "Demir", "Kardiyoloji", 9000, "Kardiyolog", 5, " Giresun Devlet Hastanesi")
        print("Doktor1:", doktor1)
        print("Doktor2:", doktor2)
        print("Doktor3:", doktor3)

        # Hemşire sınıfının nesnelerini oluşturuyoruz.
        hemsire1 = Hemsire(6, "Ali", "Koç", "Yoğun bakım", 6000, 40, "İlk Yardım", " Bayraklı Şehir Hastanesi")
        hemsire2 = Hemsire(7, "Fatih", "Terim", "Ruh Sağlığı", 6200, 42, "Psikoterapi", " Giresun Devlet Hastanesi")
        hemsire3 = Hemsire(8, "Arda", "Güler", "Onkoloji", 5800, 38, "Kanserin ilaçla tedavisi", "Özel Hastane")
        print("Hemşire1:", hemsire1)
        print("Hemşire2:", hemsire2)
        print("Hemşire3:", hemsire3)

        # Hasta sınıfının nesnelerini oluşturuyoruz.
        hasta1 = Hasta(9, "Eylül", "Kiraz", "1995-04-12", "Ateşli Hastalık", "İlaç Tedavisi")
        hasta2 = Hasta(10, "Aslan", "Yılmaz", "2000-09-22", "Kırık/Çıkık", "Alçı")
        hasta3 = Hasta(11, "Can", "Kara", "1988-11-30", "Ameliyat", "Cerrahi Müdahale")
        print("Hasta1:", hasta1)
        print("Hasta2:", hasta2)
        print("Hasta3:", hasta3)

        # Pandasla DataFrame oluşturuyoruz liste oluşturarak.
        data = {
            "Personel No": [
                personel1.get_personel_no(), personel2.get_personel_no(), doktor1.get_personel_no(),
                doktor2.get_personel_no(), doktor3.get_personel_no(), hemsire1.get_personel_no(),
                hemsire2.get_personel_no(), hemsire3.get_personel_no(), hasta1.get_hasta_no(),
                hasta2.get_hasta_no(), hasta3.get_hasta_no()
            ],
            "Ad": [
                personel1.get_ad(), personel2.get_ad(), doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(),
                hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(), hasta1.get_ad(),
                hasta2.get_ad(), hasta3.get_ad()
            ],
            "Soyad": [
                personel1.get_soyad(), personel2.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(),
                hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad(), hasta1.get_soyad(),
                hasta2.get_soyad(), hasta3.get_soyad()
            ],
            "Departman": [
                personel1.get_departman(), personel2.get_departman(), doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(),
                hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman(), None, None, None
            ],
            "Maas": [
                personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(),
                hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(), None, None, None
            ],
            "Uzmanlık": [
                None, None, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), None, None, None, None, None, None
            ],
            "Deneyim Yılı": [
                None, None, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(), None, None, None, None, None, None
            ],
            "Hastane": [
                None, None, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(),
                hemsire2.get_hastane(), hemsire3.get_hastane(), None, None, None
            ],
            "Çalışma Saati": [
                None, None, None, None, None, hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(), None, None, None
            ],
            "Sertifika": [
                None, None, None, None, None, hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(), None, None, None
            ],
            "Hasta No": [
                None, None, None, None, None, None, None, None, hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()
            ],
            "Doğum Tarihi": [
                None, None, None, None, None, None, None, None, hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()
            ],
            "Hastalık": [
                None, None, None, None, None, None, None, None, hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()
            ],
            "Tedavi": [
                None, None, None, None, None, None, None, None, hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()
            ]
        }

        df = pd.DataFrame(data)

        
        df = df.fillna(0) # None olarak tanımlanan boş değerler için 0 atamak için yazdık.

        
        uzmanlik_grup = df[df["Uzmanlık"] != 0].groupby("Uzmanlık").size() #Doktorları uzmanlıklarına göre gruplandırıp sayılarını buluyoruz.
        print("\nUzmanlıklarına Göre Doktor Sayıları:\n", uzmanlik_grup)

        deneyimli_doktorlar = df[(df["Deneyim Yılı"] > 5)].shape[0] # 5 yıldan fazla deneyimli doktorların sayısını bulmak
        print("\n5 Yıldan Fazla Deneyimi Olan Doktor Sayısı:", deneyimli_doktorlar)

        df_sorted_by_name = df.sort_values("Ad") #Hasta adlarını alfabetik sıralama 
        print("\nHasta Adına Göre Sıralanmış DataFrame:\n", df_sorted_by_name)

        maasi_7000_ustundeyse = df[df["Maas"] > 7000]  # Maaşı 7000 TL üstü olan personelleri bulmak için
        print("\nMaaşı 7000 TL Üzerinde Olan Personeller:\n", maasi_7000_ustundeyse)

        # Doğum tarihi 1990 ve sonrası olan hastaları gösterme
        df["Doğum Tarihi"] = pd.to_datetime(df["Doğum Tarihi"])
        dogum_tarihi_1990_sonrasi = df[(df["Doğum Tarihi"] >= "1990-01-01")]
        print("\nDoğum Tarihi 1990 ve Sonrası Olan Hastalar:\n", dogum_tarihi_1990_sonrasi)

        yeni_df = df[["Ad", "Soyad", "Departman", "Maas", "Uzmanlık", "Deneyim Yılı", "Hastalık", "Tedavi"]] #Bulduklarımızı yeni DataFrame'e dönüştürüyoruz.
        # Yeni DataFrame'i yazdırma
        print("\nYeni DataFrame:\n", yeni_df)

    except Exception as e: #Hatayı ve hatanın türünü bulmamıza yardımcı oluyor.
        print("Bir hata oluştu:", str(e))


if __name__ == "__main__":
    main()
