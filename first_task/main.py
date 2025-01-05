def isEven(value: int) -> bool:
    return value % 2 == 0

def myIsEven(value: int) -> bool:
    return value & 1 == 0

def main() -> None:
    num = int(input('Введите число: '))
    if myIsEven(num):
        print("Число четное!")
    else:
        print("Число нечетное!")

if __name__ == "__main__":
    main()
