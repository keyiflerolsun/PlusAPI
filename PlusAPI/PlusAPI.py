from requests_html import HTMLSession
from simplejson.errors import JSONDecodeError

class PlusAPI:
    def __repr__(self):
        return f"{__class__.__name__} | Piyasa Verileri Sınıfı"

    def __init__(self, token:str):
        """PlusAPI | Piyasa Verileri Sınıfı
        
        Gereksinimler
        -------------
            token:str = XXXX
        
        Methodlar
        ---------
            .hisse_ver(sembol:str) -> dict:
                İstenilen Sembolün Bilgilerini Çevirir

            .hisse_sepet -> dict:
                BIST Top-10 Çevirir

            .kripto_ver(sembol:str) -> dict:
                İstenilen Sembolün Bilgilerini Çevirir

            .kripto_haber -> dict:
                Kriptolar Hakkında Güncel Haberleri Çevirir

            .kripto_sepet -> dict:
                Kripto Top-10 Çevirir
        """
        self.token  = token
        self.oturum = HTMLSession()

    def hisse_ver(self, sembol:str) -> dict:
        "İstenilen Sembolün Bilgilerini Çevirir"
        try:
            istek = self.oturum.get(f"https://plusapi.org/api/hisse?token={self.token}&sembol={sembol.upper()}").json()
        except JSONDecodeError:
            return {'token': self.token, 'hata': f"« {sembol} » Hisse Veri Tabanında Mevcut Değil!"}

        if istek['code'] == 200:
            return istek['data']
        else:
            return {'token': self.token, 'hata': istek['text']}

    @property
    def hisse_sepet(self) -> dict:
        "BIST Top-10 Çevirir"
        istek = self.oturum.get(f"https://plusapi.org/api/hisse/sepet?token={self.token}").json()
        if 'data' not in istek.keys():
            return {'token': self.token, 'hata': istek['text']}

        return istek['data']

    def kripto_ver(self, sembol:str) -> dict:
        "İstenilen Sembolün Bilgilerini Çevirir"
        try:
            istek = self.oturum.get(f"https://plusapi.org/api/kripto?token={self.token}&sembol={sembol.upper()}").json()
        except JSONDecodeError:
            return {'token': self.token, 'hata': f"« {sembol} » Kripto Veri Tabanında Mevcut Değil!"}

        if istek['code'] == 200:
            return istek['data']
        else:
            return {'token': self.token, 'hata': istek['text']}

    @property
    def kripto_haber(self) -> dict:
        "Kriptolar Hakkında Güncel Haberleri Çevirir"
        istek = self.oturum.get(f"https://plusapi.org/api/kripto/haber?token={self.token}").json()
        if 'data' not in istek.keys():
            return {'token': self.token, 'hata': istek['text']}

        return istek['data']

    @property
    def kripto_sepet(self) -> dict:
        "Kripto Top-10 Çevirir"
        istek = self.oturum.get(f"https://plusapi.org/api/kripto/sepet?token={self.token}").json()
        if 'data' not in istek.keys():
            return {'token': self.token, 'hata': istek['text']}

        return istek['data']

# bakalim = PlusAPI("a3d46c9ce8066b7e07c48cb4e069763")
# print(bakalim.hisse_ver("SASA"))
# print(bakalim.hisse_sepet)
# print(bakalim.kripto_ver("BTC"))
# print(bakalim.kripto_haber)
# print(bakalim.kripto_sepet)
# print(bakalim.__dict__)