class BangunDatar():
    def __init__(self, panjang, lebar):
        self.p = panjang
        self.l = lebar
    
    def HitungLuas(self):
        global hasil
        hasil = self.p * self.l

        return hasil
        

    def show(self):
        print(hasil)
        
