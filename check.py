#6_Check if a number is positive, negative, or zero.

def main():
    try :
        n = int(input("Enter a number: "))
    except Exception as e :
        print (f"The Error is {e}")
    else :
        if n < 0 :
            print (f"{n} is negative")
        elif n == 0 :
            print (f"{n} is zero")
        else :
            print(f"{n} is positive")

    finally :
        print ("This is nice")
main()
