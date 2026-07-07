def displayEven(no):
    for i in range(2, (2*no)+1, 2):
        print(i, end=" ")
def main():
    displayEven(10)
if(__name__ == "__main__"):
    main()