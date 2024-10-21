def countLetterA(string):
    counter = 0
    for c in string:
        if c in ['a', 'A']:
            counter += 1

    return counter

def main():
    string = input("Entre um texto nesta linha para contar a quantidade de a's: ")
    print(f"A letra 'A' apareceu {countLetterA(string)}")

if __name__=='__main__':
    main()