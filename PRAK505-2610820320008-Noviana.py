def Biodata(tahunLahir, A, B):
    tahun_sekarang = 2020
    umur = tahun_sekarang - tahunLahir
    print(f"Perkenalkan Nama Saya: {A}")
    print(f"Umur Saya: {umur}")
    print(f"Saya Adalah Angkatan: {tahun_sekarang}")
    print(f"Asal Saya dari: {B}")

if __name__ == "__main__":
    tahunLahir = int(input())
    A = input()
    B = input()
    Biodata(tahunLahir, A, B)