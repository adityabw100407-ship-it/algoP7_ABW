while True:
    print("\n===== MENU =====")
    print("1. A Pangkat B")
    print("2. Hitung 1 - 2/3 + 5/8 - 13/21 + ...")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        a = int(input("Masukkan suatu bilangan bulat: "))
        b = int(input("Masukkan pangkat yang diinginkan: "))

        for i in range(1, b + 1):
            hasil = a ** i
            print(f"hasil {a} pangkat {i} adalah {hasil}")

    elif pilihan == "2":
        n = int(input("Masukkan jumlah N: "))

        f1, f2 = 1, 1
        total = 0

        for i in range(1, n + 1):
            suku = f1 / f2

            if i % 2 == 1:
                total += suku
            else:
                total -= suku

            f3 = f1 + f2
            f4 = f2 + f3
            f1, f2 = f3, f4

        print("Hasil =", total)

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")