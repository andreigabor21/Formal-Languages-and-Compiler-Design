class Grammar:
    def __init__(self, filename="g1.txt"):
        self.file = filename
        self.grammar = self.read_grammar()
        self.N = self.grammar[0]
        self.E = self.grammar[1]
        self.S = self.grammar[2]
        self.P = self.represent_productions(self.grammar[3])


    # read the grammar from file
    def read_grammar(self):
        grammar = []
        with open(self.file) as file:
            # get the set of  non-terminal symbols
            line = file.readline()
            grammar.append(line[0:-1].split(" "))
            # get the alphabet (set of terminal symbols)
            line = file.readline()
            grammar.append(line[0:-1].split(" "))
            # get the start symbol
            line = file.readline()
            grammar.append(line[0:-1].split(" "))
            # get the finite set of productions
            p = []
            line = file.readline()
            while line:
                production = line[0:-1]

                p.append(production.split(" "))
                line = file.readline()
            grammar.append(p)
        return grammar

    @staticmethod
    def represent_productions(productions):
        productions_dictionary = {}
        for production in productions:
            if production[0] not in productions_dictionary.keys():
                productions_dictionary[production[0]] = []
            productions_dictionary[production[0]].append(production[1].split("$"))
        return productions_dictionary

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


#menu()