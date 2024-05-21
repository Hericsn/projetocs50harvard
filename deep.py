def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    if answer.lower() == "42":
        print("Yes")
    elif answer.lower() == "forty-two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
