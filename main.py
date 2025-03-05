from dictionary import Dictionary
import translator as tr

dizionario = Dictionary()
t = tr.Translator(dizionario)
gira = True

while gira:
    t.printMenu()
    t.loadDictionary("dictionary.txt")
    txtIn = input("Cosa vuoi fare: ")

# Add input control here!

    if int(txtIn) == 1:
        print(t.handleAdd("dictionary.txt"))

    elif int(txtIn) == 2:
        print(t.handleTranslate())

    elif int(txtIn) == 3:
        print(t.handleWildCard())

    elif int(txtIn) == 4:
        print(t.dizionario.stampaDizionario())

    elif int(txtIn) == 5:
        gira = False