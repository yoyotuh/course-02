def inputAngka():
    while True:
        try:
            number = input("input angka: ")
            int(number)       
            return number
        except ValueError:
            print("Masukkan hanya angka saja!")
     