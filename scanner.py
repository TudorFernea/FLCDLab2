from automata import read_transitions, Automata
from table import HashTable

import re

class Scanner:

    def __init__(self):
        self.tokens = []
        self.operators = ["+", "-", "==", "/", "%", "<=", ">=", "!=", "!", "="]
        self.separators = [" ", ";", "(", ")", "\n", "{", "}", ",", "\t","."]
        self.identifier = r'^[a-zA-Z]([a-zA-Z]|[0-9])*$'
        self.constant = r'^\".*\"$|^\'.*\'$'
        transitions, alphabet, states, initial_states, final_states = read_transitions("identifier.in")
        automata_transitions = []

        for t in transitions:
            t = t.split(",")
            automata_transitions.append((t[0], t[1], t[2]))

        self.automataIdentifier = Automata(automata_transitions, alphabet, states, initial_states, final_states)

        transitions, alphabet, states, initial_states, final_states = read_transitions("FA.in")
        automata_transitions = []

        for t in transitions:
            t = t.split(",")
            automata_transitions.append((t[0], t[1], t[2]))

        self.automataConstant = Automata(automata_transitions, alphabet, states, initial_states, final_states)

    def tokenize(self, line, linenum):

        index = 0
        token = ""
        inString = False
        while index < len(line):

            c = line[index]


            if self.isInOperator(c) and not inString:
                self.tokens.append((token,linenum))
                token, index = self.getOperator(line, index)
                self.tokens.append((token,linenum))
                token = ""
            else:
                if self.isSeparator(c) and not inString:
                    self.tokens.append((token,linenum))
                    token = ""
                else:
                    if c == '"':
                        if inString:
                            token += c
                            self.tokens.append((token,linenum))
                            token = ""
                            inString = False
                        else:
                            token += c
                            inString = True
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
        PIF = []

        linenum = 0
        for l in lines:
            linenum += 1
            scanner.tokenize(l, linenum)

        for p in scanner.tokens:
            if p[0] == "":
                scanner.tokens.remove(p)

        index = 0

        error = False

        for p in scanner.tokens:

            t = p[0]



            if t in scanner.separators or t in scanner.operators or t in tok:
                PIF.append((t, 0))
            else:
                if scanner.automataIdentifier.verify(t, scanner.automataIdentifier.initial_states[0]) != False or scanner.automataConstant.verify(t, scanner.automataIdentifier.initial_states[0]) != False or re.search(scanner.constant, t) != None: #if scanner.automata.verify(t, scanner.automata.initial_states[0]) != False ...
                    if ST.get(t) == -1:
                        index += 1
                        ST.insert(t, index)
                    insertIndex = ST.get(t)
                    PIF.append(("id", insertIndex))
                else:
                    error = True
                    print(f"Lexical error at {p[0]} line {p[1]}")

        pifOut = open("PIF.out","w")
        stOUT = open("ST.out","w")

        if error == False:
            print("Lexically correct")

        #print(scanner.tokens)
        stOUT.write("Symbol table using hash table \n")
        stOUT.write(str(ST))
        for p in PIF:
            pifOut.write(str(p)+"\n")


run()