def hitung(nilai1, nilai2):
    hasil = nilai1 - nilai2
    return -hasil if hasil < 0 else hasil

def mutlak(angka):
    return -angka if angka < 0 else angka

if __name__ == "__main__":
    
    a, c, b, d = map(int, input().split())
    
    Hasil = hitung(a, b) + hitung(c, d)
    print(mutlak(Hasil))