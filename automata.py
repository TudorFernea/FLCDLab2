
class Automata:

    def __init__(self, transitions, alphabet, states, initial_states, final_states):
        self.transitions = transitions
        self.alphabet = alphabet
        self.states = states
        self.initial_states = initial_states
        self.final_states = final_states

    def verify(self, input, state):

        if input != "":
            for transition in self.transitions:
                if transition[0] == state:
                    if transition[1] != "a-z" and transition[1] != "A-Z" and transition[1] != "0-9" and transition[1] != "1-9":
                        if transition[1] != "alphabet":
                            if transition[1] == input[0]:
                                return False or self.verify(input[1:], transition[2])
                        elif input[0] in self.get_alphabet():
                            return False or self.verify(input[1:], transition[2])
                    elif input[0] in self.get_range(transition[1]):
                        return False or self.verify(input[1:], transition[2])
            return False
        else:
            if state in self.final_states:
                return True
            else:
                return False

    def print_states(self):
        print(self.states)

    def print_alphabet(self):
        print(self.alphabet)

    def print_transitions(self):
        for transition in self.transitions:
            print(transition)

    def print_final_states(self):
        print(self.final_states)

    def get_alphabet(self):
        res = []
        for c in self.alphabet:
            if c not in ["a-z", "A-Z", "0-9", "1-9"]:
                res.append(c)
            else:
                res += self.get_range(c)
        return res

    def get_range(self, rng):
        res = []

        if rng == "a-z":
            for c in range(ord("a"), ord("z")+1):
                res.append(chr(c))
            return res

        if rng == "A-Z":
            for c in range(ord("A"), ord("Z")+1):
                res.append(chr(c))
            return res

        if rng == "0-9":
            for c in range(ord("0"), ord("9")+1):
                res.append(chr(c))
            return res

        if rng == "1-9":
            for c in range(ord("1"), ord("9")+1):
                res.append(chr(c))
            return res

        return None

def print_menu():
    print("1. Display states")
    print("2. Display alphabet")
    print("3. Display transitions")
    print("4. Display final states")
    print("0. Exit")

def read_transitions():
    f = open("FA.in", "r")
    transitions = []
    alphabet = []
    states = []
    initial_states = []
    final_states = []
    t = ""
    f.readline()
    while t != "Alphabet":
        t = f.readline().strip("\n")
        if not t:
            break
        t.split(",")
        transitions.append(t)

    while t != "States":
        t = f.readline().strip("\n")
        alphabet.append(t)

    while t != "Initial_states":
        t = f.readline().strip("\n")
        states.append(t)

    while t != "Final_states":
        t = f.readline().strip("\n")
        initial_states.append(t)

    while True:
        t = f.readline().strip("\n")
        if not t:
            break
        final_states.append(t)

    return transitions[:-1], alphabet[:-1], states[:-1], initial_states[:-1], final_states


def run():

    transitions, alphabet, states, initial_states, final_states = read_transitions()
    automata_transitions = []

    for t in transitions:
        t = t.split(",")
        automata_transitions.append((t[0], t[1], t[2]))

    a = Automata(automata_transitions, alphabet, states, initial_states, final_states)
    inputt = "\"abcd\""
    input2 = "\"a022333ASBASD34ASaa asd\""
    input3 = "0223"
    input4 = "abcd"

    while True:
        print_menu()
        op = input("Choose option: ")

        if op == "1":
            a.print_states()
        if op == "2":
            a.print_alphabet()
        if op == "3":
            a.print_transitions()
        if op == "4":
            a.print_final_states()
        if op == "0":
            break


    print(a.verify(inputt, "p"))
    print(a.verify(input2, "p"))
    print(a.verify(input3, "p"))
    print(a.verify(input4, "p"))

#run()

