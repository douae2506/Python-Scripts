#4Convert Celsius to Fahrenheit.

def main():
    number = int(input("enter a number: "))
    result = format(convert(number), ".3f")
    print(f"{number}C is {result}F ")


def convert(n):
    m = n * 33.800
    return m


main()
