from table import HashTable

class Scanner:

    def __init__(self):
        self.tokens = []
        self.operators = ["+", "-", "==", "/", "%", "<=", ">=", "!=", "!", "="]
        self.separators = [" ", ";", "(", ")", "\n", "{", "}", ","]

    def tokenize(self, line):

        index = 0
        token = ""
        while index < len(line):

            c = line[index]

            if self.isInOperator(c):
                self.tokens.append(token)
                token, index = self.getOperator(line, index)
                self.tokens.append(token)
                token = ""
            else:
                if self.isSeparator(c):
                    self.tokens.append(token)
                    token = ""
                else:
                    token += c
            index += 1




    def getOperator(self, line, index):

        token = ""

        while line[index] != "\n" and self.isInOperator(line[index]):
            token += line[index]
            index += 1

        return token, index-1

    def isInOperator(self, c):
        for op in self.operators:
            if c in op:
                return True
        return False

    def isSeparator(self, c):
        for sep in self.separators:
            if c in sep:
                return True
        return False





def run():

    with open("p.txt", "r") as p:

        tok = open("token.in","r")
        tok = tok.read()
        tok = tok.split("\n")
        p = p.read()
        lines = p.split("\n")

        scanner = Scanner()
        ST = HashTable()
        PIF = HashTable()

        for l in lines:
            scanner.tokenize(l)

        scanner.tokens = list(filter(("").__ne__, scanner.tokens))

        index = 0

        print(tok)

        for t in scanner.tokens:

            if t in scanner.separators or t in scanner.operators or t in tok:
                PIF.insert(t,0)
            else:
                index += 1
                ST.insert(t,index)
                PIF.insert("id", index)

        print(scanner.tokens)
        print(ST)
        print(PIF)


run()