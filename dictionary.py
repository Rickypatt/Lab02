import re

class Dictionary:

    def __init__(self):
        self.parole = {}

    def addWord(self,fileName, parolaAliena, traduzione):

            if parolaAliena not in self.parole:
                self.parole[parolaAliena] = traduzione
                with open(fileName, "a") as file:
                    file.write(f"\n{parolaAliena} {traduzione}")
            else:
                self.parole[parolaAliena].append(traduzione)
                with open(fileName, "r") as file:
                    righe = file.readlines()
                    for i, riga in enumerate(righe):
                        campi = riga.rstrip().split(" ")
                        if campi[0] == parolaAliena:
                            righe[i] += " "+ traduzione

                with open(fileName, "w") as file:
                    file.writelines(righe)

    def translate(self,parolaAliena):
        return self.parole[parolaAliena]

    def translateWordWildCard(self,parolaWild):
        sost = parolaWild.replace('?','.')
        regex = re.compile(sost)
        mystr = [p for p in self.parole if regex.fullmatch(p)]
        risultato = ""
        for p in mystr:
            risultato += f"{p} {self.parole[p]} \n"

        return risultato

    def stampaDizionario(self):
        mystr = ""
        for parola, traduzione in self.parole.items():
            mystr += f"Parola: {parola} Traduzioni: {traduzione} \n"

        return mystr