def masksimal(a, b):
    return a if a > b else b
def minimal(a, b):
    return a if a < b else b

if __name__ == "__main__":
    bilangan = int (input())
    nilai_list = list(map(int, input().split()))
    maks = -10000
    minim = 10000
    batas = 0
    while batas < bilangan:
        nilai = nilai_list[batas]
        maks = masksimal(maks, nilai)
        minim = minimal(minim, nilai)
        batas += 1
    print(f"{maks} {minim}")