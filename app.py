def luas_persegi(panjang, lebar):
    """Menghitung luas persegi."""
    luas = panjang * lebar
    return luas

def main():
    """Program utama."""
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = luas_persegi(panjang, lebar)
    print("Luas persegi:", luas)

if __name__ == "__main__":
    main()