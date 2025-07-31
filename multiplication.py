#8Print the multiplication table of a number.


def main():
    n = int(input("Enter a number: "))
    for i in range(10):
        print(f"{n}x{i} = {n*i}")


main()
