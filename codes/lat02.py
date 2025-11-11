def inputAngka():
    while True:
        try:
            number = input("input angka: ")
            int(number)       
            return number
        except ValueError:
            print("Masukkan hanya angka saja!")
        
number  = inputAngka()
temp  = sum(int(digit) for digit in number)
print("Jumlah :", temp)
# ini code baru

