#9Sum all numbers from 1 to N (user input).


def main():
    n = int(input("Enter n: "))
    m = 0
    for i in range(1, n + 1):
        m = i + m
    print(f"the sum = {m}")


main()
