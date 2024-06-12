class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    # Get metotları
    def get_hasta_no(self):
        return self.__hasta_no

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi

    def get_hastalik(self):
        return self.__hastalik

    def get_tedavi(self):
        return self.__tedavi

    # Set metotları
    def set_ad(self, ad):
        self.__ad = ad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik

    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi

    # Tedavi süresi hesapla metodu
    def tedavi_suresi_hesapla(self):
        # Örneğin tedavi süresini hastalık ismine göre belirleyebiliriz
        tedavi_sureleri = {
            "Ateşli Hastalık": 10,
            "Kırık/Çıkık": 30,
            "Ameliyat": 120
        }
        if self.__hastalik in tedavi_sureleri:
            return tedavi_sureleri[self.__hastalik]
        else:
            # Varsayılan bir hesaplama veya açıklama yapılabilir.
            return f"{self.__hastalik} için tedavi süresi bilinmiyor."

    # __str__ metodu
    def __str__(self):
        return f"Hasta No: {self.__hasta_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}"
