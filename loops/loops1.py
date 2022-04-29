
def main():
    try:
        while True:
                x = int(input("x: "))
                y = int(input("y: "))
                if x > y:
                    print("x is greater than y")
                else:
                    print("y is greater than x")
    except:
        print("Bye!")

if __name__ == '__main__':
    main()
