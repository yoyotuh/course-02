from myUtil import inputAngka
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
   
    number=int(inputAngka())
    print(factorial(number)) 

if __name__ == "__main__":
    main()