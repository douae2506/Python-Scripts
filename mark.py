#7_Take a mark and print "Pass" or "Fail".

from word2number import w2n

def main():
    mark = input("Enter your note: ")
    result = w2n.word_to_num(mark)
    if result > 10 :
        print ("Pass")
    else :
        print ("Fail")


main()

