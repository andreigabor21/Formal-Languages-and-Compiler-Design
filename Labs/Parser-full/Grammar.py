class Grammar:
    def __init__(self, filename="g1.txt"):
        self.file = filename
        self.grammar = self.read_grammar()
        self.N = self.grammar[0]
        self.E = self.grammar[1]
        self.P = self.represent_productions(self.grammar[3])
        self.S = self.grammar[2]

    # read the grammar from file
    def read_grammar(self):
        g = []
        with open(self.file) as f:
            # get the set of  non-terminal symbols
            line = f.readline()
            g.append(line[0:-1].split(" "))
            # get the alphabet (set of terminal symbols)
            line = f.readline()
            g.append(line[0:-1].split(" "))
            # get the start symbol
            line = f.readline()
            g.append(line[0:-1].split(" "))
            # get the finite set of productions
            p = []
            line = f.readline()
            while line:
                production = line[0:-1]

                p.append(production.split(" "))
                line = f.readline()
            g.append(p)
        return g

    @staticmethod
    def represent_productions(productions):
        rep = {}
        for p in productions:
            if p[0] not in rep.keys():
                rep[p[0]] = []
            rep[p[0]].append(p[1].split("@"))
        return rep

    def get_non_terminals(self):
        return self.N

    def get_terminals(self):
        return self.E

    def get_start_symbol(self):
        return self.S

    def get_productions(self):
        return self.P

    def get_productions_for_non_terminal(self, symbol):
        return self.P[symbol]

    def print_productions_for_non_terminal(self, symbol):
        string_builder = ""
        if symbol in self.P.keys():
            string_builder += "The productions for {0} are: \n".format(symbol)
            for p in self.P[symbol]:
                string_builder += symbol + " -> " + " ".join(p) + "\n"
        else:
            string_builder += "There is no such non terminal"
        return string_builder

def menu():
    grammar = Grammar("g1.txt")
    while True:
        try:
            option = int(input(
                "\nEnter \n1 get the set of  non-terminal symbols \n2 get the alphabet (set of terminal symbols) \n3 "
                "get the start symbol \n4 get the finite set of productions \n5 get productions from a non-terminal "
                "\n0 to exit.\n>> "))
            if option == 1:
                print(grammar.get_non_terminals())
            elif option == 2:
                print(grammar.get_terminals())
            elif option == 3:
                print(grammar.get_start_symbol())
            elif option == 4:
                print(grammar.get_productions())
            elif option == 5:
                nt = input("Give non-terminal >> ")
                print(grammar.print_productions_for_non_terminal(nt))
            elif option == 0:
                return
            else:
                print("Wrong option!")
        except Exception as e:
            print(e)
            print("Something went wrong!")


# menu()