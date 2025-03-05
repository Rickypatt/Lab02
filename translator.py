class Translator:

    def __init__(self,dizionario):
           self.dizionario = dizionario

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("-----------------------------"+ "\n" +
              "  Translator Alien-Italian" +"\n" + "\n" +
              "-----------------------------" + "\n" +
              " 1. Aggiungi nuova parola" + "\n" +
              " 2. Cerca una traduzione" + "\n" +
              " 3. Cerca con wildcard" + "\n" +
              " 4. Stampa tutto il dizionario" + "\n" +
              " 5. Exit" + "\n" +
              "-----------------------------" + "\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r") as file:
            for line in file:
                campi = line.rstrip().lower().split(" ")
                self.dizionario.parole[campi[0]] = [campi[1]]

        # return self.dizionario

    def handleAdd(self,fileName):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        print()
        txtIn1 = input("Ok, quale parola devo aggiungere? ")
        campi = txtIn1.strip().lower().split(maxsplit=1)
        if len(campi) != 2:
            raise Exception("Indicazioni sbagliate, riprova")
        else:
            self.dizionario.addWord(fileName,campi[0], campi[1])

    def handleTranslate(self):
        # query is a string <parola-aliena>
        print()
        txtIn2 = input("Ok, quale parola devo cercare? ")
        if txtIn2.rstrip().lower() in self.dizionario.parole:
            return self.dizionario.translate(txtIn2.lower())
        else:
            raise Exception("Indicazioni sbagliate, riprova")

    def handleWildCard(self):
        # query is a string with a ? --> <par?la_aliena>
        print()
        txtin3 = input("Ok, quale parola con '?' devo cercare? ")
        return self.dizionario.translateWordWildCard(txtin3.lower())

